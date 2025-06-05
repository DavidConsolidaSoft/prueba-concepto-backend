# language_service.py
import os
import requests
from typing import Dict, Any

class LanguageService:
    def __init__(self):
        self.endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")
        self.key = os.getenv("AZURE_LANGUAGE_KEY")
        self.project_name = os.getenv("AZURE_LANGUAGE_PROJECT_NAME")
        self.deployment_name = os.getenv("AZURE_LANGUAGE_DEPLOYMENT_NAME")
    
    def analyze_query_intent(self, query_text: str) -> Dict[str, Any]:
        """Analiza la intención y entidades en una consulta usando Azure Language Understanding."""
        url = f"{self.endpoint}/language/:analyze-conversations?api-version=2022-10-01-preview"
        
        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/json"
        }
        
        body = {
            "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "id": "1",
                    "text": query_text,
                    "modality": "text",
                    "participantId": "user"
                }
            },
            "parameters": {
                "projectName": self.project_name,
                "deploymentName": self.deployment_name,
                "verbose": True
            }
        }
        
        try:
            response = requests.post(url, headers=headers, json=body)
            response.raise_for_status()
            result = response.json()
            
            # Procesar el resultado para extraer intención y entidades
            top_intent = result["result"]["prediction"]["topIntent"]
            entities = {}
            
            # Convertir la lista de entidades en un diccionario más fácil de usar
            for entity in result["result"]["prediction"]["entities"]:
                entity_type = entity["category"]
                entity_text = entity["text"]
                
                if entity_type in entities:
                    if isinstance(entities[entity_type], list):
                        entities[entity_type].append(entity_text)
                    else:
                        entities[entity_type] = [entities[entity_type], entity_text]
                else:
                    entities[entity_type] = entity_text
            
            intent_score = 0
            if result["result"]["prediction"]["intents"]:
                intent_score = result["result"]["prediction"]["intents"][0]["confidenceScore"]
                
            return {
                "intent": top_intent,
                "entities": entities,
                "confidence": intent_score,
                "query_text": query_text
            }
        except Exception as e:
            print(f"Error al analizar intención: {str(e)}")
            return {"intent": "None", "entities": {}, "confidence": 0, "query_text": query_text}