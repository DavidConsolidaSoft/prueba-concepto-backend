import json
import logging
import time
from typing import Dict, List, Tuple, Optional

import numpy as np
from app.api.v1.routers.ai.embedding_service import EmbeddingService
from app.api.v1.routers.ai.redis_service import RedisService
from app.api.v1.routers.ai.schema_metadata_service import SchemaMetadataService

logger = logging.getLogger(__name__)

class SemanticCache:
    """
    Servicio para cachear consultas semánticamente similares y sus resultados SQL/ORM.
    """
    
    def __init__(self):
        self.redis_service = RedisService()
        self.embedding_service = EmbeddingService()
        self.schema_service = SchemaMetadataService()
        
        # Prefijos para claves en Redis
        self.QUERY_CACHE_PREFIX = "semantic:query:"
        self.QUERY_EMBEDDING_PREFIX = "semantic:embedding:"
        self.QUERY_LIST_KEY = "semantic:all_queries"
        
        # Umbral de similitud para considerar una consulta como similar
        self.SIMILARITY_THRESHOLD = 0.85
    
    def find_similar_query(self, query_text: str) -> Optional[Dict]:
        """
        Busca una consulta semánticamente similar en la caché.
        
        Args:
            query_text: Texto de la consulta en lenguaje natural
            
        Returns:
            Diccionario con información de la consulta encontrada, o None si no hay similares
        """
        try:
            # Generar embedding para la consulta
            query_embedding = self.embedding_service.get_embedding(query_text)
            
            # Obtener todas las consultas cacheadas
            all_queries = self.redis_service.redis_client.smembers(self.QUERY_LIST_KEY)
            if not all_queries:
                return None
            
            # Calcular similitud con cada consulta
            best_match = None
            best_similarity = 0
            
            for query_id in all_queries:
                if isinstance(query_id, bytes):
                    query_id = query_id.decode('utf-8')
                
                # Obtener embedding de la consulta cacheada
                emb_key = f"{self.QUERY_EMBEDDING_PREFIX}{query_id}"
                cached_emb_json = self.redis_service.redis_client.get(emb_key)
                
                if not cached_emb_json:
                    continue
                
                if isinstance(cached_emb_json, bytes):
                    cached_emb_json = cached_emb_json.decode('utf-8')
                
                cached_embedding = json.loads(cached_emb_json)
                
                # Calcular similitud
                similarity = self.embedding_service.vector_similarity(query_embedding, cached_embedding)
                
                # Si supera el umbral y es mejor que el anterior mejor match
                if similarity > self.SIMILARITY_THRESHOLD and similarity > best_similarity:
                    # Obtener datos de la consulta
                    query_key = f"{self.QUERY_CACHE_PREFIX}{query_id}"
                    query_data_json = self.redis_service.redis_client.get(query_key)
                    
                    if query_data_json:
                        if isinstance(query_data_json, bytes):
                            query_data_json = query_data_json.decode('utf-8')
                        
                        query_data = json.loads(query_data_json)
                        best_match = query_data
                        best_similarity = similarity
            
            if best_match:
                logger.info(f"Consulta similar encontrada con similitud {best_similarity:.4f}")
                # Añadir la similitud al resultado para referencia
                best_match["similarity"] = best_similarity
            
            return best_match
            
        except Exception as e:
            logger.error(f"Error al buscar consulta similar: {str(e)}")
            return None
     
    def store_successful_query(self, query_text: str, orm_code: str, sql: str, results: list, table_name: str):
        """
        Almacena una consulta exitosa para aprendizaje futuro.
        
        Args:
            query_text: Texto de la consulta en lenguaje natural
            orm_code: Código ORM que funcionó correctamente
            sql: SQL generado/ejecutado
            results: Resultados obtenidos
            table_name: Nombre de la tabla principal involucrada
        """
        try:
            # Generar ID único
            query_id = f"{int(time.time())}_{hash(query_text) % 10000}"
            
            # Crear documento con la información
            query_data = {
                "id": query_id,
                "query_text": query_text,
                "orm_code": orm_code,
                "sql": sql,
                "table_name": table_name,
                "result_count": len(results),
                "sample_result": results[0] if results else {},
                "timestamp": time.time()
            }
            
            # Generar embedding
            query_embedding = self.embedding_service.get_embedding(query_text)
            
            # Guardar en Redis con pipeline
            pipeline = self.redis_service.redis_client.pipeline()
            
            # Guardar datos de la consulta
            query_key = f"{self.QUERY_CACHE_PREFIX}{query_id}"
            pipeline.set(query_key, json.dumps(query_data))
            
            # Guardar embedding
            emb_key = f"{self.QUERY_EMBEDDING_PREFIX}{query_id}"
            pipeline.set(emb_key, json.dumps(query_embedding))
            
            # Añadir a conjunto de todas las consultas
            pipeline.sadd(self.QUERY_LIST_KEY, query_id)
            
            # Añadir a conjunto específico de tabla
            table_queries_key = f"semantic:table_queries:{table_name}"
            pipeline.sadd(table_queries_key, query_id)
            
            # Ejecutar pipeline
            pipeline.execute()
            
            logger.info(f"Consulta exitosa almacenada para aprendizaje: {query_id} (tabla: {table_name})")
            return True
        except Exception as e:
            logger.error(f"Error almacenando consulta exitosa: {str(e)}")
            return False
        
    def store_query(self, query_text: str, orm_code: str, sql: str, target_tables: List[str]) -> str:
        """
        Almacena una consulta y su correspondiente código ORM/SQL para futuras referencias.
        
        Args:
            query_text: Texto de la consulta en lenguaje natural
            orm_code: Código ORM generado
            sql: SQL generado
            target_tables: Tablas objetivo de la consulta
            
        Returns:
            ID de la consulta almacenada
        """
        try:
            # Generar ID único para la consulta
            query_id = f"{int(time.time())}_{hash(query_text) % 10000}"
            
            # Crear documento con la información
            query_data = {
                "id": query_id,
                "query_text": query_text,
                "orm_code": orm_code,
                "sql": sql,
                "target_tables": target_tables,
                "timestamp": time.time()
            }
            
            # Generar y guardar embedding
            query_embedding = self.embedding_service.get_embedding(query_text)
            
            # Guardar en Redis
            pipeline = self.redis_service.redis_client.pipeline()
            
            # Guardar datos de la consulta
            query_key = f"{self.QUERY_CACHE_PREFIX}{query_id}"
            pipeline.set(query_key, json.dumps(query_data))
            
            # Guardar embedding
            emb_key = f"{self.QUERY_EMBEDDING_PREFIX}{query_id}"
            pipeline.set(emb_key, json.dumps(query_embedding))
            
            # Añadir a conjunto de todas las consultas
            pipeline.sadd(self.QUERY_LIST_KEY, query_id)
            
            # Ejecutar comandos
            pipeline.execute()
            
            logger.info(f"Consulta almacenada con ID {query_id}")
            return query_id
            
        except Exception as e:
            logger.error(f"Error almacenando consulta: {str(e)}")
            return ""

    def add_example_queries(self, force_update=False) -> int:
        """
        Añade consultas de ejemplo para las tablas principales.
        
        Returns:
            Número de consultas añadidas
        """
        try:
            # Verificar si ya existen ejemplos
            existing_queries = self.redis_service.redis_client.scard(self.QUERY_LIST_KEY)
            if existing_queries > 0:
                logger.info(f"Ya existen {existing_queries} consultas en la caché semántica")
                return 0
            
            # Si force_update es True, eliminar ejemplos existentes
            if force_update and existing_queries > 0:
                logger.info("Eliminando ejemplos existentes para forzar actualización")
                all_queries = self.redis_service.redis_client.smembers(self.QUERY_LIST_KEY)
                
                # Usar pipeline para mejor rendimiento
                pipeline = self.redis_service.redis_client.pipeline()
                
                # Eliminar cada consulta
                for query_id in all_queries:
                    if isinstance(query_id, bytes):
                        query_id = query_id.decode('utf-8')
                    
                    pipeline.delete(f"{self.QUERY_CACHE_PREFIX}{query_id}")
                    pipeline.delete(f"{self.QUERY_EMBEDDING_PREFIX}{query_id}")
                
                # Eliminar conjunto de consultas
                pipeline.delete(self.QUERY_LIST_KEY)
                
                # Ejecutar
                pipeline.execute()
            
            # Ejemplos para tabla 'caja'
            caja_examples = [
                {
                    "query": "Listar las 10 cajas más recientes",
                    "orm": "query = select(find_model('caja')).order_by(find_model('caja').horatiempo.desc()).limit(10)",
                    "sql": "SELECT TOP 10 * FROM caja ORDER BY horatiempo DESC",
                    "tables": ["caja"]
                },
                {
                    "query": "¿Cuál es la caja que más ingresos tiene?",
                    "orm": "query = select(find_model('caja')).order_by(find_model('caja').ingreso.desc()).limit(1)",
                    "sql": "SELECT TOP 1 * FROM caja ORDER BY ingreso DESC",
                    "tables": ["caja"]
                },
                {
                    "query": "Cajas activas actualmente",
                    "orm": "query = select(find_model('caja')).where(find_model('caja').activo == True).limit(20)",
                    "sql": "SELECT TOP 20 * FROM caja WHERE activo = 1",
                    "tables": ["caja"]
                },
                {
                    "query": "Mostrar las cajas con punto de venta",
                    "orm": "query = select(find_model('caja')).where(find_model('caja').puntoventa == True).limit(20)",
                    "sql": "SELECT TOP 20 * FROM caja WHERE puntoventa = 1",
                    "tables": ["caja"]
                },
                {
                    "query": "Mostrar cajas ordenadas por ingreso",
                    "orm": "query = select(find_model('caja')).order_by(find_model('caja').ingreso.desc()).limit(10)",
                    "sql": "SELECT TOP 10 * FROM caja ORDER BY ingreso DESC",
                    "tables": ["caja"]
                }
            ]
            
            banco_examples = [
                {
                    "query": "Dame los bancos",
                    "orm": "query = select(find_model('banco').banco, find_model('banco').nbanco).where(find_model('banco').activo == 1).limit(20)",
                    "sql": "SELECT TOP 20 banco, nbanco, preferido, activo FROM banco WHERE activo = 1",
                    "tables": ["banco"]
                },
                {
                    "query": "Lista de bancos",
                    "orm": "query = select(find_model('banco')).limit(20)",
                    "sql": "SELECT TOP 20 banco, nbanco, preferido, activo FROM banco",
                    "tables": ["banco"]
                },
                {
                    "query": "Mostrar todos los bancos",
                    "orm": "query = select(find_model('banco').banco, find_model('banco').nbanco, find_model('banco').preferido).limit(20)",
                    "sql": "SELECT TOP 20 banco, nbanco, preferido FROM banco",
                    "tables": ["banco"]
                }
            ]
            
            # Ejemplos para tabla 'factura'
            factura_examples = [
                {
                    "query": "Últimas 10 facturas",
                    "orm": "query = select(find_model('factura')).order_by(find_model('factura').fecha.desc()).limit(10)",
                    "sql": "SELECT TOP 10 * FROM factura ORDER BY fecha DESC",
                    "tables": ["factura"]
                },
                {
                    "query": "Facturas del cliente 123",
                    "orm": "query = select(find_model('factura')).where(find_model('factura').cliente == 123).limit(20)",
                    "sql": "SELECT TOP 20 * FROM factura WHERE cliente = 123",
                    "tables": ["factura"]
                }
            ]
            
            # Ejemplos para tabla 'cliente'
            cliente_examples = [
                {
                    "query": "Clientes activos",
                    "orm": "query = select(find_model('clientes')).where(find_model('clientes').activo == True).limit(20)",
                    "sql": "SELECT TOP 20 * FROM clientes WHERE activo = 1",
                    "tables": ["clientes"]
                },
                {
                    "query": "Clientes con mayor límite de crédito",
                    "orm": "query = select(find_model('clientes')).order_by(find_model('clientes').limite.desc()).limit(10)",
                    "sql": "SELECT TOP 10 * FROM clientes ORDER BY limite DESC",
                    "tables": ["clientes"]
                }
            ]
            
            # Unir todos los ejemplos
            all_examples = caja_examples + factura_examples + cliente_examples + banco_examples
            
            # Almacenar ejemplos
            added_count = 0
            for example in all_examples:
                self.store_query(
                    example["query"],
                    example["orm"],
                    example["sql"],
                    example["tables"]
                )
                added_count += 1
            
            logger.info(f"Se añadieron {added_count} consultas de ejemplo a la caché semántica")
            return added_count
            
        except Exception as e:
            logger.error(f"Error añadiendo ejemplos: {str(e)}")
            return 0