import json
import os
import logging
from openai import AzureOpenAI
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class ChatService:
    """
    Servicio para generar SQL y formatear respuestas usando Azure OpenAI.
    """
    
    def __init__(self):
        """Inicializa el servicio de chat."""
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_CHAT_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        self.chat_model = os.getenv("AZURE_OPENAI_CHAT_MODEL")
    
    def generate_sql(self, query_text: str, schema_metadata: Dict) -> str:
        """
        Genera una consulta SQL a partir de una pregunta en lenguaje natural.
        
        Args:
            query_text: Pregunta en lenguaje natural
            schema_metadata: Metadatos del esquema de la base de datos
            
        Returns:
            Consulta SQL generada
        """
        # Identificar tablas relevantes en lugar de enviar todo el esquema
        relevant_tables = self._identify_relevant_tables(query_text, schema_metadata)
        
        # Construir un esquema reducido
        reduced_schema = {"tables": {}}
        for table in relevant_tables:
            if table in schema_metadata.get("tables", {}):
                reduced_schema["tables"][table] = schema_metadata["tables"][table]
        
        # Agregar relaciones si existen
        if "relationships" in schema_metadata:
            reduced_schema["relationships"] = [
                r for r in schema_metadata.get("relationships", []) 
                if r.get("table") in relevant_tables or r.get("referenced_table") in relevant_tables
            ]
        
        # Serializar solo el esquema reducido
        reduced_schema_json = json.dumps(reduced_schema, indent=1, ensure_ascii=False)
        
        # Prompt más eficiente con mejores instrucciones
        prompt = f"""
        Pregunta: "{query_text}"
        
        Tablas disponibles: {', '.join(relevant_tables)}
        
        Esquema de la base de datos:
        {reduced_schema_json}
        
        INSTRUCCIONES IMPORTANTES:
        1. NO agregues filtros WHERE a menos que se especifiquen explícitamente en la pregunta
        2. Cuando se pida "listar" o "mostrar", devuelve TODAS las columnas principales
        3. Para tablas como 'banco', 'caja', 'cliente', NO filtres por 'activo' a menos que se pida
        4. NO uses la sintaxis de triple backtick (```) en tu respuesta
        5. Si la consulta es sobre bancos, usa "SELECT banco, nbanco, preferido, activo FROM banco"
        
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
            
            # Limpiar respuesta de backticks si los hay
            sql = response.choices[0].message.content.strip()
            sql = sql.replace("```sql", "").replace("```", "").strip()
            
            return sql
        except Exception as e:
            # Si hay error de rate limit, devolver mensaje específico
            if "429" in str(e):
                raise Exception("Rate limit alcanzado. Reintenta en 60 segundos.")
            raise e
        
    def _identify_relevant_tables(self, query_text: str, schema_metadata: Dict) -> List[str]:
        """
        Identifica tablas relevantes basadas en el texto de la consulta.
        
        Args:
            query_text: Consulta en lenguaje natural
            schema_metadata: Metadatos del esquema
            
        Returns:
            Lista de nombres de tablas relevantes
        """
        # Convertir consulta a minúsculas para comparación
        query_lower = query_text.lower()
        
        # Lista de palabras clave que pueden indicar tablas relevantes
        relevant_tables = []
        
        # Mapeo de términos comunes a tablas
        common_terms = {
            "banco": ["banco", "bancos", "bancario", "bancaria"],
            "caja": ["caja", "cajas", "tienda", "pos", "punto de venta"],
            "factura": ["factura", "facturas", "venta", "ventas", "compra", "transacción", "facturación"],
            "producto": ["producto", "productos", "artículo", "mercancía", "inventario"],
            "cliente": ["cliente", "clientes", "comprador", "persona", "usuario"],
            "vendedor": ["vendedor", "vendedores", "empleado", "staff", "personal"]
        }
        
        # Verificar menciones directas de tablas
        tables = schema_metadata.get("tables", {}).keys()
        for table_name in tables:
            # Verificar si el nombre de la tabla aparece en la consulta
            if table_name.lower() in query_lower:
                relevant_tables.append(table_name)
        
        # Si no se encontraron menciones directas, buscar por términos comunes
        if not relevant_tables:
            for table, terms in common_terms.items():
                if any(term in query_lower for term in terms):
                    # Verificar si la tabla existe en el esquema
                    if table in tables:
                        relevant_tables.append(table)
                    # Buscar tablas que comiencen con este término
                    for schema_table in tables:
                        if schema_table.lower().startswith(table):
                            relevant_tables.append(schema_table)
        
        # Si aún no hay tablas relevantes, incluir algunas principales
        if not relevant_tables:
            # Incluir las tablas más comunes si existen en el esquema
            default_tables = ["banco", "caja", "factura", "dfactura", "producto", "clientes"]
            relevant_tables = [t for t in default_tables if t in tables]
        
        return list(set(relevant_tables))  # Eliminar duplicados
    
    def format_response(self, query_text: str, results: List[Dict], total_results: int) -> str:
        """
        Genera una respuesta natural basada en los resultados de la consulta.
        
        Args:
            query_text: Consulta original en lenguaje natural
            results: Resultados de la consulta (muestra)
            total_results: Número total de resultados
            
        Returns:
            Respuesta en lenguaje natural
        """
        # Limitar resultados de muestra
        sample_size = min(3, len(results))
        results_sample = results[:sample_size]
        
        # Serializar solo los resultados de muestra
        results_json = json.dumps(results_sample, ensure_ascii=False)
        
        # Prompt optimizado
        prompt = f"""
        Pregunta: "{query_text}"
        
        Resultados ({sample_size} de {total_results}): {results_json}
        
        INSTRUCCIONES:
        1. Responde de forma natural y concisa a la pregunta
        2. Si los resultados están vacíos, no asumas que no existen datos, solo indica que no se encontraron resultados
        3. Si la consulta es sobre bancos, menciona específicamente los bancos encontrados
        
        Responde de forma natural y concisa.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.chat_model,
                messages=[
                    {"role": "system", "content": "Eres un asistente empresarial conciso y directo que responde preguntas sobre datos de manera natural."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=200
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            # Manejar error de rate limit
            if "429" in str(e):
                # Devolver una respuesta sencilla sin usar OpenAI
                if total_results > 0:
                    if "banco" in query_text.lower():
                        return f"Encontré {total_results} bancos en el sistema."
                    return f"Encontré {total_results} resultados para tu consulta."
                else:
                    return "No encontré resultados para tu consulta."
            
            logger.error(f"Error en format_response: {str(e)}")
            raise e
            
    def generate_orm_query(self, query_text: str) -> str:
        """
        Genera código SQLAlchemy ORM a partir de una consulta en lenguaje natural.
        Esta función es un puente para cuando el servicio no tiene acceso directo al ORMGenerator.
        
        Args:
            query_text: Consulta en lenguaje natural
            
        Returns:
            Código ORM generado
        """
        # Este método será sustituido por el método de ORMGenerator
        # cuando el servicio sea mejorado con SchemaEnhancedChatService
        
        prompt = f"""
        Genera código SQLAlchemy ORM para esta consulta: "{query_text}"
        
        INSTRUCCIONES:
        1. Incluye "from app.db.base import models" en la primera línea
        2. Usa select() (sintaxis SQLAlchemy 2.0) en lugar de query (sintaxis 1.x)
        3. Para consultas de listado, incluye .limit(10)
        4. Si la consulta menciona "reciente", ordena por fecha o ID en orden descendente
        5. Usa siempre models.NombreTabla para referenciar los modelos
        6. Asegúrate de que el resultado final se guarde en una variable llamada "query"
        
        Devuelve solo el código, sin explicaciones.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.chat_model,
                messages=[
                    {"role": "system", "content": "Eres un experto en SQLAlchemy ORM que genera código Python conciso y funcional."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=500
            )
            
            # Limpiar el código generado
            code = response.choices[0].message.content.strip()
            
            # Eliminar backticks si están presentes
            if code.startswith("```python"):
                code = code.replace("```python", "", 1)
            if code.endswith("```"):
                code = code[:-3]
                
            return code.strip()
            
        except Exception as e:
            logger.error(f"Error generando ORM: {str(e)}")
            
            # Código de fallback básico
            return """
            from app.db.base import models
            
            # Consulta básica de fallback
            query = select(models.caja)
            query = query.limit(10)
            """