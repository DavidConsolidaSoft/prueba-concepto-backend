import os
import json
import logging
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from app.api.v1.routers.ai.schema_metadata_service import SchemaMetadataService
from app.api.v1.routers.ai.orm_generator import ORMGenerator

load_dotenv()
logger = logging.getLogger(__name__)

class SchemaEnhancedChatService:
    """
    Servicio de chat mejorado que utiliza metadatos de esquema para mejorar el procesamiento de consultas.
    """
    
    def __init__(self, original_chat_service):
        """
        Inicializa con una instancia existente de servicio de chat.
        """
        self.original_service = original_chat_service
        self.schema_service = SchemaMetadataService()
        self.orm_generator = ORMGenerator()
        
        # Copiar atributos del servicio original
        self.client = original_chat_service.client
        self.chat_model = original_chat_service.chat_model
    
    def generate_orm_query(self, query_text: str) -> str:
        """
        Genera código SQLAlchemy ORM para una consulta en lenguaje natural.
        """
        return self.orm_generator.generate_orm_query(query_text)
    
    def generate_sql(self, query_text: str, schema_metadata: Dict = None) -> str:
        """
        Versión mejorada que utiliza contexto de esquema relevante.
        """
        # Si no se proporcionaron metadatos, obtener esquema relevante
        if not schema_metadata:
            schema_metadata = self.schema_service.get_schema_for_query(query_text)
        
        # Obtener contexto de esquema como texto
        schema_context = self.schema_service.generate_schema_context(query_text)
        
        # Mejorar prompt con contexto de esquema
        prompt = f"""
        Pregunta: "{query_text}"
        
        {schema_context}
        
        INSTRUCCIONES IMPORTANTES:
        1. NO agregues filtros WHERE a menos que se especifiquen explícitamente en la pregunta
        2. Cuando se pida "listar" o "mostrar", devuelve las columnas principales de la tabla
        3. Para tablas como 'banco', 'caja', 'cliente', NO filtres por 'activo' a menos que se pida
        4. NO uses la sintaxis de triple backtick (```) en tu respuesta
        5. Si la consulta es sobre bancos, usa "SELECT banco, nbanco, preferido, activo FROM banco"
        6. Utiliza solo las tablas y columnas mencionadas en el esquema proporcionado
        
        Genera una consulta SQL válida para SQL Server. Solo SQL, sin explicaciones.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.chat_model,
                messages=[
                    {"role": "system", "content": "Eres un experto en SQL que genera consultas precisas y seguras para SQL Server."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=500
            )
            
            # Limpiar respuesta de backticks si están presentes
            sql = response.choices[0].message.content.strip()
            sql = sql.replace("```sql", "").replace("```", "").strip()
            
            return sql
        except Exception as e:
            # Manejar errores de rate limit
            if "429" in str(e):
                raise Exception("Rate limit alcanzado. Reintenta en 60 segundos.")
            raise e
    
    def format_response(self, query_text: str, results: List[Dict], total_results: int) -> str:
        """
        Proxy al método original.
        """
        return self.original_service.format_response(query_text, results, total_results)


def enhance_query_processor(query_processor):
    """
    Mejora un QueryProcessor existente con funcionalidad de esquema.
    """
    try:
        logger.info("Iniciando mejora del procesador de consultas con datos de esquema...")
        
        # Crear instancia de servicio de esquema
        schema_service = SchemaMetadataService()
        
        # Verificar si el esquema ya existe en Redis
        tables = schema_service.get_all_tables()
        if not tables:
            logger.info("No se encontró esquema en Redis. Extrayendo esquema inicial...")
            schema_service.extract_and_store_schema(force_update=True)
            tables = schema_service.get_all_tables()
            logger.info(f"Esquema extraído. {len(tables)} tablas disponibles.")
        else:
            logger.info(f"Esquema encontrado en Redis con {len(tables)} tablas.")
        
        # Mejorar el ChatService
        original_chat_service = query_processor.chat_service
        enhanced_chat_service = SchemaEnhancedChatService(original_chat_service)
        query_processor.chat_service = enhanced_chat_service
        
        # Reemplazar método para identificar tablas relevantes
        def enhanced_identify_tables(self, query_text: str, schema_metadata: Dict) -> List[str]:
            """Método mejorado que usa embeddings para identificar tablas relevantes."""
            relevant_tables = schema_service.find_relevant_tables(query_text)
            return [table['nombre_tabla'] for table in relevant_tables]
        
        # Reemplazar método original
        query_processor._identify_relevant_tables = enhanced_identify_tables.__get__(query_processor, type(query_processor))
        
        # Añadir servicio de esquema como atributo
        query_processor.schema_service = schema_service
        
        # Añadir método para obtener esquema optimizado
        def get_optimized_schema(self, query_text: str) -> Dict:
            """Obtiene un esquema optimizado con solo las tablas relevantes para la consulta."""
            return self.schema_service.get_schema_for_query(query_text)
        
        query_processor.get_optimized_schema = get_optimized_schema.__get__(query_processor, type(query_processor))
        
        # Modificar método principal de procesamiento de consultas para usar el esquema optimizado
        original_process_query = query_processor._process_query_multicapa
        
        def enhanced_process_query(self, query_text: str) -> Dict[str, Any]:
            """Versión mejorada que usa el esquema optimizado."""
            # Optimización: usar el servicio de esquema para generar un esquema reducido
            try:
                # Esto mejora la generación SQL al reducir el tamaño del esquema
                optimized_schema = self.get_optimized_schema(query_text)
                
                # Modificar la capa de generación dinámica para usar el esquema optimizado
                def process_with_enhanced_schema(original_method):
                    # Guardar el esquema original
                    original_schema = getattr(self, 'schema_metadata', {})
                    
                    # Usar el esquema optimizado temporalmente
                    self.schema_metadata = optimized_schema
                    
                    # Ejecutar el método original
                    result = original_method(query_text)
                    
                    # Restaurar el esquema original
                    self.schema_metadata = original_schema
                    
                    # Añadir información sobre las tablas utilizadas
                    if "sql_executed" in result:
                        # Encontrar tablas relevantes utilizadas
                        relevant_tables = [table['nombre_tabla'] for table in self.schema_service.find_relevant_tables(query_text)]
                        
                        # Añadir contexto de esquema a la respuesta
                        result["schema_context"] = {
                            "relevant_tables": relevant_tables,
                            "tables_used": len(relevant_tables)
                        }
                    
                    return result
                
                # Ejecutar el método original con el esquema optimizado
                result = process_with_enhanced_schema(original_process_query.__get__(self, type(self)))
                
                return result
                
            except Exception as e:
                logger.error(f"Error en procesamiento mejorado: {str(e)}")
                # Si hay error, usar el método original como fallback
                return original_process_query(self, query_text)
        
        # Reemplazar el método de procesamiento
        query_processor._process_query_multicapa = enhanced_process_query.__get__(query_processor, type(query_processor))
        
        logger.info("QueryProcessor mejorado con funcionalidades de esquema.")
        
        # Analizar tablas disponibles
        schema_info = {}
        try:
            important_tables = schema_service.get_important_tables()
            all_tables = schema_service.get_all_tables()
            
            schema_info = {
                "total_tables": len(all_tables),
                "important_tables": len(important_tables),
                "tables_sample": list(all_tables)[:5] if all_tables else []
            }
            
            logger.info(f"Schema: {schema_info['total_tables']} tablas, {schema_info['important_tables']} importantes")
        except Exception as e:
            logger.error(f"Error analizando tablas: {str(e)}")
            
        return query_processor
        
    except Exception as e:
        logger.error(f"Error al mejorar query processor: {str(e)}")
        # Devolver el procesador original si falla
        return query_processor