
from datetime import datetime
from pydantic import BaseModel

class FactImpresaResponse(BaseModel):
    fecha: datetime
    numedocu: str
    ntipomov: str
    factura: int
    montfact: float
    nclientes: str
    nvendedor: str
    ncondpago: str
    tipomov: int
    condpago: int

    class Config:
        from_attributes = True