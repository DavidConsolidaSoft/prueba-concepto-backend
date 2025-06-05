# app/api/v1/routers/clientes/clientes_lista.py
import logging
from fastapi import APIRouter, Depends, HTTPException, Query, Body, Path
from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any
from app.api.v1.services.clientes_service import ClientesServiceORM
from app.models.dbo.clientes import Clientes
from app.db.database import get_db
from app.api.v1.routers.auth.jwt_handler import get_current_user
from pydantic import BaseModel, Field, EmailStr, validator
from datetime import datetime
from typing import Optional, List

# Esquemas Pydantic para solicitudes y respuestas
class ClienteBase(BaseModel):
    # Información básica
    nclientes: Optional[str] = Field("", description="Nombre del cliente")
    propietario: Optional[str] = Field("", description="Nombre del propietario")
    activo: bool = Field(True, description="Estado del cliente (activo/inactivo)")
    
    # Documentos e identificación
    registro: Optional[str] = Field("", description="Número de registro")
    nit: Optional[str] = Field("", description="Número de Identificación Tributaria")
    dui: Optional[str] = Field("", description="Documento Único de Identidad")
    
    # Información de contacto
    direccion: Optional[str] = Field("", description="Dirección del cliente")
    telefono1: Optional[str] = Field("", description="Teléfono principal")
    telefono2: Optional[str] = Field("", description="Teléfono secundario")
    celular: Optional[str] = Field("", description="Número de celular")
    email: Optional[str] = Field(None, description="Correo electrónico")
    
    # Clasificación del cliente
    tipcli: Optional[int] = Field(0, description="Tipo de cliente")
    giro: Optional[str] = Field("", description="Giro del negocio")
    razonsoc: Optional[str] = Field("", description="Razón social")
    contado: bool = Field(False, description="Cliente de contado")
    
    # Información fiscal
    exento: bool = Field(False, description="Cliente exento de impuestos")
    retencion: bool = Field(False, description="Aplica retención")
    nosujeto: bool = Field(False, description="No sujeto a impuestos")
    gobierno: bool = Field(False, description="Cliente gubernamental")
    ivacero: bool = Field(False, description="IVA cero")
    percepcion: bool = Field(False, description="Aplica percepción")
    autoconsumo: bool = Field(False, description="Autoconsumo")
    PROPIO: bool = Field(False, description="Propio (Tal-Sol)")
    ExcluirCredito: bool = Field(False, description="No restringir crédito")
    
    # Configuración de créditos
    limitecredito: float = Field(0.0, description="Límite de crédito")
    
    # Información regional
    pais: int = Field(0, description="ID del país")
    municip: Optional[int] = Field(0, description="ID del municipio")
    
    # Información adicional
    condpago: Optional[int] = Field(0, description="Condición de pago")
    prodprec: Optional[int] = Field(0, description="Lista de precios")
    cliencatego: Optional[int] = Field(0, description="Categoría de cliente")
    
    class Config:
        from_attributes = True
        # Permite valores por defecto aunque el campo sea None
        populate_by_name = True
        # Validar asignaciones
        validate_assignment = True
        
class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    clientes: str = Field("", description="Código del cliente")
    empresa: int = Field(0, description="ID de la empresa")
    idClientes: int = Field(0, description="ID único del cliente")
    horatiempo: datetime = Field(default_factory=datetime.now, description="Fecha y hora de última modificación")
    
    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None
        }

class ClienteDetalle(ClienteResponse):
    # Campos adicionales para el detalle completo
    moneda: int
    transpte: int
    contacto: str
    recomendado: str
    razonsoc: str
    fax: str
    descuento: int
    promcomp: float
    prompago: float
    saldo: str
    notas: str
    usuario: int
    vendedor: int
    bodega: int
    
    class Config:
        from_attributes = True

class ClientesPaginados(BaseModel):
    items: List[ClienteResponse] = Field([], description="Lista de clientes")
    total: int = Field(0, description="Total de registros")
    page: int = Field(1, description="Página actual")
    size: int = Field(50, description="Tamaño de página")
    pages: int = Field(0, description="Total de páginas")

