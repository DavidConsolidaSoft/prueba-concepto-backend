import datetime
import hashlib
import re
import json
import time
import random
import logging
from typing import List, Dict, Any, Tuple, Optional
import pyodbc
import os
from dotenv import load_dotenv
from app.api.v1.routers.ai.embedding_service import EmbeddingService
from app.api.v1.routers.ai.redis_service import RedisService
from app.api.v1.routers.ai.chat_service import ChatService

load_dotenv()
logger = logging.getLogger(__name__)

class QueryProcessor:
    def __init__(self):
        """Inicializa el procesador de consultas."""
        self.embedding_service = EmbeddingService()
        self.redis_service = RedisService()
        self.chat_service = ChatService()
        
        # Configuración de la base de datos
        self.db_config = {
            "driver": os.getenv("DB_DRIVER"),
            "server": os.getenv("DB_SERVER"),
            "database": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD")
        }
        
        # Cargar o crear metadatos del esquema
        self._load_or_create_schema_metadata()
    
    def _load_or_create_schema_metadata(self):
        """Carga o crea metadatos del esquema de la base de datos."""
        schema_data = self.redis_service.redis_client.get("db_schema")
        
        if schema_data:
            try:
                self.schema_metadata = json.loads(schema_data)
                logger.info(f"Esquema cargado de Redis: {len(self.schema_metadata.get('tables', {}))} tablas")
            except json.JSONDecodeError:
                logger.error("Error al decodificar esquema de Redis. Generando nuevo esquema.")
                self.schema_metadata = self._extract_schema_metadata_relationships()
                self.redis_service.redis_client.set("db_schema", json.dumps(self.schema_metadata))
        else:
            logger.info("Esquema no encontrado en Redis. Generando nuevo esquema.")
            self.schema_metadata = self._extract_schema_metadata_relationships()
            # Guardar en Redis para futuras consultas
            self.redis_service.redis_client.set("db_schema", json.dumps(self.schema_metadata))
    
    def _extract_schema_metadata_relationships(self):
        """Extrae metadatos básicos del esquema (versión simplificada)."""
        metadata = {"tables": {}, "relationships": []}
        
        try:
            conn_str = f'DRIVER={{{self.db_config["driver"]}}};SERVER={self.db_config["server"]};DATABASE={self.db_config["database"]};UID={self.db_config["user"]};PWD={self.db_config["password"]}'
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            
            # Obtener tablas principales (limitado a 100 para evitar sobrecarga)
            cursor.execute("""
                SELECT TOP 100 TABLE_NAME 
                FROM INFORMATION_SCHEMA.TABLES 
                WHERE TABLE_TYPE = 'BASE TABLE'
            """)
            tables = [row[0] for row in cursor.fetchall()]
            
            for table in tables:
                # Obtener columnas básicas
                cursor.execute(f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'")
                columns = {row[0]: {"type": row[1]} for row in cursor.fetchall()}
                
                # Obtener relaciones (versión simplificada)
                cursor.execute(f"""
                    SELECT 
                        OBJECT_NAME(f.parent_object_id) AS TableName,
                        COL_NAME(fc.parent_object_id, fc.parent_column_id) AS ColumnName,
                        OBJECT_NAME(f.referenced_object_id) AS ReferenceTableName,
                        COL_NAME(fc.referenced_object_id, fc.referenced_column_id) AS ReferenceColumnName
                    FROM 
                        sys.foreign_keys AS f
                        INNER JOIN sys.foreign_key_columns AS fc ON f.OBJECT_ID = fc.constraint_object_id
                    WHERE 
                        OBJECT_NAME(f.parent_object_id) = '{table}'
                """)
                
                relationships = []
                for row in cursor.fetchall():
                    relationships.append({
                        "referenced_table": row.ReferenceTableName,
                        "local_column": row.ColumnName,
                        "referenced_column": row.ReferenceColumnName
                    })
                
                # Construir metadata simple
                metadata["tables"][table] = {
                    "columns": columns,
                    "relationships": relationships,
                    "sample_data": []
                }
            
            cursor.close()
            conn.close()
            
            logger.info(f"Esquema extraído: {len(metadata['tables'])} tablas")
            
        except Exception as e:
            logger.error(f"Error al extraer metadatos básicos: {str(e)}")
        
        return metadata
    
    def _identify_relevant_tables(self, query_text: str, schema_metadata: Dict) -> List[str]:
        """
        Identifica tablas relevantes basadas en el texto (será reemplazado 
        por la versión mejorada en schema_integration.py).
        """
        query_lower = query_text.lower()
        relevant_tables = []
        
        # Buscar tablas mencionadas explícitamente
        tables = schema_metadata.get("tables", {}).keys()
        for table in tables:
            if table.lower() in query_lower:
                relevant_tables.append(table)
        
        # Si no se encontraron tablas, incluir algunas comunes
        if not relevant_tables:
            default_tables = ["banco", "caja", "factura", "producto", "cliente"]
            for default_table in default_tables:
                if default_table in tables:
                    relevant_tables.append(default_table)
        
        return relevant_tables
    
    def execute_sql_query(self, sql: str) -> List[Dict[str, Any]]:
        """Ejecuta una consulta SQL con caché."""
        # Generar clave de caché
        cache_key = f"sql_cache:{hashlib.md5(sql.encode()).hexdigest()}"
        
        # Verificar caché
        cached_result = self.redis_service.redis_client.get(cache_key)
        if cached_result:
            try:
                return json.loads(cached_result)
            except json.JSONDecodeError:
                logger.warning("Error al decodificar caché SQL. Ejecutando consulta de nuevo.")
        
        try:
            # Crear conexión
            conn_str = f'DRIVER={{{self.db_config["driver"]}}};SERVER={self.db_config["server"]};DATABASE={self.db_config["database"]};UID={self.db_config["user"]};PWD={self.db_config["password"]}'
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            
            # Ejecutar consulta
            cursor.execute(sql)
            
            # Procesar resultados
            if cursor.description is None:
                results = []
            else:
                columns = [column[0] for column in cursor.description]
                results = []
                
                for row in cursor.fetchall():
                    row_dict = {}
                    for i, value in enumerate(row):
                        if isinstance(value, (datetime.datetime, datetime.date)):
                            row_dict[columns[i]] = value.isoformat()
                        else:
                            row_dict[columns[i]] = value
                    results.append(row_dict)
            
            cursor.close()
            conn.close()
            
            # Guardar en caché (TTL 15 minutos)
            self.redis_service.redis_client.setex(cache_key, 900, json.dumps(results))
            
            return results
        except Exception as e:
            logger.error(f"Error al ejecutar SQL: {str(e)}")
            return []
    
    def process_query_with_retry(self, query_text: str, max_retries=3) -> Dict[str, Any]:
        """Procesa consultas con reintentos en caso de errores."""
        for attempt in range(max_retries):
            try:
                return self._process_query_multicapa(query_text)
            except Exception as e:
                error_str = str(e)
                if "429" in error_str and attempt < max_retries - 1:
                    # Rate limit - esperar antes del siguiente intento
                    wait_time = (2 ** attempt) + random.uniform(0, 1)
                    logger.info(f"Rate limit alcanzado. Reintentando en {wait_time:.2f} segundos...")
                    time.sleep(wait_time)
                else:
                    # Error final o último intento
                    logger.error(f"Error procesando consulta: {str(e)}")
                    return {
                        "error": f"No se pudo procesar tu consulta: {str(e)}",
                        "results": [],
                        "processing_time": 0
                    }
        
        return {
            "error": "No se pudo procesar tu consulta después de varios intentos.",
            "results": [],
            "processing_time": 0
        }

    def _process_query_multicapa(self, query_text: str) -> Dict[str, Any]:
        """
        Procesa consultas en un enfoque multicapa.
        Este método será potenciado por la versión mejorada en schema_integration.py.
        """
        start_time = time.time()
        
        # CAPA 1: Caché de respuestas exactas
        query_hash = hashlib.md5(query_text.encode()).hexdigest()
        cache_key = f"response_cache:{query_hash}"
        
        cached_response = self.redis_service.redis_client.get(cache_key)
        if cached_response:
            try:
                return json.loads(cached_response)
            except json.JSONDecodeError:
                logger.warning("Error al decodificar caché de respuesta. Continuando con procesamiento.")
        
        # CAPA 2: Detección de patrones simples
        simple_query_type = self.is_simple_query(query_text)
        if simple_query_type:
            if simple_query_type == "cajas":
                sql = "SELECT caja, ncaja FROM caja ORDER BY ncaja"
            elif simple_query_type == "bancos":
                sql = "SELECT banco, nbanco, preferido, activo FROM banco"
            else:
                sql = None
                
            if sql:
                results = self.execute_sql_query(sql)
                
                response = {
                    "answer": f"Aquí tienes la lista de {len(results)} {simple_query_type}.",
                    "results": results,
                    "template_used": f"Consulta simple: {simple_query_type}",
                    "confidence": 0.9,
                    "sql_executed": sql,
                    "processing_time": time.time() - start_time
                }
                
                # Guardar en caché
                self.redis_service.redis_client.setex(cache_key, 3600, json.dumps(response))
                return response
        
        # CAPA 3: Generación SQL con OpenAI
        try:
            # Encontrar tablas relevantes
            relevant_tables = self._identify_relevant_tables(query_text, self.schema_metadata)
            
            # Crear esquema reducido
            reduced_schema = {"tables": {}}
            for table in relevant_tables:
                if table in self.schema_metadata["tables"]:
                    reduced_schema["tables"][table] = self.schema_metadata["tables"][table]
            
            # Generar SQL
            sql = self.chat_service.generate_sql(query_text, reduced_schema)
            
            # Ejecutar consulta
            results = self.execute_sql_query(sql)
            
            # Generar respuesta natural
            answer = self.chat_service.format_response(query_text, results[:10], len(results))
            
            # Preparar respuesta final
            response = {
                "answer": answer,
                "results": results,
                "template_used": "Generación dinámica",
                "confidence": 0.8,
                "sql_executed": sql,
                "processing_time": time.time() - start_time
            }
            
            # Guardar en caché
            self.redis_service.redis_client.setex(cache_key, 3600, json.dumps(response))
            
            return response
            
        except Exception as e:
            logger.error(f"Error en generación dinámica: {str(e)}")
            return {
                "error": f"No se pudo procesar tu consulta: {str(e)}",
                "results": [],
                "processing_time": time.time() - start_time
            }
    
    def is_simple_query(self, query_text: str) -> Optional[str]:
        """Detecta si es una consulta simple y conocida."""
        query_lower = query_text.lower()
        
        # Patrones para cajas
        if re.search(r"(?:dame|muestra|lista)(?:\s+(?:todas|los|las))?\s+(?:las\s+)?cajas", query_lower):
            return "cajas"
        
        # Patrones para bancos
        if re.search(r"(?:dame|muestra|lista)(?:\s+(?:todas|los|las))?\s+(?:los\s+)?bancos", query_lower):
            return "bancos"
        
        return None
    
    def analyze_and_precalculate_queries(self):
        """Analiza consultas lentas y programa precálculos."""
        try:
            logger.info("Analizando consultas para precálculo...")
            
            # Obtener consultas lentas (si están disponibles)
            slow_queries = self.redis_service.redis_client.hgetall("slow_queries") or {}
            
            if slow_queries:
                logger.info(f"Se encontraron {len(slow_queries)} consultas lentas para analizar")
                
                # Aquí iría la lógica de precálculo
                for query_hash, query_data in slow_queries.items():
                    try:
                        query_info = json.loads(query_data)
                        query_text = query_info.get("text", "")
                        execution_time = query_info.get("time", 0)
                        
                        # Si es una consulta lenta, precalcular y guardar en caché
                        if execution_time > 1.0 and query_text:  # Solo consultas que toman más de 1 segundo
                            logger.info(f"Precalculando consulta lenta: {query_text}")
                            self.process_query_with_retry(query_text)
                    except Exception as e:
                        logger.error(f"Error al procesar consulta lenta: {str(e)}")
            else:
                logger.info("No se encontraron consultas lentas para analizar")
                
            return True
            
        except Exception as e:
            logger.error(f"Error en análisis de consultas: {str(e)}")
            return False