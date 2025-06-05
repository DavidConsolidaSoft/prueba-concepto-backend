from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

router = APIRouter(prefix="/api/tipoprod", tags=["tipoprod"])

class TipoProdResponse(BaseModel):
    NTIPOPROD: str
    image: Optional[str] = Field(default=None)  # Agregado valor por defecto
    PREFERIDO: Optional[bool] = None
    ACTIVO: Optional[bool] = None
    TIPOPROD: Optional[int] = None
    EMPRESA: int
    PARANCEL: Optional[float] = None
    PUNO: Optional[int] = Field(default=None)  # Agregado valor por defecto
    PDOS: Optional[int] = Field(default=None)  # Agregado valor por defecto
    PTRES: Optional[bool] = Field(default=None)  # Agregado valor por defecto
    PCUATRO: Optional[int] = Field(default=None)  # Agregado valor por defecto
    PCINCO: Optional[int] = Field(default=None)  # Agregado valor por defecto
    VOL1: Optional[int] = Field(default=None)  # Agregado valor por defecto
    VOL2: Optional[int] = Field(default=None)  # Agregado valor por defecto
    VOL3: Optional[int] = Field(default=None)  # Agregado valor por defecto
    VOL4: Optional[int] = Field(default=None)  # Agregado valor por defecto
    VOL5: Optional[int] = Field(default=None)  # Agregado valor por defecto
    FECHA1: Optional[datetime] = Field(default=None)  # Agregado valor por defecto
    FECHA2: Optional[datetime] = Field(default=None)  # Agregado valor por defecto
    FACTOR1: Optional[int] = Field(default=None)  # Agregado valor por defecto
    FACTOR2: Optional[int] = Field(default=None)  # Agregado valor por defecto
    FACTOR3: Optional[int] = Field(default=None)  # Agregado valor por defecto
    FACTOR4: Optional[int] = Field(default=None)  # Agregado valor por defecto
    FACTOR5: Optional[int] = Field(default=None)  # Agregado valor por defecto
    PRINCIPAL: Optional[bool] = Field(default=None)  # Agregado valor por defecto

    class Config:
        from_attributes = True