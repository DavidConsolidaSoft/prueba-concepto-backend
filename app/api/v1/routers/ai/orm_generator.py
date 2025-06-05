import os
import logging
import json
import re
from typing import List, Dict, Any, Optional
from openai import AzureOpenAI
from dotenv import load_dotenv
from app.api.v1.routers.ai.schema_metadata_service import SchemaMetadataService

load_dotenv()
logger = logging.getLogger(__name__)

class ORMGenerator:
    """
    Servicio para generar código SQLAlchemy ORM a partir de consultas en lenguaje natural
    utilizando metadatos de esquema y OpenAI.
    """
    
    def __init__(self):
        """Inicializa el servicio generador de ORM."""
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_CHAT_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        self.chat_model = os.getenv("AZURE_OPENAI_CHAT_MODEL")
        self.schema_service = SchemaMetadataService()
        
    def generate_orm_query(self, query_text: str) -> str:
        """
        Genera código ORM optimizado usando embeddings y contexto de esquema.
        
        Args:
            query_text: Consulta en lenguaje natural
            
        Returns:
            Código SQLAlchemy ORM generado
        """
        try:
            # Obtener tablas relevantes usando embeddings
            relevant_tables = self.schema_service.find_relevant_tables(query_text, top_k=3)
            
            # Construir contexto de esquema específico
            schema_context = []
            
            for table_info in relevant_tables:
                table_name = table_info['nombre_tabla']
                table_data = self.schema_service.get_table_schema(table_name)
                
                if table_data:
                    columns_info = []
                    for col in table_data.get('columnas', []):
                        column_type = col.get('type', 'Unknown')
                        is_key = col.get('is_key', False)
                        columns_info.append(f"- {col['name']} ({column_type}){'*' if is_key else ''}")
                    
                    schema_context.append(
                        f"Tabla {table_name}:\n" + 
                        f"Propósito: {table_data.get('proposito', 'No especificado')}\n" +
                        "Columnas:\n" + "\n".join(columns_info)
                    )
            
            schema_context_str = "\n\n".join(schema_context)
            
            # Detectar tipo de consulta para dar instrucciones específicas
            query_type = self._detect_query_intent(query_text)
            specific_instructions = self._get_specialized_instructions(query_type)
            
            # Detectar filtros en la consulta
            filters = self._detect_filter_intent(query_text)
            
            # Añadir instrucciones específicas para los filtros
            filter_instructions = ""
            if filters:
                filter_instructions = "Filtros detectados en la consulta:\n"
                for filter_type, filter_value in filters.items():
                    filter_instructions += f"- {filter_type}: {filter_value}\n"
            
            # Armar el prompt completo
            prompt = f"""
            Genera código SQLAlchemy ORM para la siguiente consulta: "{query_text}"
            
            {filter_instructions}

            Esquema de tablas relevantes:
            {schema_context_str}

            Instrucciones generales:
            1. NO incluyas instrucciones import o from ... import en tu respuesta
            2. MUY IMPORTANTE: Usa find_model('nombre_tabla') en lugar de models['nombre_tabla'] siempre
            3. Ejemplo: query = select(find_model('caja')).limit(10)
            4. NO uses models.Caja, models['caja'] o cualquier referencia directa a models
            5. Define las consultas usando la sintaxis de SQLAlchemy 2.0 con select()
            6. Ejemplos de consulta correctos:
            - query = select(find_model('caja')).limit(10)
            - query = select(find_model('factura')).where(find_model('factura').fecha > fecha_inicio)
            7. Usa aliasing explícito para joins complejos
            8. Aplica límites razonables para cualquier consulta (10-20 filas por defecto)
            9. Para fechas o numeración, ordena de forma descendente a menos que se especifique lo contrario
            10. Nombra la variable final como "query" para que pueda ser ejecutada directamente

            {specific_instructions}

            Por favor genera SOLO código Python, sin explicaciones adicionales.
            """
            # Realizar llamada a la API
            response = self.client.chat.completions.create(
                model=self.chat_model,
                messages=[
                    {"role": "system", "content": "Eres un experto en SQLAlchemy ORM que genera código preciso y eficiente."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=800
            )
            
            # Extraer y limpiar el código generado
            generated_code = response.choices[0].message.content.strip()
            
            # Eliminar backticks si existen
            if generated_code.startswith("```python"):
                generated_code = generated_code.replace("```python", "", 1)
            
            if generated_code.endswith("```"):
                generated_code = generated_code[:-3]
                
            # Quitar las líneas de importación
            clean_lines = []
            for line in generated_code.strip().split('\n'):
                # Omitir líneas que comienzan con 'import' o 'from'
                if not line.strip().startswith(('import ', 'from ')):
                    clean_lines.append(line)
            
            # Si eliminamos todas las líneas (poco probable), devolvemos un código básico
            if not clean_lines:
                return "query = select(find_model('caja')).limit(10) if find_model('caja') else select(find_model('banco')).limit(10)"
                
            # Asegurarse de que se usa find_model en lugar de acceso directo a models
            processed_code = '\n'.join(clean_lines).strip()
            
            # Reemplazar cualquier acceso directo a models por find_model
            processed_code = re.sub(
                r"models\['([^']+)'\]", 
                r"find_model('\1')", 
                processed_code
            )
            
            processed_code = re.sub(
                r'models\["([^"]+)"\]', 
                r'find_model("\1")', 
                processed_code
            )
            
            processed_code = re.sub(
                r"models\.([a-zA-Z0-9_]+)", 
                r"find_model('\1')", 
                processed_code
            )
            
            # Agregar una verificación de seguridad para el modelo 'caja'
            if 'caja' in processed_code.lower():
                if "find_model('caja')" not in processed_code and 'find_model("caja")' not in processed_code:
                    # Reemplazar manualmente las referencias a 'caja'
                    processed_code = processed_code.replace("models['caja']", "find_model('caja')")
                    processed_code = processed_code.replace('models["caja"]', 'find_model("caja")')
                    processed_code = processed_code.replace("models.caja", "find_model('caja')")
                    processed_code = processed_code.replace("models.Caja", "find_model('caja')")
            
            logger.info(f"Código ORM generado: {processed_code}")
            return processed_code
            
        except Exception as e:
            logger.error(f"Error al generar código ORM: {str(e)}")
            # Código de fallback básico que usa find_model
            return """
            # Consulta generada en modo de respaldo
            # Error original: {str(e)}
            query = select(find_model('caja')).limit(10) if find_model('caja') else select(find_model('banco')).limit(10)
            """

    # Añadir en orm_generator.py o mejorar la función existente
    def _detect_filter_intent(self, query_text: str) -> Dict[str, Any]:
        """Detecta intenciones de filtrado en el texto de la consulta."""
        query_lower = query_text.lower()
        filters = {}
        
        # Detectar filtros por nombre
        name_patterns = [
            r"con\s+nombre\s+([a-zA-Z0-9\s]+)",
            r"llamado\s+([a-zA-Z0-9\s]+)",
            r"que\s+se\s+llama\s+([a-zA-Z0-9\s]+)",
            r"con\s+el\s+nombre\s+([a-zA-Z0-9\s]+)"
        ]
        
        for pattern in name_patterns:
            matches = re.finditer(pattern, query_lower)
            for match in matches:
                # Extraer el nombre mencionado
                name = match.group(1).strip()
                if name:
                    filters["name"] = name
                    break
        
        # Detectar filtros por ID
        id_patterns = [
            r"con\s+id\s+(\d+)",
            r"con\s+código\s+(\d+)",
            r"número\s+(\d+)"
        ]
        
        for pattern in id_patterns:
            matches = re.finditer(pattern, query_lower)
            for match in matches:
                filters["id"] = int(match.group(1))
                break
        
        return filters

    def _detect_query_intent(self, query_text: str) -> str:
        """
        Detecta la intención de la consulta para proporcionar instrucciones más especializadas.
        
        Args:
            query_text: La consulta en lenguaje natural
            
        Returns:
            Categoría de intención de consulta
        """
        query_lower = query_text.lower()
        
        # Verificar diferentes tipos de consulta
        if any(word in query_lower for word in ["reciente", "últim", "ultim", "nuevo", "nueva"]):
            return "recent_records"
        
        if any(word in query_lower for word in ["count", "cuántos", "cuantos", "total", "cantidad"]):
            return "aggregation"
            
        if any(word in query_lower for word in ["top", "mejor", "peor", "ranking", "más", "mas"]):
            return "ranking"
            
        if any(word in query_lower for word in ["por fecha", "rango", "entre", "periodo"]):
            return "date_range"
            
        if any(word in query_lower for word in ["agrupar", "group", "promedio", "average", "suma", "sum"]):
            return "grouping"
            
        if any(word in query_lower for word in ["join", "relaciona", "combina"]):
            return "joining"
            
        # Caso por defecto
        return "listing"
    
    def _get_specialized_instructions(self, query_intent: str) -> str:
        """
        Obtiene instrucciones especializadas basadas en la intención de la consulta.
        
        Args:
            query_intent: La intención de consulta detectada
            
        Returns:
            Instrucciones especializadas para el tipo de consulta
        """
        instructions = {
            "recent_records": """
            Para esta consulta de registros recientes:
            - Usa ORDER BY con DESC en columnas de fecha o ID
            - Incluye solo columnas necesarias en la sentencia select
            - Aplica un límite razonable (p. ej., query = query.limit(10))
            - IMPORTANTE: Usa find_model en lugar de models (Ejemplo: select(find_model('caja')))
            """,
            
            "aggregation": """
            Para esta consulta de conteo/agregación:
            - Usa func.count() para contar registros
            - Para otras agregaciones, usa métodos func apropiados (sum, avg, etc.)
            - Agrupa correctamente si se requiere contar por categorías
            - IMPORTANTE: Usa find_model en lugar de models (Ejemplo: select(func.count(find_model('caja').id)))
            """,
            
            "ranking": """
            Para esta consulta de ranking/top-N:
            - Usa ORDER BY con dirección apropiada (DESC para "top", ASC para "bottom")
            - Aplica un límite apropiado según el número solicitado
            - Para rankings complejos, considera usar func.row_number() o func.rank()
            - IMPORTANTE: Usa find_model en lugar de models
            """,
            
            "date_range": """
            Para esta consulta de rango de fechas:
            - Usa between o operadores de comparación (>=, <=) para rangos de fechas
            - Para fechas relativas, usa texto como "hoy", "ayer", "mes pasado", etc.
            - IMPORTANTE: Usa find_model en lugar de models
            """,
            
            "grouping": """
            Para esta consulta de agrupación/agregación:
            - Usa func.sum(), func.avg(), etc. para agregar valores
            - Incluye cláusula group_by con columnas apropiadas
            - Ordena los resultados por los valores agregados (normalmente descendente)
            - IMPORTANTE: Usa find_model en lugar de models
            """,
            
            "joining": """
            Para esta consulta que requiere joins:
            - Usa joins explícitos con condiciones claras
            - Selecciona solo las columnas necesarias de cada tabla para evitar ambigüedades
            - Usa aliases descriptivos para las tablas cuando sea necesario
            - IMPORTANTE: Usa find_model en lugar de models para cada tabla
            """,
            
            "listing": """
            Para esta consulta de listado:
            - Selecciona solo las columnas necesarias para optimizar el rendimiento
            - Aplica filtros apropiados en la cláusula where si se especifican criterios
            - Usa limit para evitar conjuntos de resultados demasiado grandes
            - IMPORTANTE: Usa find_model en lugar de models. Ejemplo:
              query = select(find_model('caja')).limit(10)
            """
        }
        
        return instructions.get(query_intent, instructions["listing"])