# app/api/v1/routers/facturacion/factura_lista.py
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, date
from app.db.database import get_db
from app.api.v1.routers.auth.jwt_handler import get_current_user
from app.api.v1.services.factura_service_simple_orm import FacturaServiceSimpleORM
from app.models.facturacion.factura_lista_models import (
    FacturaListItem,
    FacturaDetalle,
    DetalleProducto,
    ResumenDia
)
import logging

# Configurar logging
logger = logging.getLogger(__name__)

# Modelo para respuesta paginada
class FacturasPaginadas(BaseModel):
    items: List[FacturaListItem]
    total: int
    page: int
    size: int
    pages: int

router = APIRouter()

@router.get("/lista", response_model=FacturasPaginadas)
async def get_facturas(
    fecha_inicio: Optional[date] = Query(None, description="Fecha inicial para filtrar facturas"),
    fecha_fin: Optional[date] = Query(None, description="Fecha final para filtrar facturas"),
    cliente: Optional[str] = Query(None, description="Nombre o código del cliente"),
    pedido: Optional[str] = Query(None, description="Número de pedido o documento"),
    caja: Optional[str] = Query(None, description="Caja"),
    estado: Optional[str] = Query(None, description="Estado: abiertas, cerradas, nulas, todas"),
    empresa: int = Query(..., description="ID de la empresa (requerido)", ge=1),
    orden: int = Query(1, description="Tipo de ordenamiento (1-6)", ge=1, le=6),
    psat_tipo: int = Query(0, description="Tipo de factura SAT (0: normal, 1-2: FEL, 3: DTE)"),
    moneda: int = Query(1, description="Código de moneda"),
    search: Optional[str] = Query(None, min_length=2, description="Búsqueda general (mínimo 2 caracteres)"),
    page: int = Query(1, ge=1, description="Número de página"),
    size: int = Query(50, ge=1, le=100, description="Tamaño de página"),
    db: Session = Depends(get_db)
):
    """
    Obtiene la lista de facturas filtradas por los parámetros especificados.
    """
    try:
        # Validar y limpiar término de búsqueda
        if search is not None:
            search = search.strip()
            if len(search) < 2:
                logger.warning(f"Término de búsqueda muy corto: '{search}', ignorando")
                search = None
        
        # Usar valores por defecto si no se proporcionan fechas
        if not fecha_inicio:
            fecha_inicio = date.today()
        if not fecha_fin:
            fecha_fin = date.today()
       
        fecha_inicio_dt = datetime.combine(fecha_inicio, datetime.min.time())
        fecha_fin_dt = datetime.combine(fecha_fin, datetime.max.time())
        
        # Determinar filtro de impresión basado en estado
        solo_sin_imprimir = False
        aplicar_filtro_estado = True  # Nueva bandera
        
        if estado == "abiertas":
            solo_sin_imprimir = True
        elif estado == "todas":
            aplicar_filtro_estado = False
        
        # Calcular skip para paginación
        skip = (page - 1) * size
        
        logger.info(f"Consultando facturas: empresa={empresa}, búsqueda='{search}', estado='{estado}', página={page}")
        
        service = FacturaServiceSimpleORM(db)
        facturas, total = service.get_facturas_list(
            empresa=empresa,
            fecha_inicio=fecha_inicio_dt,
            fecha_fin=fecha_fin_dt,
            cliente=cliente,
            pedido=pedido,
            caja=caja,
            solo_sin_imprimir=solo_sin_imprimir,
            orden=orden,
            psat_tipo=psat_tipo,
            moneda=moneda,
            search=search,
            skip=skip,
            limit=size
        )
        
        # Aplicar filtro de estado adicional si es necesario
        if aplicar_filtro_estado and estado and estado != "todas":
            facturas_filtradas = []
            for f in facturas:
                if estado == "abiertas" and f.estado == "Abierta":
                    facturas_filtradas.append(f)
                elif estado == "cerradas" and f.estado == "Cerrada":
                    facturas_filtradas.append(f)
                elif estado == "nulas" and f.estado == "Nula":
                    facturas_filtradas.append(f)
            
            # Ajustar el total si filtramos localmente
            if len(facturas_filtradas) != len(facturas):
                ratio = len(facturas_filtradas) / len(facturas) if len(facturas) > 0 else 1
                total = int(total * ratio)
            
            facturas = facturas_filtradas
        
        # Calcular número de páginas
        pages = (total + size - 1) // size if total > 0 else 0
        
        logger.info(f"Retornando {len(facturas)} facturas de {total} totales")
        
        return FacturasPaginadas(
            items=facturas,
            total=total,
            page=page,
            size=size,
            pages=pages
        )
       
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.error(f"Error al obtener la lista de facturas: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener la lista de facturas: {str(e)}"
        )

