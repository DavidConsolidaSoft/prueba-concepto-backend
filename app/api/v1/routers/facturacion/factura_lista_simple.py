# app/api/v1/routers/facturacion/factura_lista_simple.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, date
from app.db.database import get_db
from app.api.v1.services.factura_service_orm import FacturaService
from app.models.facturacion.factura_lista_models import (
    FacturaListSimple,
    FacturaListItem
)

router = APIRouter()

@router.get("/simple", response_model=List[FacturaListSimple])
async def get_facturas_simple(
    fecha_inicio: Optional[date] = Query(None, description="Fecha inicial"),
    fecha_fin: Optional[date] = Query(None, description="Fecha final"),
    estado: Optional[str] = Query("abiertas", description="Estado: abiertas, cerradas, nulas"),
    empresa: int = Query(1, description="ID de la empresa"),
    db: Session = Depends(get_db)
):
    """
    Endpoint simplificado que retorna la lista de facturas con los campos básicos
    que se muestran en la interfaz móvil.
    """
    try:
        # Valores por defecto para fechas
        if not fecha_inicio:
            fecha_inicio = date.today().replace(day=1)
        if not fecha_fin:
            fecha_fin = date.today()
        
        fecha_inicio_dt = datetime.combine(fecha_inicio, datetime.min.time())
        fecha_fin_dt = datetime.combine(fecha_fin, datetime.max.time())
        
        # Determinar filtro basado en estado
        solo_sin_imprimir = estado == "abiertas"
        
        service = FacturaService(db)
        facturas = service.get_facturas_list(
            empresa=empresa,
            fecha_inicio=fecha_inicio_dt,
            fecha_fin=fecha_fin_dt,
            solo_sin_imprimir=solo_sin_imprimir
        )
        
        # Filtrar por estado si es necesario
        if estado == "nulas":
            facturas = [f for f in facturas if f.nula]
        elif estado == "cerradas":
            facturas = [f for f in facturas if f.impresa and not f.nula]
        
        # Convertir a formato simple
        facturas_simple = []
        for f in facturas:
            factura_simple = FacturaListSimple(
                codigo_factura=f.numedocu,
                nombre_empresa=f.nombre_cliente,  # En el ejemplo se muestra el cliente como "empresa"
                nombre_vendedor=f.nombre_vendedor,
                total_factura=f.monto_total,
                fecha_factura=f.fecha,
                estado_factura="Abierta" if not f.impresa else ("Nula" if f.nula else "Cerrada")
            )
            facturas_simple.append(factura_simple)
        
        return facturas_simple
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener facturas: {str(e)}"
        )

@router.get("/completa", response_model=List[FacturaListItem])
async def get_facturas_completa(
    fecha_inicio: Optional[date] = Query(None, description="Fecha inicial"),
    fecha_fin: Optional[date] = Query(None, description="Fecha final"),
    cliente: Optional[str] = Query(None, description="Filtro por cliente"),
    pedido: Optional[str] = Query(None, description="Filtro por pedido"),
    caja: Optional[str] = Query(None, description="Filtro por caja"),
    solo_sin_imprimir: bool = Query(False, description="Solo sin imprimir"),
    empresa: int = Query(1, description="ID de la empresa"),
    db: Session = Depends(get_db)
):
    """
    Endpoint que retorna la lista completa de facturas con todos los campos.
    Similar al query SQL original.
    """
    try:
        # Valores por defecto para fechas
        if not fecha_inicio:
            fecha_inicio = date.today().replace(day=1)
        if not fecha_fin:
            fecha_fin = date.today()
        
        fecha_inicio_dt = datetime.combine(fecha_inicio, datetime.min.time())
        fecha_fin_dt = datetime.combine(fecha_fin, datetime.max.time())
        
        service = FacturaService(db)
        facturas = service.get_facturas_list(
            empresa=empresa,
            fecha_inicio=fecha_inicio_dt,
            fecha_fin=fecha_fin_dt,
            cliente=cliente,
            pedido=pedido,
            caja=caja,
            solo_sin_imprimir=solo_sin_imprimir
        )
        
        return facturas
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener facturas: {str(e)}"
        )

@router.get("/test")
async def test_endpoint():
    """Endpoint de prueba para verificar que el router funciona"""
    return {"message": "Router de facturas funcionando correctamente"}