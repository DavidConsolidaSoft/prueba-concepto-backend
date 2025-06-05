import os
import json
import redis
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

class RedisService:
    def __init__(self):
        redis_ssl = os.getenv("REDIS_SSL", "False").lower() == "true"
        self.redis_client = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=int(os.getenv("REDIS_PORT", 6380)),
            password=os.getenv("REDIS_PASSWORD"),
            ssl=redis_ssl,
            db=0,
            decode_responses=True  # Para obtener cadenas en lugar de bytes
        )
    
    def save_query_template(self, template_id: str, template_data: Dict[str, Any]) -> bool:
        """Guarda una plantilla de consulta en Redis."""
        try:
            self.redis_client.set(template_id, json.dumps(template_data))
            return True
        except Exception as e:
            print(f"Error al guardar plantilla en Redis: {str(e)}")
            return False
    
    def get_query_template(self, template_id: str) -> Optional[Dict[str, Any]]:
        """Obtiene una plantilla de consulta desde Redis."""
        try:
            data = self.redis_client.get(template_id)
            if data:
                return json.loads(data)
            return None
        except Exception as e:
            print(f"Error al obtener plantilla de Redis: {str(e)}")
            return None
    
    def get_all_templates(self) -> List[Dict[str, Any]]:
        """Obtiene todas las plantillas de consulta."""
        try:
            templates = []
            template_keys = self.redis_client.keys("template:*")
            
            for key in template_keys:
                template_data = self.get_query_template(key)
                if template_data:
                    template_data["id"] = key
                    templates.append(template_data)
            
            return templates
        except Exception as e:
            print(f"Error al obtener todas las plantillas: {str(e)}")
            return []