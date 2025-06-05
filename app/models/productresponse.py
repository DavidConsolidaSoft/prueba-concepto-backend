
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class ProductoResponse(BaseModel):
    korden: Optional[int]
    icdbarra: Optional[str]
    codbarra: Optional[str]
    nproducto: Optional[str]
    producto: Optional[int]
    cantidad: Optional[float]
    rcantidad: Optional[float]
    nolote: Optional[str]
    orden: Optional[str]
    fecvence: Optional[datetime]
    kardex: Optional[int]
    lote: Optional[int]
    precio: Optional[float]
    existencia: Optional[float]
    columna: Optional[int]
    volumen: Optional[float]
    tallak: Optional[float]
    factor: Optional[float]
    cant: Optional[float]
    qdec: Optional[float]
    servicios: Optional[bool]
    posicion: Optional[int]
    miimagen: Optional[str]