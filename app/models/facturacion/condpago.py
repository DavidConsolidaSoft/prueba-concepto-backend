
from pydantic import BaseModel
from enum import Enum

class FilterType(Enum):
    TODOS = "TODOS"
    CONTADO = "CONTADO"
    CREDITO = "CREDITO"

class CondPagoResponse(BaseModel):
    ncondpago: str
    plazo: int
    contado: bool
    condpago: int
    preferido: bool
    tarjeta: bool
    cheque: bool
    vueltaviaje: bool
    remesa: bool
    otro: bool

    class Config:
        from_attributes = True