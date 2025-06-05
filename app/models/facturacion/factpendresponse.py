from typing import Optional
from datetime import datetime
from pydantic import BaseModel

# Modelo Pydantic para la respuesta
class FactPendResponse(BaseModel):
    PEDIDO: str | None
    ntipomov: str | None
    numedocu: str | None
    FECHA: datetime | None
    MONTFACT: float | None
    IMPRESA: bool | None
    NULA: bool | None
    CLIENTES: str | None
    nClientes: str | None
    Registro: str | None
    nDepto: str | None
    nMunicip: str | None
    Telefono1: str | None
    factura: int | None
    caja: int | None
    efectivo: float | None
    tipomov: int | None
    ntipovta: str | None
    nvendedor: str | None
    ntipcli: str | None
    ncondpago: str | None
    si: bool | None
    notas: str | None
    neto: float | None

    class Config:
        from_attributes = True