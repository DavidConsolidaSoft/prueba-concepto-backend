from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional, Dict
from app.api.v1.services.forma_pago_service import FormaPagoServiceORM
from app.models.dbo.formpago import FormPago
from app.models.dbo.condpago import CondPago
from app.db.database import get_db
from app.api.v1.routers.auth.jwt_handler import get_current_user
# Esquemas Pydantic para la respuesta
from pydantic import BaseModel
from datetime import datetime

class FormaPagoBase(BaseModel):
    formpago: int
    nformpago: str
    activo: bool
    frecuente: bool
    empresa: int
   
    class Config:
        orm_mode = True

class FormaPagoDetalle(FormaPagoBase):
    FIJO: Optional[bool]
    OBRA: Optional[bool]
    COMISION: Optional[bool]
    HORATIEMPO: datetime
    usuario: Optional[int]
   
    class Config:
        orm_mode = True

class FormasPagoPorTipoResponse(BaseModel):
    fijas: List[FormaPagoBase]
    por_obra: List[FormaPagoBase]
    comision: List[FormaPagoBase]
    frecuentes: List[FormaPagoBase]
   
    class Config:
        orm_mode = True

# Nuevos esquemas para condiciones de pago
class CondPagoBase(BaseModel):
    condpago: int
    ncondpago: str
    plazo: int
    contado: bool
    preferido: bool
    tarjeta: bool
    cheque: bool
    vueltaviaje: bool
    remesa: bool
    otro: bool
    
    class Config:
        orm_mode = True

class CondPagoDetalle(CondPagoBase):
    activo: bool
    empresa: int
    usuario: int
    horatiempo: datetime
    
    class Config:
        orm_mode = True

router = APIRouter()

@router.get("/", response_model=List[FormaPagoBase])
def get_formas_pago_por_empresa(
    empresa_id: int,
    activo: Optional[bool] = Query(None, description="Filtrar por formas de pago activas"),
    frecuente: Optional[bool] = Query(None, description="Filtrar por formas de pago frecuentes"),
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Obtiene la lista de formas de pago por empresa.
    Opcionalmente filtra por estado activo y/o frecuentes.
    """
    service = FormaPagoServiceORM(db)
    formas_pago = service.get_formas_pago_by_empresa(empresa_id, activo, frecuente)
    if not formas_pago:
        return []
    return formas_pago

@router.get("/por-tipo", response_model=FormasPagoPorTipoResponse)
def get_formas_pago_por_tipo(
    empresa_id: int,
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Obtiene las formas de pago categorizadas por tipo (fijas, por obra, comisión, frecuentes).
    """
    service = FormaPagoServiceORM(db)
    formas_pago_por_tipo = service.get_formas_pago_by_tipo(empresa_id)
   
    return formas_pago_por_tipo

@router.get("/{formpago_id}", response_model=FormaPagoDetalle)
def get_forma_pago(
    formpago_id: int,
    empresa_id: int,
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Obtiene una forma de pago específica por su ID dentro de una empresa.
    """
    service = FormaPagoServiceORM(db)
    forma_pago = service.get_forma_pago_by_id(formpago_id, empresa_id)
    if not forma_pago:
        raise HTTPException(status_code=404, detail="Forma de pago no encontrada")
    return forma_pago

# Nuevos endpoints para condiciones de pago
@router.get("/condiciones/", response_model=List[CondPagoBase])
def get_condiciones_pago(
    empresa_id: int,
    tipo: Optional[str] = Query(None, description="Tipo de condición de pago (contado, credito, todos)"),
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Obtiene las condiciones de pago según el tipo especificado:
    - contado: Solo condiciones de pago de contado (contado=1 or cheque=1 or tarjeta=1)
    - credito: Solo condiciones de pago de crédito (contado=0 and cheque=0 and tarjeta=0 and otro=0)
    - todos o null: Todas las condiciones de pago activas
    """
    service = FormaPagoServiceORM(db)
    
    if tipo == "contado":
        condiciones = service.get_condiciones_pago(empresa_id, solo_contado=True)
    elif tipo == "credito":
        condiciones = service.get_condiciones_pago(empresa_id, solo_credito=True)
    else:  # tipo == "todos" o None
        condiciones = service.get_condiciones_pago(empresa_id)
    
    if not condiciones:
        return []
    
    return condiciones

@router.get("/condiciones/{condpago_id}", response_model=CondPagoDetalle)
def get_condicion_pago(
    condpago_id: int,
    empresa_id: int,
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Obtiene una condición de pago específica por su ID dentro de una empresa.
    """
    service = FormaPagoServiceORM(db)
    condicion = service.get_condicion_pago_by_id(condpago_id, empresa_id)
    
    if not condicion:
        raise HTTPException(status_code=404, detail="Condición de pago no encontrada")
    
    return condicion