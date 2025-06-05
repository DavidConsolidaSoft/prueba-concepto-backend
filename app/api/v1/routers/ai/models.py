from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class DynamicQueryRequest(BaseModel):
    """Modelo para solicitudes de consultas dinámicas."""
    text: str
    limit: int = 10
    offset: int = 0
    order_by: Optional[str] = None
    descending: bool = True

class DynamicQueryResponse(BaseModel):
    """Modelo para respuestas de consultas dinámicas."""
    results: List[Dict[str, Any]]
    orm_code: str
    processing_time: float
    total_results: int
    message: str