class ClientesPorTipoResponse(BaseModel):
    individuales: List[ClienteResponse]
    corporativos: List[ClienteResponse]
    contado: List[ClienteResponse]
    credito: List[ClienteResponse]
    
    class Config:
        from_attributes = True

router = APIRouter()

@router.get("/", response_model=ClientesPaginados)
def get_clientes_por_empresa(
    empresa_id: int,
    activo: Optional[bool] = Query(None, description="Filtrar por clientes activos"),
    tipcli: Optional[int] = Query(None, description="Filtrar por tipo de cliente"),
    search: Optional[str] = Query(None, min_length=2, description="Buscar por nombre, nit, registro o teléfono (mínimo 2 caracteres)"),
    page: int = Query(1, ge=1, description="Número de página"),
    size: int = Query(50, ge=1, le=100, description="Tamaño de página"),
    db: Session = Depends(get_db),
):
    """
    Obtiene la lista paginada de clientes por empresa.
    Ahora con validación consistente y búsqueda mejorada.
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Iniciando consulta de clientes para empresa_id={empresa_id}, search='{search}'")
    
    # Validar y limpiar término de búsqueda
    if search is not None:
        search = search.strip()
        if len(search) < 2:
            logger.warning(f"Término de búsqueda muy corto: '{search}', ignorando")
            search = None
    
    try:
        service = ClientesServiceORM(db)
        skip = (page - 1) * size
        
        # Obtener clientes usando el servicio optimizado
        clientes, total = service.get_clientes_by_empresa(
            empresa_id=empresa_id, 
            activo=activo, 
            tipcli=tipcli, 
            search=search, 
            skip=skip, 
            limit=size
        )
        
        if not clientes:
            logger.info(f"No se encontraron clientes para empresa_id={empresa_id} con búsqueda '{search}'")
            return ClientesPaginados(
                items=[],
                total=0,
                page=page,
                size=size,
                pages=0
            )
        
        # Convertir a modelos Pydantic
        clientes_response = []
        for cliente in clientes:
            try:
                cliente_model = ClienteResponse.model_validate(cliente)
                clientes_response.append(cliente_model)
            except Exception as e:
                logger.error(f"Error al validar cliente {cliente.get('clientes', 'unknown')}: {str(e)}")
        
        # Calcular número de páginas
        pages = (total + size - 1) // size if total > 0 else 0
        
        return ClientesPaginados(
            items=clientes_response,
            total=total,
            page=page,
            size=size,
            pages=pages
        )
    
    except Exception as e:
        logger.error(f"Error obteniendo clientes: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error obteniendo clientes: {str(e)}")

@router.get("/search", response_model=List[ClienteResponse])
def search_clientes(
    empresa_id: int,
    query: str = Query(..., min_length=2, description="Texto a buscar (mínimo 2 caracteres)"),
    limit: int = Query(20, ge=1, le=50, description="Cantidad máxima de resultados"),
    db: Session = Depends(get_db),
):
    """
    Búsqueda rápida de clientes para autocompletado.
    Optimizado para consistencia con el endpoint principal.
    """
    logger = logging.getLogger(__name__)
    
    # Limpiar y validar query
    query = query.strip()
    if len(query) < 2:
        logger.warning(f"Query de búsqueda muy corto: '{query}'")
        return []
    
    logger.debug(f"Iniciando búsqueda rápida: '{query}' para empresa {empresa_id}")
    
    try:
        service = ClientesServiceORM(db)
        
        # Usar el nuevo método optimizado
        clientes = service.search_clientes_optimized(
            empresa_id=empresa_id,
            search_term=query,
            limit=limit
        )
        
        if not clientes:
            logger.debug(f"No se encontraron resultados para: '{query}'")
            return []
        
        # Convertir a modelos Pydantic
        clientes_response = []
        for cliente in clientes:
            try:
                cliente_model = ClienteResponse.model_validate(cliente)
                clientes_response.append(cliente_model)
            except Exception as e:
                logger.error(f"Error al validar cliente en búsqueda: {str(e)}")
        
        logger.debug(f"Búsqueda '{query}' devolvió {len(clientes_response)} resultados")
        return clientes_response
    
    except Exception as e:
        logger.error(f"Error en búsqueda de clientes: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error en búsqueda: {str(e)}")
    

@router.get("/por-tipo", response_model=ClientesPorTipoResponse)
def get_clientes_por_tipo(
    empresa_id: int,
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Obtiene clientes agrupados por tipo.
    """
    service = ClientesServiceORM(db)
    clientes_por_tipo_dict = service.get_clientes_por_tipo(empresa_id)
    
    # Conversión explícita de cada lista de clientes
    return ClientesPorTipoResponse(
        individuales=[ClienteResponse.model_validate(c) for c in clientes_por_tipo_dict["individuales"]],
        corporativos=[ClienteResponse.model_validate(c) for c in clientes_por_tipo_dict["corporativos"]],
        contado=[ClienteResponse.model_validate(c) for c in clientes_por_tipo_dict["contado"]],
        credito=[ClienteResponse.model_validate(c) for c in clientes_por_tipo_dict["credito"]]
    )

