from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.api.v1.services.vendedores_service import VendedoresServiceORM
from app.models.dbo.vendedor import Vendedor
from app.db.database import get_db
from app.api.v1.routers.auth.jwt_handler import get_current_user

# Esquemas Pydantic para la respuesta
from pydantic import BaseModel
from datetime import datetime

class VendedorBase(BaseModel):
    vendedor: int
    nvendedor: str
    activo: bool
    lcobrador: bool
    lvendedor: bool
    empresa: int
    fecingreso: Optional[datetime] = None
    fecretiro: Optional[datetime] = None
    vcorreo: str
    tipovendedor: int
    descrip: Optional[str] = None
    idvend: Optional[str] = None

    class Config:
        orm_mode = True

router = APIRouter()

@router.get("/", response_model=List[VendedorBase])
def get_vendedores_por_empresa(
    empresa_id: int,
    activo: Optional[bool] = Query(None, description="Filtrar por vendedor activo"),
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Obtiene la lista de vendedores por empresa.
    Opcionalmente filtra por estado activo.
    """
    service = VendedoresServiceORM(db)
    vendedores = service.get_vendedores_by_empresa(empresa_id, activo)
    if not vendedores:
        return []
    return vendedores

@router.get("/{vendedor_id}", response_model=VendedorBase)
def get_vendedor(
    vendedor_id: int,
    empresa_id: int,
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Obtiene un vendedor específico por su ID dentro de una empresa.
    """
    service = VendedoresServiceORM(db)
    vendedor = service.get_vendedor_by_id(vendedor_id, empresa_id)
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor no encontrado")
    return vendedor