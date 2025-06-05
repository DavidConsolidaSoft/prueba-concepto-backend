import asyncio
import os
from typing import List, Dict, Any
from openai import OpenAI, AzureOpenAI
from dotenv import load_dotenv
import numpy as np

load_dotenv()

class EmbeddingService:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        
        self.embedding_model = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
    
    def get_embedding(self, text: str) -> List[float]:
        """Genera un embedding vectorial para un texto dado."""
        try:
            response = self.client.embeddings.create(
                input=text,
                model=self.embedding_model
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"Error al generar embedding: {str(e)}")
            return [0.0] * 1536  # El modelo text-embedding-ada-002 tiene 1536 dimensiones
    
    def vector_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """Calcula la similitud coseno entre dos vectores."""
        v1 = np.array(vec1)
        v2 = np.array(vec2)
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    
    # En embedding_service.py
    async def get_embedding_async(self, text: str) -> List[float]:
        """Versión async del método de embeddings"""
        return await asyncio.get_event_loop().run_in_executor(
            None, 
            self.get_embedding, 
            text
        )