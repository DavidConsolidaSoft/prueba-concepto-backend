"""
MCP Tools Simple - Solo acceso seguro a BD, sin queries predefinidas
La IA generará las consultas dinámicamente
"""
import logging
from typing import Dict, Any, List, Optional
from functools import wraps
from mcp.server.fastmcp import FastMCP

# Importar tu infraestructura existente
from app.api.v1.routers.auth.jwt_handler import verify_token
from app.db.database import get_db
from app.models.all_models import Usuario as User

logger = logging.getLogger(__name__)

# Crear servidor MCP simple
consolida_mcp = FastMCP("Consolida ERP Simple DB Access", stateless_http=True)

# ===== VALIDACIÓN DE USUARIO =====

async def validate_jwt_and_get_user_info(jwt_token: str) -> Optional[Dict[str, Any]]:
    """Valida JWT y obtiene información del usuario"""
    try:
        payload = verify_token(jwt_token)
        email = payload.get("sub")
        user_id = payload.get("user_id")
        
        if not email:
            return None
        
        # Usar tu dependency de base de datos
        async for db in get_db():
            try:
                if user_id and user_id > 0:
                    user = db.query(User).filter(User.usuario == user_id).first()
                else:
                    user = db.query(User).filter(
                        (User.email == email) | (User.correo == email)
                    ).first()
                
                if not user or not user.activo or not user.empresa:
                    return None
                
                return {
                    "user_id": user.usuario,
                    "email": user.email or user.correo,
                    "nombre": user.nusuario,
                    "empresa": user.empresa,
                    "activo": user.activo
                }
                
            except Exception as e:
                logger.error(f"Error consultando usuario: {e}")
                return None
            finally:
                break
        
        return None
        
    except Exception as e:
        logger.error(f"Error validando JWT: {e}")
        return None

