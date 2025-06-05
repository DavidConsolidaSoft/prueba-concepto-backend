import os
import json
import time
import datetime
import logging
import numpy as np
from typing import List, Dict, Any, Optional, Set
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, MetaData, Table, text
from app.api.v1.routers.ai.embedding_service import EmbeddingService
from app.api.v1.routers.ai.redis_service import RedisService
from app.core.config import settings

logger = logging.getLogger(__name__)

load_dotenv()

class SchemaMetadataService:
    """
    Servicio para gestionar los metadatos del esquema de la base de datos.
    Proporciona funcionalidades para extraer, almacenar, buscar y mantener
    la documentación del esquema directamente en Redis.
    """
    def __init__(self):
        # Inicializar servicios
        self.redis_service = RedisService()
        self.embedding_service = EmbeddingService()
        
        # Configuración de la base de datos
        self.db_config = {
            "driver": os.getenv("DB_DRIVER"),
            "server": os.getenv("DB_SERVER"),
            "database": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD")
        }
        
        # Prefijos para claves de Redis
        self.TABLE_KEY_PREFIX = "schema:table:"
        self.EMBEDDING_KEY_PREFIX = "schema:embedding:"
        self.ALL_TABLES_KEY = "schema:all_tables"
        self.IMPORTANT_TABLES_KEY = "schema:important_tables"
        self.LAST_UPDATE_KEY = "schema:last_update"
        
        # Flag para control de actualización
        self._last_version_check = 0
        self._cache_timeout = 3600  # 1 hora entre comprobaciones
    
    def extract_and_store_schema(self, force_update: bool = False) -> int:
        """
        Extrae y almacena metadatos del esquema de base de datos en Redis.
        
        Args:
            force_update: Si es True, fuerza la actualización incluso si ya existe
            
        Returns:
            Número de tablas procesadas
        """
        try:
            # Clave para la metadata del esquema en Redis
            SCHEMA_METADATA_KEY = "db_schema_metadata"
            
            # Si no se fuerza actualización, intentar usar datos de Redis
            if not force_update:
                schema_data_json = self.redis_service.redis_client.get(SCHEMA_METADATA_KEY)
                if schema_data_json:
                    # Asegurarse de decodificar si es necesario
                    if isinstance(schema_data_json, bytes):
                        schema_data_json = schema_data_json.decode('utf-8')
                        
                    schema_data = json.loads(schema_data_json)
                    if schema_data and "tables" in schema_data and len(schema_data["tables"]) > 0:
                        logger.info(f"Usando metadata de esquema desde Redis: {len(schema_data['tables'])} tablas")
                        
                        # Procesar y guardar en formato adecuado para el servicio
                        pipeline = self.redis_service.redis_client.pipeline()
                        
                        # Limpiar claves anteriores
                        pipeline.delete(self.ALL_TABLES_KEY)
                        
                        # Preparar lista de tablas
                        table_names = list(schema_data["tables"].keys())
                        if table_names:
                            pipeline.sadd(self.ALL_TABLES_KEY, *table_names)
                            
                        # Procesar cada tabla
                        for table_name, table_data in schema_data["tables"].items():
                            # Convertir al formato que espera este servicio
                            formatted_data = {
                                "nombre_tabla": table_name,
                                "proposito": f"Tabla: {table_name}",
                                "columnas": []
                            }
                            
                            # Convertir columnas al formato esperado
                            for column in table_data.get("columns", []):
                                col_info = {
                                    "name": column["name"],
                                    "type": column["type"],
                                    "description": f"Columna {column['name']}",
                                    "is_key": False  # Por defecto, sin información de clave primaria
                                }
                                formatted_data["columnas"].append(col_info)
                            
                            # Guardar tabla formateada
                            table_key = f"{self.TABLE_KEY_PREFIX}{table_name}"
                            pipeline.set(table_key, json.dumps(formatted_data))
                            
                            # Generar embedding
                            table_text = self._create_table_document(formatted_data)
                            embedding = self.embedding_service.get_embedding(table_text)
                            pipeline.set(f"{self.EMBEDDING_KEY_PREFIX}{table_name}", json.dumps(embedding))
                        
                        pipeline.set(self.LAST_UPDATE_KEY, str(time.time()))
                        pipeline.execute()
                        
                        logger.info(f"Metadata de esquema procesada desde Redis")
                        return len(schema_data["tables"])
            
            # Si llegamos aquí, necesitamos extraer el esquema de la base de datos
            logger.info("Extrayendo esquema directamente de la base de datos...")
            
            # Crear conexión a la base de datos usando SQLAlchemy
            engine = create_engine(settings.DATABASE_URI)
            inspector = inspect(engine)
            
            # Obtener lista de tablas
            tables = []
            for schema in inspector.get_schema_names():
                # Usar el esquema 'dbo' para SQL Server o el esquema predeterminado
                if schema in ['dbo', 'public', '']:
                    for table_name in inspector.get_table_names(schema=schema):
                        tables.append(table_name)
            
            logger.info(f"Se encontraron {len(tables)} tablas en la base de datos")
            
            # Iniciar pipeline de Redis
            pipeline = self.redis_service.redis_client.pipeline()
            
            # Limpiar claves existentes
            pipeline.delete(self.ALL_TABLES_KEY)
            
            # Añadir todas las tablas al conjunto
            if tables:
                pipeline.sadd(self.ALL_TABLES_KEY, *tables)
            
            # Procesar cada tabla
            for table_name in tables:
                try:
                    # Separar esquema y nombre de tabla
                    if '.' in table_name:
                        schema, pure_table_name = table_name.split('.', 1)
                    else:
                        schema = 'dbo'  # Esquema por defecto para SQL Server
                        pure_table_name = table_name
                    
                    # Obtener información de la tabla
                    try:
                        table_info = self._reflect_table(pure_table_name, inspector, schema)
                        
                        # Guardar en Redis usando solo el nombre puro (sin esquema)
                        table_key = f"{self.TABLE_KEY_PREFIX}{pure_table_name}"
                        pipeline.set(table_key, json.dumps(table_info))
                        
                        # Generar y guardar embedding
                        table_text = self._create_table_document(table_info)
                        embedding = self.embedding_service.get_embedding(table_text)
                        pipeline.set(f"{self.EMBEDDING_KEY_PREFIX}{pure_table_name}", json.dumps(embedding))
                    except Exception as inner_e:
                        logger.error(f"Error procesando tabla {table_name}: {str(inner_e)}")
                except Exception as e:
                    logger.error(f"Error procesando tabla {table_name}: {str(e)}")
            
            # Actualizar timestamp
            pipeline.set(self.LAST_UPDATE_KEY, str(time.time()))
            
            # Ejecutar todas las operaciones
            pipeline.execute()
            
            # Actualizar metadatos generales
            schema_metadata = {
                "tables": {},
                "last_update": time.time(),
                "total_tables": len(tables)
            }
            
            # Simplificar para el metadata general
            for table_name in tables:
                schema_metadata["tables"][table_name] = {"processed": True}
            
            # Guardar metadata completa
            self.redis_service.redis_client.set(SCHEMA_METADATA_KEY, json.dumps(schema_metadata))
            
            logger.info(f"Esquema extraído y almacenado correctamente: {len(tables)} tablas")
            return len(tables)
            
        except Exception as e:
            logger.error(f"Error en extracción de esquema: {str(e)}")
            return 0
    
    def _reflect_table(self, table_name: str, inspector, schema: str = 'dbo') -> Dict[str, Any]:
        """
        Refleja los metadatos de una tabla desde la base de datos.
        
        Args:
            table_name: Nombre de la tabla
            inspector: Inspector de SQLAlchemy
            schema: Esquema de la base de datos (por defecto: 'dbo')
            
        Returns:
            Diccionario con los metadatos de la tabla
        """
        # Obtener columnas
        columns = []
        try:
            primary_keys = inspector.get_pk_constraint(table_name, schema=schema).get('constrained_columns', [])
            
            for col in inspector.get_columns(table_name, schema=schema):
                columns.append({
                    "name": col['name'],
                    "type": str(col['type']),
                    "description": f"Columna {col['name']}",
                    "is_key": col['name'] in primary_keys
                })
            
            # Obtener relaciones si existen
            relationships = self._get_reflected_relationships(table_name, inspector, schema)
            
            # Crear documento de tabla
            return {
                "nombre_tabla": table_name,
                "proposito": f"Tabla que almacena datos de {table_name}",
                "columnas": columns,
                "relaciones": relationships
            }
        except Exception as e:
            logger.warning(f"Error obteniendo detalles para {table_name}: {str(e)}")
            # Devolver información básica en caso de error
            return {
                "nombre_tabla": table_name,
                "proposito": f"Tabla {table_name}",
                "columnas": [],
                "relaciones": []
            }
        
    def _get_reflected_relationships(self, table_name: str, inspector, schema: str = 'dbo') -> List[Dict[str, Any]]:
        """
        Obtiene las relaciones de una tabla desde la base de datos.
        
        Args:
            table_name: Nombre de la tabla
            inspector: Inspector de SQLAlchemy
            schema: Esquema de la base de datos (por defecto: 'dbo')
            
        Returns:
            Lista de relaciones
        """
        relationships = []
        try:
            # Obtener foreign keys
            fks = inspector.get_foreign_keys(table_name, schema=schema)
            
            for fk in fks:
                if 'constrained_columns' in fk and 'referred_table' in fk:
                    rel = {
                        "tipo_relacion": "foreign_key",
                        "tabla_relacionada": fk['referred_table'],
                        "columna_local": fk['constrained_columns'][0] if fk['constrained_columns'] else "",
                        "columna_externa": fk['referred_columns'][0] if 'referred_columns' in fk and fk['referred_columns'] else ""
                    }
                    relationships.append(rel)
        except Exception as e:
            logger.warning(f"Error obteniendo relaciones para {table_name}: {str(e)}")
        
        return relationships
    
    def find_relevant_tables(self, query_text: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Encuentra tablas relevantes para una consulta usando embeddings.
        
        Args:
            query_text: Texto de la consulta
            top_k: Número máximo de tablas a devolver
            
        Returns:
            Lista de diccionarios con información de las tablas relevantes
        """
        try:
            # Generar embedding para la consulta
            query_embedding = self.embedding_service.get_embedding(query_text)
            
            # Obtener todas las tablas
            all_tables = self.get_all_tables()
            if not all_tables:
                logger.warning("No hay tablas disponibles para búsqueda")
                return []
            
            # Calcular similitudes
            tables_with_similarity = []
            
            for table_name in all_tables:
                # Decodificar a string si es necesario
                if isinstance(table_name, bytes):
                    table_name = table_name.decode('utf-8')
                
                # Obtener embedding
                embedding_key = f"{self.EMBEDDING_KEY_PREFIX}{table_name}"
                embedding_json = self.redis_service.redis_client.get(embedding_key)
                
                if embedding_json:
                    # Decodificar si es necesario
                    if isinstance(embedding_json, bytes):
                        embedding_json = embedding_json.decode('utf-8')
                        
                    table_embedding = json.loads(embedding_json)
                    
                    # Calcular similitud
                    similarity = self.embedding_service.vector_similarity(
                        query_embedding,
                        table_embedding
                    )
                    
                    # Obtener metadatos de la tabla
                    table_data = self.get_table_schema(table_name)
                    
                    if table_data:
                        tables_with_similarity.append({
                            "nombre_tabla": table_name,
                            "proposito": table_data.get("proposito", f"Tabla {table_name}"),
                            "columnas": table_data.get("columnas", []),
                            "similarity": similarity
                        })
            
            # Ordenar por similitud descendente y limitar resultados
            relevant_tables = sorted(
                tables_with_similarity, 
                key=lambda x: x["similarity"], 
                reverse=True
            )[:top_k]
            
            return relevant_tables
            
        except Exception as e:
            logger.error(f"Error buscando tablas relevantes: {str(e)}")
            return []
    
    def update_table_metadata(self, table_name: str, purpose: str = None, 
                            column_descriptions: List[Dict] = None, 
                            is_important: bool = None) -> bool:
        """
        Actualiza la documentación de una tabla específica.
        
        Args:
            table_name: Nombre de la tabla a actualizar
            purpose: Nuevo propósito/descripción de la tabla (opcional)
            column_descriptions: Lista de descripciones de columnas (opcional)
            is_important: Marcar si la tabla es importante (opcional)
            
        Returns:
            True si la actualización fue exitosa
        """
        try:
            # Verificar si la tabla existe
            table_key = f"{self.TABLE_KEY_PREFIX}{table_name}"
            table_data_json = self.redis_service.redis_client.get(table_key)
            
            if not table_data_json:
                logger.error(f"La tabla '{table_name}' no existe en el esquema.")
                return False
            
            # Decodificar si es necesario
            if isinstance(table_data_json, bytes):
                table_data_json = table_data_json.decode('utf-8')
                
            # Obtener datos actuales
            table_data = json.loads(table_data_json)
            
            # Actualizar propósito si se proporcionó
            if purpose:
                table_data["proposito"] = purpose
            
            # Actualizar descripciones de columnas si se proporcionaron
            if column_descriptions:
                columns_dict = {col["name"]: col for col in table_data.get("columnas", [])}
                
                for new_col in column_descriptions:
                    if new_col["name"] in columns_dict:
                        # Actualizar descripción de la columna existente
                        for col in table_data["columnas"]:
                            if col["name"] == new_col["name"]:
                                col["description"] = new_col.get("description", col.get("description", ""))
                                break
            
            # Actualizar tabla en Redis
            self.redis_service.redis_client.set(table_key, json.dumps(table_data))
            
            # Actualizar embedding
            table_text = self._create_table_document(table_data)
            embedding = self.embedding_service.get_embedding(table_text)
            self.redis_service.redis_client.set(
                f"{self.EMBEDDING_KEY_PREFIX}{table_name}", 
                json.dumps(embedding)
            )
            
            # Actualizar estado de "importante" si se proporcionó
            if is_important is not None:
                if is_important:
                    self.redis_service.redis_client.sadd(self.IMPORTANT_TABLES_KEY, table_name)
                else:
                    self.redis_service.redis_client.srem(self.IMPORTANT_TABLES_KEY, table_name)
            
            logger.info(f"Metadatos de la tabla '{table_name}' actualizados correctamente.")
            return True
            
        except Exception as e:
            logger.error(f"Error al actualizar metadatos de tabla: {str(e)}")
            return False
    
    def get_table_schema(self, table_name: str) -> Optional[Dict[str, Any]]:
        """
        Obtiene la documentación completa de una tabla.
        
        Args:
            table_name: Nombre de la tabla
            
        Returns:
            Diccionario con los metadatos de la tabla o None si no existe
        """
        try:
            table_key = f"{self.TABLE_KEY_PREFIX}{table_name}"
            table_data_json = self.redis_service.redis_client.get(table_key)
            
            if table_data_json:
                # Decodificar si es necesario
                if isinstance(table_data_json, bytes):
                    table_data_json = table_data_json.decode('utf-8')
                    
                return json.loads(table_data_json)
            
            return None
            
        except Exception as e:
            logger.error(f"Error al obtener esquema de tabla: {str(e)}")
            return None
    
    def get_all_tables(self) -> List[str]:
        """
        Obtiene la lista de todas las tablas documentadas.
        
        Returns:
            Lista con los nombres de todas las tablas
        """
        try:
            tables = self.redis_service.redis_client.smembers(self.ALL_TABLES_KEY)
            return list(tables)
        except Exception as e:
            logger.error(f"Error al obtener lista de tablas: {str(e)}")
            return []
    
    def get_important_tables(self) -> List[str]:
        """
        Obtiene la lista de tablas marcadas como importantes.
        
        Returns:
            Lista con los nombres de las tablas importantes
        """
        try:
            tables = self.redis_service.redis_client.smembers(self.IMPORTANT_TABLES_KEY)
            return list(tables)
        except Exception as e:
            logger.error(f"Error al obtener tablas importantes: {str(e)}")
            return []
    
    def mark_table_as_important(self, table_name: str) -> bool:
        """
        Marca una tabla como importante.
        
        Args:
            table_name: Nombre de la tabla
            
        Returns:
            True si la operación fue exitosa
        """
        try:
            # Verificar que la tabla existe
            if not self.redis_service.redis_client.exists(f"{self.TABLE_KEY_PREFIX}{table_name}"):
                return False
            
            # Añadir a conjunto de tablas importantes
            self.redis_service.redis_client.sadd(self.IMPORTANT_TABLES_KEY, table_name)
            return True
            
        except Exception as e:
            logger.error(f"Error al marcar tabla como importante: {str(e)}")
            return False
    
    def generate_schema_context(self, query_text: str, max_tables: int = 5) -> str:
        """
        Genera un contexto de esquema para incluir en prompts al modelo de lenguaje.
        
        Args:
            query_text: Texto de la consulta
            max_tables: Número máximo de tablas a incluir
            
        Returns:
            Texto con el contexto del esquema relevante
        """
        try:
            # Encontrar tablas relevantes
            relevant_tables = self.find_relevant_tables(query_text, top_k=max_tables)
            
            if not relevant_tables:
                return "No se encontró información de esquema relevante para esta consulta."
            
            # Generar contexto
            context = "INFORMACIÓN DEL ESQUEMA DE LA BASE DE DATOS:\n\n"
            
            for table_data in relevant_tables:
                # Añadir información de la tabla
                context += f"TABLA: {table_data['nombre_tabla']}\n"
                context += f"PROPÓSITO: {table_data['proposito']}\n"
                
                # Añadir columnas
                context += "COLUMNAS:\n"
                for column in table_data['columnas']:
                    context += f"- {column['name']} ({column['type']}): {column.get('description', 'Sin descripción')}\n"
                
                # Añadir relaciones si existen
                if table_data.get('relaciones'):
                    context += "\nRELACIONES:\n"
                    for rel in table_data['relaciones']:
                        context += f"- {rel['tipo_relacion']} con {rel['tabla_relacionada']} "
                        context += f"a través de {rel['columna_local']} -> {rel['columna_externa']}\n"
                
                context += "\n"
            
            return context
            
        except Exception as e:
            logger.error(f"Error al generar contexto de esquema: {str(e)}")
            return "Error al generar contexto de esquema."
    
    def get_schema_for_query(self, query_text: str) -> Dict:
        """
        Obtiene un esquema optimizado para la consulta usando embeddings.
        
        Args:
            query_text: Texto de la consulta
            
        Returns:
            Esquema optimizado para la consulta
        """
        # Generar embedding de la consulta
        query_embedding = self.embedding_service.get_embedding(query_text)
        
        # Buscar tablas similares
        similar_tables = []
        all_tables = self.get_all_tables()
        
        for table_name in all_tables:
            # Decodificar a string si es necesario
            if isinstance(table_name, bytes):
                table_name = table_name.decode('utf-8')
                
            emb_key = f"{self.EMBEDDING_KEY_PREFIX}{table_name}"
            table_emb_json = self.redis_service.redis_client.get(emb_key)
            
            if table_emb_json:
                try:
                    # Decodificar si es necesario
                    if isinstance(table_emb_json, bytes):
                        table_emb_json = table_emb_json.decode('utf-8')
                        
                    table_emb = json.loads(table_emb_json)
                    similarity = self.embedding_service.vector_similarity(
                        query_embedding, 
                        table_emb
                    )
                    if similarity > 0.6:  # Umbral de similitud
                        similar_tables.append((table_name, similarity))
                except Exception as e:
                    logger.warning(f"Error procesando embedding para {table_name}: {str(e)}")
        
        # Ordenar por similitud y limitar a las más relevantes
        similar_tables.sort(key=lambda x: x[1], reverse=True)
        top_tables = [t[0] for t in similar_tables[:5]]
        
        # Construir esquema reducido
        optimized_schema = {"tables": {}}
        for table_name in top_tables:
            table_data = self.get_table_schema(table_name)
            if table_data:
                # Incluir solo información relevante
                optimized_schema["tables"][table_name] = {
                    "columns": [
                        {"name": col["name"], "type": col["type"], "description": col.get("description", "")}
                        for col in table_data.get("columnas", [])
                    ]
                }
        
        return optimized_schema
    
    def refresh_schema(self) -> int:
        """
        Actualiza la reflexión del esquema solo si ha cambiado.
        
        Returns:
            Número de tablas procesadas
        """
        try:
            # Verificar si ha pasado suficiente tiempo desde la última comprobación
            current_time = time.time()
            if (current_time - self._last_version_check) < self._cache_timeout:
                logger.info("Comprobación de esquema reciente, saltando verificación")
                return 0
                
            self._last_version_check = current_time
            
            # Verificar versión actual del esquema en Redis
            current_version = self.redis_service.redis_client.get("schema_version")
            if isinstance(current_version, bytes):
                current_version = current_version.decode('utf-8')
            
            # Obtener nueva versión usando SQLAlchemy
            engine = create_engine(settings.DATABASE_URI)
            
            # Usar una consulta simple que no requiera reflexión completa
            with engine.connect() as conn:
                # Comprobar solo si el número de tablas ha cambiado
                result = conn.execute(text("""
                    SELECT COUNT(*) as table_count
                    FROM sys.tables 
                    WHERE is_ms_shipped = 0
                """))
                table_count = result.fetchone()[0]
                
                # Comprobar si alguna tabla ha sido modificada recientemente
                result = conn.execute(text("""
                    SELECT MAX(modify_date) as last_modified
                    FROM sys.tables 
                    WHERE is_ms_shipped = 0
                """))
                last_modified = result.fetchone()[0]
                
                # Crear una versión simplificada basada solo en el recuento de tablas y la última modificación
                # Esto es menos propenso a cambios innecesarios que el enfoque anterior
                new_version = f"{table_count}_{last_modified}"
            
            # Registrar versiones para diagnóstico
            logger.info(f"Versiones de esquema - Actual: {current_version}, Nueva: {new_version}")
            
            # Si cambió, forzar actualización
            if current_version != new_version:
                logger.info(f"Esquema cambió, actualizando ({current_version} -> {new_version})")
                tables_count = self.extract_and_store_schema(force_update=True)
                self.redis_service.redis_client.set("schema_version", new_version)
                return tables_count
            else:
                logger.info("Esquema sin cambios, no se requiere actualización")
                return 0
                
        except Exception as e:
            logger.error(f"Error al refrescar esquema: {str(e)}")
            return 0
    
    def _create_table_document(self, table_data: Dict[str, Any]) -> str:
        """
        Crea un documento de texto para la tabla que se usará para generar embeddings.
        
        Args:
            table_data: Datos de la tabla
            
        Returns:
            Texto que representa la tabla
        """
        doc = f"Tabla {table_data['nombre_tabla']}: {table_data.get('proposito', '')}\n"
        doc += "Columnas:\n"
        
        for col in table_data.get('columnas', []):
            # Obtener datos de la columna
            col_name = col.get('name', '')
            col_type = col.get('type', '')
            col_desc = col.get('description', f"Columna {col_name}")
            is_key = col.get('is_key', False)
            
            # Añadir información sobre clave primaria
            key_info = " (Clave primaria)" if is_key else ""
            
            doc += f"- {col_name} ({col_type}){key_info}: {col_desc}\n"
        
        # Añadir relaciones si existen
        if 'relaciones' in table_data and table_data['relaciones']:
            doc += "\nRelaciones:\n"
            for rel in table_data['relaciones']:
                doc += f"→ Relacionada con {rel['tabla_relacionada']} "
                doc += f"via {rel['columna_local']} -> {rel['columna_externa']}\n"
        
        return doc