import os
from dotenv import load_dotenv
from embedding_service import EmbeddingService
from redis_service import RedisService 

# Cargar variables de entorno
load_dotenv()

def initialize_cajas_template():
    """Inicializa la plantilla para consulta de cajas."""
    embedding_service = EmbeddingService()
    redis_service = RedisService()
    
    # Definir preguntas de ejemplo para la consulta de cajas
    example_questions = [
        "Dame la lista de cajas",
        "Muestra todas las cajas",
        "¿Qué cajas están disponibles?",
        "Lista de cajas ordenadas",
        "Ver cajas del sistema"
    ]
    
    # Crear embedding para la primera pregunta ejemplo
    query_embedding = embedding_service.get_embedding(example_questions[0])
    
    # Definir la plantilla de consulta
    template_data = {
        "description": "Obtener lista de cajas disponibles",
        "example_questions": example_questions,
        "embedding": query_embedding,
        "sql_template": "SELECT caja, ncaja FROM caja ORDER BY ncaja",
        "param_extractors": [],
        "table": "caja",
        "created_from": "manual_init",
        "usage_count": 0,
        "success_count": 0,
        "success_rate": 0
    }
    
    # Guardar en Redis
    template_id = "template:caja_list"
    success = redis_service.save_query_template(template_id, template_data)
    
    if success:
        print(f"Plantilla '{template_id}' creada correctamente")
    else:
        print(f"Error al crear la plantilla '{template_id}'")

if __name__ == "__main__":
    initialize_cajas_template()