
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class CarteraClienteResponse(BaseModel):
    tipocliente: str
    codigo: str
    grupocliente: Optional[str]
    NombreCliente: str
    fecha: datetime
    fechavencimiento: datetime
    tipodocumento: str
    documento: str
    monto: float
    cargo: float
    abono: float
    saldo: float
    vencida: int
    antiguedad: int
    vendedor: str
    telefono: Optional[str]
    pais: Optional[str]
    departamento: Optional[str]
    municipio: Optional[str]
    direccion: Optional[str]
    limitecredito: float
    razonsocial: Optional[str]
    registro: Optional[str]
    contrato: bool
    plazo: int
    caja: str

    class Config:
        from_attributes = True