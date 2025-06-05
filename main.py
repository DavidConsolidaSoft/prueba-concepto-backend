import os
import sys
import asyncio
import logging
import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mensaje de inicio
logger.info("Iniciando la aplicación...")

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
logger.info("Path del sistema configurado")

# Importaciones configurables
settings = None
api_router = None
query_processor = None
enhanced_processor = None

# Flag para servicios opcionales
USE_REDIS_SERVICES = os.getenv("USE_REDIS_SERVICES", "False").lower() == "true"
USE_AI_SERVICES = os.getenv("USE_AI_SERVICES", "False").lower() == "true"
USE_MCP_TOOLS = os.getenv("USE_MCP_TOOLS", "True").lower() == "true"

# Importar configuración PRIMERO
try:
    logger.info("Importando configuración...")
    from app.core.config import settings
    logger.info("Configuración importada correctamente")
except Exception as e:
    logger.error(f"Error al importar configuración: {str(e)}")
    # Crear configuración por defecto para evitar errores
    class DefaultSettings:
        ENVIRONMENT = "development"
        ALLOWED_ORIGINS = ["*"]
    settings = DefaultSettings()

# Importar MCP tools DESPUÉS de la configuración
consolida_mcp = None
if USE_MCP_TOOLS:
    try:
        logger.info("Importando MCP tools...")
        from app.api.v1.services.mcp_tools import get_consolida_mcp_server
        consolida_mcp = get_consolida_mcp_server()
        logger.info("✅ MCP tools importados correctamente")
    except Exception as e:
        logger.error(f"❌ Error al importar MCP tools: {str(e)}")
        logger.warning("Continuando sin MCP tools")
else:
    logger.info("MCP tools deshabilitados por configuración")

# Solo intentar reflejar esquema si Redis está habilitado
db_models = {}
if USE_REDIS_SERVICES:
    try:
        logger.info("Reflejando esquema de base de datos...")
        from app.db.base import reflect_and_cache_schema
        db_models = reflect_and_cache_schema()
        logger.info(f"Esquema cargado: {len(db_models)} modelos")
    except Exception as e:
        logger.error(f"Error al reflejar esquema de BD: {str(e)}")
        logger.warning("Continuando sin esquema de BD cacheado")
else:
    logger.info("Redis deshabilitado, saltando reflejo de esquema")

# Importar routers siempre
try:
    logger.info("Importando routers...")
    from app.api.v1.routers.routers import api_router
    logger.info("Routers importados correctamente")
except Exception as e:
    logger.error(f"Error al importar routers: {str(e)}")
    # Si los routers fallan por dependencias de Redis, intentar routers básicos
    try:
        from app.api.v1.routers.auth.router import router as auth_router
        from fastapi import APIRouter
        api_router = APIRouter()
        api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
        logger.info("Routers básicos de autenticación cargados")
    except Exception as ex:
        logger.error(f"Error al cargar routers básicos: {str(ex)}")

# Solo cargar procesador de consultas si está habilitado
if USE_AI_SERVICES:
    try:
        logger.info("Importando procesador de consultas...")
        from app.api.v1.routers.ai.query_processor import QueryProcessor
        from app.api.v1.routers.ai.schema_integration import enhance_query_processor
        logger.info("Procesador de consultas importado correctamente")
        
        logger.info("Inicializando procesador de consultas...")
        query_processor = QueryProcessor()
        enhanced_processor = enhance_query_processor(query_processor)
        logger.info("Procesador de consultas inicializado correctamente")
    except Exception as e:
        logger.error(f"Error al inicializar procesador de consultas: {str(e)}")
        enhanced_processor = None
else:
    logger.info("Servicios AI deshabilitados, saltando procesador de consultas")

API_VERSION = "1.0.0"
API_TITLE = "Consolida ERP - API"
API_DESCRIPTION = "Llevando la información de tu empresa a la palma de tu mano"