@router.get("/search", response_model=List[FacturaListItem])
async def search_facturas(
    empresa: int,
    query: str = Query(..., min_length=2, description="Texto a buscar (mínimo 2 caracteres)"),
    fecha_inicio: Optional[date] = Query(None, description="Fecha inicial para la búsqueda"),
    fecha_fin: Optional[date] = Query(None, description="Fecha final para la búsqueda"),
    limit: int = Query(20, ge=1, le=50, description="Cantidad máxima de resultados"),
    db: Session = Depends(get_db)
):
    """
    Búsqueda rápida de facturas para autocompletado.
    Optimizado para búsquedas en tiempo real.
    """
    
    # Limpiar y validar query
    query = query.strip()
    if len(query) < 2:
        logger.warning(f"Query de búsqueda muy corto: '{query}'")
        return []
    
    try:
        # Usar valores por defecto si no se proporcionan fechas
        if not fecha_inicio:
            fecha_inicio = date.today().replace(day=1)  # Primer día del mes
        if not fecha_fin:
            fecha_fin = date.today()
            
        fecha_inicio_dt = datetime.combine(fecha_inicio, datetime.min.time())
        fecha_fin_dt = datetime.combine(fecha_fin, datetime.max.time())
        
        logger.info(f"Búsqueda rápida: empresa={empresa}, query='{query}', limit={limit}")
        
        # Usar el servicio de búsqueda optimizada
        service = FacturaServiceSimpleORM(db)
        facturas = service.search_facturas_optimized(
            empresa=empresa,
            search_term=query,
            fecha_inicio=fecha_inicio_dt,
            fecha_fin=fecha_fin_dt,
            limit=limit
        )
        
        logger.info(f"Búsqueda completada: {len(facturas)} resultados")
        return facturas
        
    except Exception as e:
        logger.error(f"Error en búsqueda de facturas: {str(e)}", exc_info=True)
        # Retornar lista vacía en lugar de lanzar excepción
        return []

@router.get("/empresa/{empresa_id}", response_model=List[FacturaListItem])
async def get_facturas_por_empresa(
    empresa_id: int,
    fecha_inicio: Optional[date] = Query(None, description="Fecha inicial"),
    fecha_fin: Optional[date] = Query(None, description="Fecha final"),
    orden: int = Query(1, description="Tipo de ordenamiento (1-6)", ge=1, le=6),
    psat_tipo: int = Query(0, description="Tipo de factura SAT (0: normal, 1-2: FEL, 3: DTE)"),
    moneda: int = Query(1, description="Código de moneda"),
    db: Session = Depends(get_db)
):
    """
    Obtiene todas las facturas de una empresa específica.
    """
    try:
        if not fecha_inicio:
            fecha_inicio = date.today().replace(day=1)
        if not fecha_fin:
            fecha_fin = date.today()
       
        fecha_inicio_dt = datetime.combine(fecha_inicio, datetime.min.time())
        fecha_fin_dt = datetime.combine(fecha_fin, datetime.max.time())
       
        # USAR EL SERVICIO CON TODOS LOS PARÁMETROS
        service = FacturaServiceSimpleORM(db)
        facturas = service.get_facturas_list(
            empresa=empresa_id,
            fecha_inicio=fecha_inicio_dt,
            fecha_fin=fecha_fin_dt,
            orden=orden,
            psat_tipo=psat_tipo,
            moneda=moneda
        )
       
        return facturas
       
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener facturas de la empresa {empresa_id}: {str(e)}"
        )

