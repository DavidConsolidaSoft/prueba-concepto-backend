from pydantic import BaseModel
from typing import Optional

class TipoMovResponse(BaseModel):
    ntipomov: str
    tipomov: int
    correl: int
    Preferido: bool  # Changed from preferido to Preferido to match SQL
    coniva: bool
    tiquet: bool
    nlineasmax: int
    informe: Optional[str]
    notacred: bool
    exportacion: bool
    noaplicariva: bool
    contado: Optional[bool]
    prodprec: int
    condpago: int
    norestariva: bool
    docunico: bool
    ptovta: bool
    efectivo: bool
    qmin: float
    correlpropio: bool
    remision: bool

    class Config:
        from_attributes = True