def require_valid_jwt(func):
    """Decorator que valida JWT"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        jwt_token = kwargs.get('jwt_token')
        
        if not jwt_token:
            raise ValueError("Token JWT requerido")
        
        user_info = await validate_jwt_and_get_user_info(jwt_token)
        
        if not user_info:
            raise PermissionError("Token inválido o usuario no autorizado")
        
        # Pasar info del usuario (SIN guión bajo)
        kwargs['user_info'] = user_info
        
        return await func(*args, **kwargs)
    
    return wrapper

# ===== FUNCIÓN DE BASE DE DATOS =====

async def execute_query_with_db(query: str, params: List = None) -> List[Dict[str, Any]]:
    """Ejecuta query usando tu sistema de BD"""
    async for db in get_db():
        try:
            if hasattr(db, 'sync_session'):
                # Tu AsyncSessionEmulator para MSSQL
                cursor = db.sync_session.execute(query, params or [])
                columns = [desc[0] for desc in cursor.description] if cursor.description else []
                rows = cursor.fetchall()
                
                result = []
                for row in rows:
                    result.append(dict(zip(columns, row)))
                
                return result
            else:
                # Para otras BD con soporte async
                result = await db.execute(query, params or [])
                rows = result.fetchall()
                return [dict(row) for row in rows]
                
        except Exception as e:
            logger.error(f"Error ejecutando query: {e}")
            raise
        finally:
            break
    
    return []

# ===== HERRAMIENTAS MCP SIMPLES =====

@consolida_mcp.tool()
@require_valid_jwt
async def get_my_empresa_info(jwt_token: str, user_info: Dict = None) -> Dict[str, Any]:
    """
    Obtiene información de MI empresa
    
    Args:
        jwt_token: Token JWT del usuario
        
    Returns:
        Información de la empresa del usuario
    """
    try:
        empresa_id = user_info['empresa']
        
        query = """
        SELECT empresa, nempresa, direccion, telefono1, telefono2, 
               email, giro, activo, nit, dui
        FROM dbo.empresa 
        WHERE empresa = ? AND activo = 1
        """
        
        result = await execute_query_with_db(query, [empresa_id])
        
        if not result:
            raise ValueError(f"Empresa {empresa_id} no encontrada")
        
        empresa_data = result[0]
        empresa_data["usuario_autorizado"] = user_info['email']
        
        return empresa_data
        
    except Exception as e:
        logger.error(f"Error getting empresa info: {e}")
        raise

@consolida_mcp.tool()
@require_valid_jwt
async def execute_safe_query(
    jwt_token: str, 
    query: str, 
    user_info: Dict = None
) -> List[Dict[str, Any]]:
    """
    Ejecuta una consulta SQL segura filtrada automáticamente por MI empresa.
    
    IMPORTANTE: La consulta debe incluir WHERE empresa = ? y será filtrada automáticamente.
    
    Args:
        jwt_token: Token JWT del usuario
        query: Consulta SQL (debe incluir WHERE empresa = ?)
        
    Returns:
        Resultados filtrados por mi empresa
    """
    try:
        empresa_id = user_info['empresa']
        
        # Validaciones de seguridad
        query_upper = query.upper().strip()
        
        # Solo permitir SELECT
        if not query_upper.startswith("SELECT"):
            raise ValueError("Solo se permiten consultas SELECT")
        
        # Prevenir patrones peligrosos
        dangerous_patterns = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "CREATE", "EXEC", "--", "/*"]
        for pattern in dangerous_patterns:
            if pattern in query_upper:
                raise ValueError(f"Patrón no permitido: {pattern}")
        
        # Debe incluir filtro por empresa
        if "WHERE EMPRESA = ?" not in query_upper:
            raise ValueError("La consulta debe incluir 'WHERE empresa = ?' para seguridad")
        
        # Ejecutar query con empresa_id como primer parámetro
        result = await execute_query_with_db(query, [empresa_id])
        
        logger.info(f"Query ejecutada para empresa {empresa_id}: {len(result)} resultados")
        return result
        
    except Exception as e:
        logger.error(f"Error executing safe query: {e}")
        raise

@consolida_mcp.tool()
@require_valid_jwt
async def get_table_schema(jwt_token: str, table_name: str, user_info: Dict = None) -> List[Dict[str, Any]]:
    """
    Obtiene el esquema de una tabla (columnas, tipos, etc.)
    
    Args:
        jwt_token: Token JWT del usuario
        table_name: Nombre de la tabla
        
    Returns:
        Esquema de la tabla
    """
    try:
        # Lista blanca de tablas permitidas
        allowed_tables = [
            "empresa", "productos", "clientes", "facturas", "inventario", 
            "pedidos", "proveedores", "compras", "movimientos"
        ]
        
        if table_name not in allowed_tables:
            raise ValueError(f"Tabla '{table_name}' no permitida. Permitidas: {allowed_tables}")
        
        query = """
        SELECT 
            COLUMN_NAME as column_name,
            DATA_TYPE as data_type,
            IS_NULLABLE as is_nullable,
            COLUMN_DEFAULT as default_value,
            CHARACTER_MAXIMUM_LENGTH as max_length
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = ? AND TABLE_SCHEMA = 'dbo'
        ORDER BY ORDINAL_POSITION
        """
        
        result = await execute_query_with_db(query, [table_name])
        
        logger.info(f"Schema obtenido para tabla {table_name}: {len(result)} columnas")
        return result
        
    except Exception as e:
        logger.error(f"Error getting table schema: {e}")
        raise

@consolida_mcp.tool()
async def test_database_connection() -> Dict[str, Any]:
    """
    Prueba la conexión a la base de datos (sin autenticación)
    
    Returns:
        Estado de la conexión
    """
    try:
        result = await execute_query_with_db("SELECT GETDATE() as fecha_servidor")
        
        if result:
            return {
                "status": "success",
                "message": "Conexión a base de datos exitosa",
                "fecha_servidor": str(result[0]["fecha_servidor"]),
                "database_type": "SQL Server (Azure)"
            }
        else:
            return {
                "status": "error",
                "message": "No se pudo obtener respuesta de la base de datos"
            }
        
    except Exception as e:
        logger.error(f"Database test failed: {e}")
        return {
            "status": "error",
            "message": f"Error de conexión: {str(e)}"
        }

# Función para obtener el servidor MCP
def get_consolida_mcp_server():
    """Retorna la instancia del servidor MCP"""
    return consolida_mcp