@router.get("/por-fecha", response_model=List[FacturaListItem])
async def get_facturas_por_fecha(
    fecha_inicio: date = Query(..., description="Fecha inicial requerida"),
    fecha_fin: date = Query(..., description="Fecha final requerida"),
    empresa: int = Query(..., description="ID de la empresa (requerido)", ge=1),
    orden: int = Query(1, description="Tipo de ordenamiento (1-6)", ge=1, le=6),
    psat_tipo: int = Query(0, description="Tipo de factura SAT (0: normal, 1-2: FEL, 3: DTE)"),
    moneda: int = Query(1, description="Código de moneda"),
    db: Session = Depends(get_db)
):
    """
    Obtiene facturas en un rango de fechas específico.
    """
    try:
        fecha_inicio_dt = datetime.combine(fecha_inicio, datetime.min.time())
        fecha_fin_dt = datetime.combine(fecha_fin, datetime.max.time())
       
        # USAR EL SERVICIO
        service = FacturaServiceSimpleORM(db)
        facturas = service.get_facturas_list(
            empresa=empresa,
            fecha_inicio=fecha_inicio_dt,
            fecha_fin=fecha_fin_dt,
            orden=orden,
            psat_tipo=psat_tipo,
            moneda=moneda
        )
       
        return facturas
       
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener facturas por fecha: {str(e)}"
        )

@router.get("/por-estado/{estado}", response_model=List[FacturaListItem])
async def get_facturas_por_estado(
    estado: str,
    empresa: int = Query(..., description="ID de la empresa (requerido)", ge=1),
    fecha_inicio: Optional[date] = Query(None, description="Fecha inicial"),
    fecha_fin: Optional[date] = Query(None, description="Fecha final"),
    orden: int = Query(1, description="Tipo de ordenamiento (1-6)", ge=1, le=6),
    psat_tipo: int = Query(0, description="Tipo de factura SAT (0: normal, 1-2: FEL, 3: DTE)"),
    moneda: int = Query(1, description="Código de moneda"),
    db: Session = Depends(get_db)
):
    """
    Obtiene facturas filtradas por estado específico.
    """
    if estado not in ["abiertas", "cerradas", "nulas"]:
        raise HTTPException(
            status_code=400,
            detail="Estado inválido. Use: abiertas, cerradas o nulas"
        )
    
    try:
        if not fecha_inicio:
            fecha_inicio = date.today().replace(day=1)
        if not fecha_fin:
            fecha_fin = date.today()
       
        fecha_inicio_dt = datetime.combine(fecha_inicio, datetime.min.time())
        fecha_fin_dt = datetime.combine(fecha_fin, datetime.max.time())
        
        solo_sin_imprimir = estado == "abiertas"
        
        # USAR EL SERVICIO
        service = FacturaServiceSimpleORM(db)
        facturas = service.get_facturas_list(
            empresa=empresa,
            fecha_inicio=fecha_inicio_dt,
            fecha_fin=fecha_fin_dt,
            solo_sin_imprimir=solo_sin_imprimir,
            orden=orden,
            psat_tipo=psat_tipo,
            moneda=moneda
        )
        
        # Filtrar por estado
        if estado == "abiertas":
            facturas = [f for f in facturas if not f.impresa and not f.nula]
        elif estado == "cerradas":
            facturas = [f for f in facturas if f.impresa and not f.nula]
        elif estado == "nulas":
            facturas = [f for f in facturas if f.nula]
       
        return facturas
       
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener facturas por estado: {str(e)}"
        )

@router.get("/detalle/{factura_id}", response_model=FacturaDetalle)
async def get_factura_detalle(
    factura_id: int,
    empresa: int = Query(..., description="ID de la empresa (requerido)", ge=1),
    db: Session = Depends(get_db)
):
    """
    Obtiene el detalle completo de una factura específica.
    
    Incluye:
    - Información del encabezado
    - Datos del cliente
    - Información del vendedor
    - Forma de pago
    - Totales y descuentos
    - Lista de productos
    """
    try:
        service = FacturaServiceSimpleORM(db)
        factura_detalle = service.get_factura_detalle(
            factura_id=factura_id,
            empresa=empresa
        )
        
        if not factura_detalle:
            raise HTTPException(
                status_code=404,
                detail=f"Factura {factura_id} no encontrada para la empresa {empresa}"
            )
        
        return factura_detalle
        
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener el detalle de la factura: {str(e)}"
        )