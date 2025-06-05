from typing import Optional
from pydantic import BaseModel


# Define Pydantic model for response
class ClienteResponse(BaseModel):
    ntipcli: Optional[str]
    clientes: Optional[str]
    nclientes: Optional[str]
    registro: Optional[str]
    npais: Optional[str]
    direccion: Optional[str]
    telefono1: Optional[str]
    razonsoc: Optional[str]
    propietario: Optional[str]
    direnvio: Optional[str]
    localidad: Optional[str]
    notas: Optional[str]
    retencion: Optional[float]
    percepcion: Optional[float]
    nosujeto: Optional[bool]
    exento: Optional[bool]
    telefono: Optional[str]
    ncondpago: Optional[str]
    limitecredito: Optional[float]
    dui: Optional[str]