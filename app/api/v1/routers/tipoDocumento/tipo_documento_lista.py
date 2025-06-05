from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any
from app.api.v1.services.tipoDocumento_service import TipoDocumentoServiceORM
from app.models.dbo.tipomov import TipoMov
from app.db.database import get_db
from app.api.v1.routers.auth.jwt_handler import get_current_user
# Esquemas Pydantic para la respuesta
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Union

class TipoDocumentoBase(BaseModel):
    tipomov: int
    ntipomov: str
    activo: bool
    factura: bool
    notacred: bool
    compra: bool
    ANTICIPO: bool
    notadebito: bool
    pedido: bool
    inventario: bool
    cargo: str
    correl: int
    empresa: int
   
    class Config:
        orm_mode = True
        
class TipoDocumentoDetalle(TipoDocumentoBase):
    preferido: bool
    coniva: bool
    iva: bool
    cancelacion: bool
    anulacion: bool
    notacargo: bool
    produccion: bool
    cambodega: bool
    devolucion: bool
    efectivo: bool
    cheque: bool
    ajuste: bool
    impuesto: bool
    costo: bool
    bonificacion: bool
    bonifextra: bool
    invinicial: bool
    nlineasmax: int
    modulo: int
    controlcorrel: int
    qmin: int
    qmax: int
   
    class Config:
        orm_mode = True

class TiposDocumentoResponse(BaseModel):
    facturas: List[TipoDocumentoBase]
    notas_credito: List[TipoDocumentoBase]
    compras: List[TipoDocumentoBase]
    inventario: List[TipoDocumentoBase]
    pedidos: List[TipoDocumentoBase]
   
    class Config:
        orm_mode = True

# Nuevo esquema para la respuesta de la consulta de facturas según país
class TipoDocumentoFacturaPais(BaseModel):
    ntipomov: str
    tipomov: int
    correl: int
    Preferido: bool
    coniva: bool
    tiquet: bool
    nlineasmax: int
    informe: str
    notacred: bool
    exportacion: bool
    noaplicariva: bool
    contado: Optional[bool] = None
    prodprec: int
    condpago: int
    norestariva: bool
    docunico: int
    ptovta: int
    efectivo: bool
    qmin: int
    correlpropio: bool
    remision: bool

    class Config:
        orm_mode = True

router = APIRouter()

@router.get("/", response_model=List[TipoDocumentoBase])
def get_documentos_por_empresa(
    empresa_id: int,
    activo: Optional[bool] = Query(None, description="Filtrar por documento activo"),
    tipo: Optional[str] = Query(None, description="Filtrar por tipo de documento (factura, notacred, compra, etc.)"),
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Obtiene la lista de tipos de documento (movimiento) por empresa.
    Opcionalmente filtra por estado activo y tipo específico.
    """
    service = TipoDocumentoServiceORM(db)
    documentos = service.get_documentos_by_empresa(empresa_id, activo, tipo)
    if not documentos:
        return []
    return documentos

@router.get("/categorias", response_model=TiposDocumentoResponse)
def get_documentos_por_categoria(
    empresa_id: int,
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Obtiene tipos de documento agrupados por categorías (facturas, notas de crédito, etc.)
    """
    service = TipoDocumentoServiceORM(db)
    documentos_categorizados = service.get_tipos_documento(empresa_id)
   
    return documentos_categorizados

@router.get("/{tipomov_id}", response_model=TipoDocumentoDetalle)
def get_documento(
    tipomov_id: int,
    empresa_id: int,
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Obtiene un tipo de documento específico por su ID dentro de una empresa.
    """
    service = TipoDocumentoServiceORM(db)
    documento = service.get_documento_by_id(tipomov_id, empresa_id)
    if not documento:
        raise HTTPException(status_code=404, detail="Tipo de documento no encontrado")
    return documento

@router.get("/facturas/pais", response_model=List[TipoDocumentoFacturaPais])
def get_facturas_por_empresa_pais(
    empresa_id: int,
    caja_id: Optional[int] = Query(None, description="ID de la caja para determinar configuración de tiquetes"),
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Obtiene la lista de tipos de documento de factura según la lógica específica por país,
    replicando exactamente la consulta SQL original con sus condicionales por país y tiquete.
    """
    service = TipoDocumentoServiceORM(db)
    documentos = service.get_facturas_by_empresa_pais(empresa_id, caja_id)
    
    if not documentos:
        return []
    
    return documentos