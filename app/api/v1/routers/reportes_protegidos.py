import json
import re
import time
import logging
import traceback
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app.api.v1.routers.ai import embedding_service, redis_service
from app.db.database import get_db
from typing import List, Dict, Any, Optional
from app.api.v1.routers.ai.dynamic_router import safe_execute_orm
from app.api.v1.routers.ai.models import DynamicQueryRequest, DynamicQueryResponse
from app.api.v1.routers.auth.azure_auth import get_current_user
from app.api.v1.routers.ai.schema_integration import enhance_query_processor
from app.api.v1.routers.ai.query_processor import QueryProcessor
from app.api.v1.routers.ai.semantic_cache import SemanticCache

logger = logging.getLogger(__name__)

semantic_cache = SemanticCache()

# Crear router para reportes protegidos
router = APIRouter()

# Inicializar el procesador de consultas y mejorarlo con integración de esquema
query_processor = QueryProcessor()
enhanced_processor = enhance_query_processor(query_processor)


@router.post("/dynamic-query", response_model=DynamicQueryResponse)
async def process_dynamic_query(
    request: Request,
    query_request: DynamicQueryRequest,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    """
    Endpoint principal para consultas dinámicas.
    Procesa una consulta en lenguaje natural y devuelve resultados estructurados.
    """
    start_time = time.time()
    
    try:
        # Opcionalmente, obtener el procesador mejorado del estado de la app
        # si está disponible (configurado en lifespan)
        app_processor = getattr(request.app.state, 'enhanced_processor', None)
        processor = app_processor if app_processor else enhanced_processor
        
        # Paso 1: Generar código ORM usando el esquema y embeddings
        orm_code = processor.chat_service.generate_orm_query(query_request.text)
        
        # Paso 2: Ejecutar el código ORM de forma segura
        results, total_count = safe_execute_orm(orm_code, db, query_request)
        
        # Paso 3: Formatear respuesta
        processing_time = time.time() - start_time
        
        return DynamicQueryResponse(
            results=results,
            orm_code=orm_code,
            processing_time=processing_time,
            total_results=total_count,
            message="Consulta ejecutada exitosamente"
        )
        
    except Exception as e:
        logger.error(f"Error en consulta dinámica: {str(e)}\n{traceback.format_exc()}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al procesar consulta: {str(e)}"
        )

@router.post("/dynamic-query-public", response_model=DynamicQueryResponse)
async def process_dynamic_query_public(
    request: Request,
    query_request: DynamicQueryRequest,
    db: Session = Depends(get_db)
):
    """
    Versión pública del endpoint de consultas dinámicas (para pruebas).
    No requiere autenticación.
    """
    start_time = time.time()
    
    try:
        # NUEVO: Verificar si hay una consulta similar en la caché semántica
        similar_query = semantic_cache.find_similar_query(query_request.text)
        orm_code = None
        source = "cache"
        
        if similar_query and similar_query.get("similarity", 0) > 0.85:
            logger.info(f"Consulta similar encontrada en caché con similitud {similar_query['similarity']:.4f}")
            orm_code = similar_query["orm_code"]
            
            # Ejecutar ORM recuperado
            results, total_count = safe_execute_orm(orm_code, db, query_request)
                
            response = DynamicQueryResponse(
                results=results,
                orm_code=orm_code,
                processing_time=time.time() - start_time,
                total_results=total_count,
                message=f"Consulta ejecutada exitosamente (fuente: cache)"
            )
                
            return response
        else:
            # Si no hay consulta similar, generar ORM con IA
            # Usar el procesador de la aplicación o el local
            app_processor = getattr(request.app.state, 'enhanced_processor', None)
            processor = app_processor if app_processor else enhanced_processor
            
            # Generar código ORM
            orm_code = processor.chat_service.generate_orm_query(query_request.text)
            source = "generated"
            logger.info(f"ORM generado por IA: {orm_code}")
        
        # Ejecutar código ORM
        try:
            results, total_count = safe_execute_orm(orm_code, db, query_request)
        except Exception as orm_error:
            # Si falla la ejecución del ORM, intentar recuperación con embeddings
            logger.warning(f"Error ejecutando ORM generado: {str(orm_error)}")
            
            # Instanciar los servicios necesarios
            embedding_svc = embedding_service.EmbeddingService() 
            redis_svc = redis_service.RedisService()
            
            # Detectar la tabla principal
            table_name = detect_main_table(orm_code, query_request.text, [])
            logger.info(f"Buscando alternativas para tabla: {table_name}")
            
            # Buscar consultas exitosas previas para esta tabla
            table_queries_key = f"semantic:table_queries:{table_name}"
            table_query_ids = redis_svc.redis_client.smembers(table_queries_key)
            
            if table_query_ids:
                # Buscar la consulta más similar en este subconjunto
                fallback_query = None
                highest_sim = 0
                query_embedding = embedding_svc.get_embedding(query_request.text)
                
                for query_id in table_query_ids:
                    if isinstance(query_id, bytes):
                        query_id = query_id.decode('utf-8')
                        
                    emb_key = f"semantic:embedding:{query_id}"
                    cached_emb_json = redis_svc.redis_client.get(emb_key)
                    
                    if cached_emb_json:
                        if isinstance(cached_emb_json, bytes):
                            cached_emb_json = cached_emb_json.decode('utf-8')
                            
                        cached_emb = json.loads(cached_emb_json)
                        similarity = embedding_svc.vector_similarity(query_embedding, cached_emb)
                        
                        if similarity > highest_sim:
                            highest_sim = similarity
                            query_key = f"semantic:query:{query_id}"
                            fallback_query_json = redis_svc.redis_client.get(query_key)
                            if fallback_query_json:
                                if isinstance(fallback_query_json, bytes):
                                    fallback_query_json = fallback_query_json.decode('utf-8')
                                fallback_query = fallback_query_json
                
                # Si encontramos una consulta similar para esta tabla
                if fallback_query and highest_sim > 0.7:
                    logger.info(f"Consulta similar encontrada para recuperación, similitud: {highest_sim:.4f}")
                    fallback_data = json.loads(fallback_query)
                    fallback_orm = fallback_data.get("orm_code")
                    
                    if fallback_orm:
                        logger.info(f"Usando ORM alternativo: {fallback_orm}")
                        # Ejecutar el ORM alternativo
                        results, total_count = safe_execute_orm(fallback_orm, db, query_request)
                        orm_code = fallback_orm  # Usar el ORM alternativo
                        source = "semantic_recovery"
                    else:
                        # Si no hay ORM alternativo, reenviar el error original
                        raise orm_error
                else:
                    # Si no hay consultas similares útiles, reenviar el error original
                    raise orm_error
            else:
                # Si no hay consultas previas para esta tabla, reenviar el error original
                raise orm_error
        
        # Valor por defecto para SQL ejecutado
        sql_executed = "-- SQL no disponible (generado desde ORM)"
        
        # Formatear respuesta
        processing_time = time.time() - start_time
        
        # Extraer tablas objetivo del código ORM
        target_tables = []
        for match in re.finditer(r"find_model\(['\"](.*?)['\"]\)", orm_code):
            target_tables.append(match.group(1))
        
        # Si no se encontraron tablas explícitamente, usar la tabla principal detectada
        if not target_tables:
            table_name = detect_main_table(orm_code, query_request.text, results)
            if table_name != "unknown":
                target_tables.append(table_name)
        
        # Si hay resultados y tenemos tablas objetivo, guardar la consulta exitosa
        if results and target_tables:
            # Guardar en caché semántica para futuras consultas
            query_id = semantic_cache.store_query(
                query_request.text,
                orm_code,
                sql_executed,
                target_tables
            )
            logger.info(f"Consulta exitosa almacenada con ID: {query_id}")
        
        return DynamicQueryResponse(
            results=results,
            orm_code=orm_code,
            processing_time=processing_time,
            total_results=total_count,
            message=f"Consulta ejecutada exitosamente (fuente: {source})"
        )
        
    except Exception as e:
        logger.error(f"Error en consulta dinámica pública: {str(e)}\n{traceback.format_exc()}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al procesar consulta: {str(e)}"
        )
            
def detect_main_table(orm_code: str, query_text: str, results: list) -> str:
    """
    Detecta la tabla principal involucrada en una consulta.
    
    Args:
        orm_code: Código ORM ejecutado
        query_text: Texto de la consulta original
        results: Resultados obtenidos
        
    Returns:
        Nombre de la tabla principal
    """
    # Método 1: Buscar en el código ORM
    if "find_model" in orm_code:
        matches = re.findall(r"find_model\(['\"]([^'\"]+)['\"]", orm_code)
        if matches:
            return matches[0]
    
    # Método 2: Buscar palabras clave en la consulta
    query_lower = query_text.lower()
    common_tables = {
        "banco": ["banco", "bancos"],
        "caja": ["caja", "cajas"],
        "factura": ["factura", "facturas"],
        "cliente": ["cliente", "clientes"],
        "producto": ["producto", "productos"]
    }
    
    for table, keywords in common_tables.items():
        if any(keyword in query_lower for keyword in keywords):
            return table
            
    # Método 3: Examinar claves en los resultados
    if results and isinstance(results[0], dict):
        # Tablas con columnas características
        key_columns = {
            "banco": ["nbanco", "banco"],
            "caja": ["ncaja", "caja"],
            "factura": ["nfactura", "factura"],
            "cliente": ["ncliente", "cliente", "nombre"]
        }
        
        result_keys = results[0].keys()
        for table, columns in key_columns.items():
            if any(col in result_keys for col in columns):
                return table
    
    # Valor por defecto
    return "unknown"
        
@router.get("/schema-status")
async def check_schema_status():
    """
    Verifica el estado del esquema en Redis.
    """
    try:
        # Obtener información del esquema
        from app.api.v1.routers.ai.schema_metadata_service import SchemaMetadataService
        schema_service = SchemaMetadataService()
        
        # Verificar si hay tablas en el esquema
        tables = schema_service.get_all_tables()
        
        return {
            "status": "active" if tables else "not_initialized",
            "tables_count": len(tables),
            "important_tables": len(schema_service.get_important_tables()) if tables else 0,
            "last_update": schema_service.redis_service.redis_client.get(schema_service.LAST_UPDATE_KEY)
        }
    except Exception as e:
        logger.error(f"Error verificando estado del esquema: {str(e)}")
        return {
            "status": "error",
            "error": str(e)
        }

@router.post("/refresh-schema")
async def refresh_schema(force: bool = False):
    """
    Actualiza el esquema de la base de datos en Redis.
    """
    try:
        from app.api.v1.routers.ai.schema_metadata_service import SchemaMetadataService
        schema_service = SchemaMetadataService()
        
        # Forzar actualización del esquema
        tables_count = schema_service.extract_and_store_schema(force_update=force)
        
        return {
            "status": "success",
            "message": f"Esquema actualizado. {tables_count} tablas procesadas.",
            "tables_count": tables_count
        }
    except Exception as e:
        logger.error(f"Error actualizando esquema: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al actualizar esquema: {str(e)}"
        )