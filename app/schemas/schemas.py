from pydantic import BaseModel, ConfigDict
from typing import Optional

class Get_by_email(BaseModel):
    tipo: int
    llave: Optional[str] = None
    notas: Optional[str] = None
    equipo: Optional[str] = None
    ma: Optional[str] = None
    mb: Optional[str] = None
    mc: Optional[str] = None
    md: Optional[str] = None

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

class CajaParams(BaseModel):
    caja: int
    bodega: int
    vendedor: int
    empresa: int
    prodprec: int
    usuario: int
    nempresa: str
    nusuario: str

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

class ConStrg(BaseModel):
    ma: str
    mb: str
    mc: str
    md: str

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)