async def initialize_services():
    """Inicializa servicios adicionales (solo si están habilitados)"""
    if not USE_REDIS_SERVICES:
        logger.info("Servicios Redis deshabilitados, saltando inicialización")
        return
        
    try:
        # Inicializar conexión a Redis
        from app.api.v1.routers.ai.redis_service import RedisService
        redis = RedisService()
        if redis.redis_client.ping():
            logger.info("Conexión a Redis establecida correctamente")
            
            # Verificar estado del esquema en Redis
            from app.api.v1.routers.ai.schema_metadata_service import SchemaMetadataService
            schema_service = SchemaMetadataService()
            tables = schema_service.get_all_tables()
            
            # Verificar estado de db_models_ready
            db_models_ready = redis.redis_client.get("db_models_ready")
            schema_version = redis.redis_client.get("schema_version")
            
            logger.info(f"Estado de esquema en Redis: db_models_ready={db_models_ready}, schema_version={schema_version}, tablas={len(tables) if tables else 0}")
            
            # Solo usar semantic cache si está disponible
            if USE_AI_SERVICES:
                from app.api.v1.routers.ai.semantic_cache import SemanticCache
                semantic_cache = SemanticCache()
                examples_added = semantic_cache.add_example_queries(force_update=True)
                if examples_added > 0:
                    logger.info(f"Se añadieron {examples_added} consultas de ejemplo a la caché semántica")
            
            # Reparar inconsistencia si es necesario
            if schema_version and not db_models_ready:
                logger.info("Reparando inconsistencia: Encontrada versión de esquema pero db_models_ready ausente")
                redis.redis_client.set("db_models_ready", "1")
                db_models_ready = b"1"
            
            if not tables or not db_models_ready:
                logger.info("Esquema incompleto en Redis. Iniciando extracción inicial...")
                redis.redis_client.delete("db_models_ready")
                tables_count = schema_service.extract_and_store_schema(force_update=True)
                logger.info(f"Esquema extraído: {tables_count} tablas procesadas")
                redis.redis_client.set("db_models_ready", "1")
            else:
                logger.info(f"Esquema encontrado en Redis: {len(tables)} tablas")
        else:
            logger.warning("No se pudo conectar a Redis")
            
    except Exception as e:
        logger.error(f"Error inicializando servicios Redis: {str(e)}")
        logger.warning("Continuando sin servicios Redis")

# Definir el administrador de contexto para el ciclo de vida de la aplicación
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código que se ejecuta al inicio
    logger.info("Ejecutando código de inicio del ciclo de vida...")
    
    # Inicializar servicios adicionales solo si están habilitados
    if USE_REDIS_SERVICES:
        await initialize_services()
    
    # Inicializar MCP si está disponible
    if consolida_mcp:
        try:
            logger.info("🔧 Configurando MCP tools...")
            app.state.mcp_server = consolida_mcp
            logger.info("✅ MCP tools configurado correctamente")
        except Exception as e:
            logger.error(f"❌ Error configurando MCP: {str(e)}")
    
    # Almacenar procesador mejorado en estado de la app
    if enhanced_processor:
        app.state.enhanced_processor = enhanced_processor
        logger.info("Procesador mejorado disponible en app.state")
    
    # Iniciar tareas en segundo plano solo si están habilitadas
    background_tasks = set()
    
    if USE_AI_SERVICES and enhanced_processor:
        logger.info("Iniciando servicios de fondo...")
        task = asyncio.create_task(run_background_services())
        background_tasks.add(task)
        task.add_done_callback(background_tasks.discard)
    
    yield
    
    # Código que se ejecuta al cierre
    logger.info("Ejecutando código de cierre del ciclo de vida...")
    for task in background_tasks:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            logger.info("Tarea en segundo plano cancelada correctamente")

async def run_background_services():
    """Ejecuta servicios en segundo plano"""
    while True:
        try:
            if enhanced_processor:
                # Ejecutar análisis de consultas
                await asyncio.to_thread(enhanced_processor.analyze_and_precalculate_queries)
                
                # Actualizar embeddings periódicamente si Redis está disponible
                if USE_REDIS_SERVICES:
                    await update_schema_embeddings()
            
            # Esperar 1 hora entre ejecuciones
            await asyncio.sleep(3600)
            
        except Exception as e:
            logger.error(f"Error en servicios de fondo: {str(e)}")
            await asyncio.sleep(300)  # Esperar 5 minutos antes de reintentar

async def update_schema_embeddings():
    """Actualiza embeddings del esquema en Redis"""
    try:
        from app.api.v1.routers.ai.schema_metadata_service import SchemaMetadataService
        service = SchemaMetadataService()
        result = service.refresh_schema()
        if result > 0:
            logger.info(f"Esquema actualizado: {result} tablas procesadas")
        else:
            logger.info("No fue necesario actualizar el esquema")
    except Exception as e:
        logger.error(f"Error actualizando embeddings: {str(e)}")

# Inicializar la aplicación FastAPI
logger.info("Creando aplicación FastAPI...")
app = FastAPI(
    debug=True,
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION,
    lifespan=lifespan
)

# Incluir routers
if api_router:
    logger.info("Incluyendo routers principales...")
    app.include_router(api_router, prefix="/api/v1")
else:
    logger.warning("No se incluyeron routers principales")