@router.get("/{cliente_id}", response_model=ClienteDetalle)
def get_cliente(
    cliente_id: str = Path(..., description="Código del cliente"),
    empresa_id: int = Query(..., description="ID de la empresa"),
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Obtiene un cliente específico por su ID dentro de una empresa.
    """
    service = ClientesServiceORM(db)
    cliente_dict = service.get_cliente_by_id(cliente_id, empresa_id)
    
    if not cliente_dict:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    # Si el resultado es un diccionario, convertirlo directamente
    if isinstance(cliente_dict, dict):
        try:
            return ClienteDetalle.model_validate(cliente_dict)
        except Exception as e:
            print(f"Error al validar modelo: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail=f"Error al procesar datos del cliente: {str(e)}"
            )
    
    # Si es un objeto ORM, usar model_validate
    return ClienteDetalle.model_validate(cliente_dict)

@router.post("/", response_model=ClienteResponse, status_code=201)
def create_cliente(
    cliente: ClienteCreate,
    empresa_id: int = Query(..., description="ID de la empresa"),
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Crea un nuevo cliente para una empresa específica.
    """
    service = ClientesServiceORM(db)
    
    # Hardcodeamos el usuario_id por ahora, en producción se obtendría del current_user
    usuario_id = 1  # current_user["id"]
    
    try:
        nuevo_cliente = service.create_cliente(
            empresa_id=empresa_id,
            cliente_data=cliente.model_dump(exclude_unset=True),
            usuario_id=usuario_id
        )
        return ClienteResponse.model_validate(nuevo_cliente)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error al crear el cliente: {str(e)}"
        )

@router.put("/{cliente_id}", response_model=ClienteResponse)
def update_cliente(
    cliente_data: ClienteUpdate,
    cliente_id: str = Path(..., description="Código del cliente"),
    empresa_id: int = Query(..., description="ID de la empresa"),
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Actualiza un cliente existente.
    """
    service = ClientesServiceORM(db)
    
    # Hardcodeamos el usuario_id por ahora, en producción se obtendría del current_user
    usuario_id = 1  # current_user["id"]
    
    cliente_actualizado = service.update_cliente(
        cliente_id=cliente_id,
        empresa_id=empresa_id,
        cliente_data=cliente_data.model_dump(exclude_unset=True),
        usuario_id=usuario_id
    )
    
    if not cliente_actualizado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    return ClienteResponse.model_validate(cliente_actualizado)

@router.delete("/{cliente_id}", status_code=204)
def delete_cliente(
    cliente_id: str = Path(..., description="Código del cliente"),
    empresa_id: int = Query(..., description="ID de la empresa"),
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    Elimina un cliente (lo marca como inactivo).
    """
    service = ClientesServiceORM(db)
    result = service.delete_cliente(cliente_id, empresa_id)
    
    if not result:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    return {"message": "Cliente eliminado correctamente"}