# Montar MCP tools si está disponible
if consolida_mcp:
    try:
        logger.info("🔧 Montando MCP en /mcp...")
        app.mount("/mcp", consolida_mcp.streamable_http_app())
        logger.info("✅ MCP montado correctamente en /mcp")
    except Exception as e:
        logger.error(f"❌ Error montando MCP: {str(e)}")

# ===== ENDPOINTS MCP =====

@app.get("/api/mcp/info")
def get_mcp_info():
    """Información sobre MCP tools disponibles"""
    if not consolida_mcp:
        return {
            "status": "unavailable", 
            "message": "MCP tools no están disponibles",
            "enabled": USE_MCP_TOOLS
        }
    
    return {
        "status": "available",
        "name": "Consolida ERP Simple DB Access",
        "version": "1.0.0",
        "endpoint": "/mcp",
        "security": {
            "authentication": "JWT Token",
            "authorization": "Empresa-based filtering",
            "isolation": "Complete cross-empresa isolation"
        },
        "tools": [
            {
                "name": "get_my_empresa_info",
                "description": "Información de MI empresa",
                "requires_jwt": True
            },
            {
                "name": "execute_safe_query",
                "description": "Ejecuta consultas SQL seguras filtradas por MI empresa",
                "requires_jwt": True,
                "parameters": ["query"],
                "security": "Automatic empresa filtering"
            },
            {
                "name": "get_table_schema",
                "description": "Obtiene esquema de tablas",
                "requires_jwt": True,
                "parameters": ["table_name"]
            },
            {
                "name": "test_database_connection",
                "description": "Test conexión a base de datos",
                "requires_jwt": False
            }
        ]
    }

@app.get("/api/mcp/test")
async def test_mcp_connection():
    """Test rápido del MCP"""
    if not consolida_mcp:
        return {
            "mcp_available": False,
            "message": "MCP no está disponible"
        }
    
    try:
        from app.api.v1.services.mcp_tools import execute_query_with_db
        
        result = await execute_query_with_db("SELECT GETDATE() as test_time")
        
        return {
            "mcp_available": True,
            "database_connected": True,
            "test_time": str(result[0]["test_time"]) if result else None,
            "message": "MCP y base de datos funcionando correctamente"
        }
        
    except Exception as e:
        return {
            "mcp_available": True,
            "database_connected": False,
            "error": str(e),
            "message": "MCP disponible pero error de base de datos"
        }

# Ruta de verificación básica
@app.get("/app/status")
def get_status():
    return {
        "status": "running",
        "version": API_VERSION,
        "database_models": len(db_models),
        "query_processor": "active" if enhanced_processor else "inactive",
        "redis_enabled": USE_REDIS_SERVICES,
        "ai_services_enabled": USE_AI_SERVICES,
        "mcp_tools": {
            "enabled": USE_MCP_TOOLS,
            "status": "available" if consolida_mcp else "unavailable",
            "endpoint": "/mcp" if consolida_mcp else None,
            "security_level": "enterprise" if consolida_mcp else "standard"
        }
    }
    
@app.get("/test")
def global_test_route():
    return {
        "status": "OK",
        "message": "API server is running",
        "version": API_VERSION,
        "services": {
            "redis": "enabled" if USE_REDIS_SERVICES else "disabled",
            "ai": "enabled" if USE_AI_SERVICES else "disabled",
            "mcp": "enabled" if USE_MCP_TOOLS else "disabled"
        }
    }

# Configurar CORS - CON PROTECCIÓN CONTRA SETTINGS NULL
logger.info("Configurando CORS...")
try:
    cors_origins = settings.ALLOWED_ORIGINS if settings and hasattr(settings, 'ALLOWED_ORIGINS') else ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Log de CORS solo si settings está disponible
    if settings and hasattr(settings, 'ENVIRONMENT'):
        print(f"🌐 CORS configurado para {settings.ENVIRONMENT}:")
        for origin in cors_origins:
            print(f"   - {origin}")
    else:
        print("🌐 CORS configurado con orígenes por defecto")
        
except Exception as e:
    logger.error(f"Error configurando CORS: {str(e)}")
    # CORS por defecto si hay error
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Manejador de errores global
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Error no controlado: {str(exc)}", exc_info=True)
    return HTTPException(
        status_code=500,
        detail="Error interno del servidor"
    )

# Iniciar servidor
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    logger.info(f"Iniciando servidor en puerto {port}...")
    logger.info(f"Redis: {'Habilitado' if USE_REDIS_SERVICES else 'Deshabilitado'}")
    logger.info(f"Servicios AI: {'Habilitados' if USE_AI_SERVICES else 'Deshabilitados'}")
    logger.info(f"MCP Tools: {'Habilitados' if USE_MCP_TOOLS else 'Deshabilitados'}")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info",
        reload=True
    )