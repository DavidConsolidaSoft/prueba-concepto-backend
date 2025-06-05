from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime, date
from app.api.v1.services.productos_service import ProductosServiceORM
from app.db.database import get_db
from app.api.v1.routers.auth.jwt_handler import get_current_user

# Esquemas Pydantic actualizados
class ListaPrecio(BaseModel):
    prodprec: int
    fechainicial: Optional[datetime]
    fechafinal: Optional[datetime]
   
    class Config:
        from_attributes = True

class ProductosResponse(BaseModel):
    productos: List[Dict[str, Any]]
    total: int
    pagina: int
    total_paginas: int
    items_por_pagina: int
    tiene_promociones: bool
   
    class Config:
        from_attributes = True

class BusquedaTiempoRealResponse(BaseModel):
    productos: List[Dict[str, Any]]
    total_resultados: int
    termino_busqueda: str

router = APIRouter()

@router.get("/diagnostico")
def diagnostico_completo(
    empresa_id: int = Query(1),
    caja_id: int = Query(1),  
    prodprec_id: int = Query(1),
    db: Session = Depends(get_db)
):
    """
    🩺 DIAGNÓSTICO COMPLETO - Usar este endpoint primero
    """
    try:
        service = ProductosServiceORM(db)
        
        diagnostico = service.diagnosticar_datos_basico(empresa_id, caja_id, prodprec_id)
        
        return {
            "status": "success",
            "mensaje": "Diagnóstico completado",
            "empresa_id": empresa_id,
            "caja_id": caja_id,
            "prodprec_id": prodprec_id,
            "diagnostico": diagnostico
        }
        
    except Exception as e:
        return {
            "status": "error",
            "mensaje": str(e),
            "empresa_id": empresa_id,
            "caja_id": caja_id,
            "prodprec_id": prodprec_id,
            "diagnostico": {}
        }

@router.get("/listas-precios", response_model=List[ListaPrecio])
def get_listas_precios(
    empresa_id: int,
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    ✅ Obtiene listas de precios - YA FUNCIONA
    """
    try:
        service = ProductosServiceORM(db)
        listas = service.get_listas_precios(empresa_id)
       
        if not listas:
            return []
       
        return listas
    except Exception as e:
        print(f"Error en listas de precios: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al obtener listas de precios: {str(e)}")

@router.get("/kardex", response_model=ProductosResponse)
def get_productos_kardex(
    empresa_id: int,
    caja_id: int,
    prodprec_id: int,
    busqueda: Optional[str] = Query("%", description="Texto para buscar productos"),
    bodega: Optional[str] = Query("%", description="Filtro de bodega"),
    solo_existencias: Optional[bool] = Query(True, description="Solo productos con existencias"),
    con_estante: Optional[bool] = Query(False, description="Incluir ubicación - DESACTIVADO"),
    precio_promo: Optional[bool] = Query(False, description="Usar precios promocionales"),
    es_control_mesa: Optional[bool] = Query(False, description="Para control de mesas"),
    pagina: Optional[int] = Query(1, ge=1, description="Número de página"),
    items_por_pagina: Optional[int] = Query(10, ge=1, le=50, description="Elementos por página"),
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    🔄 Obtiene productos del kardex - VERSIÓN SIMPLIFICADA
    """
    try:
        service = ProductosServiceORM(db)
       
        resultado = service.get_productos_kardex(
            empresa_id=empresa_id,
            caja_id=caja_id,
            prodprec_id=prodprec_id,
            busqueda=busqueda,
            bodega=bodega,
            solo_existencias=solo_existencias,
            con_estante=False,  
            precio_promo=precio_promo,
            es_control_mesa=es_control_mesa,
            pagina=pagina,
            items_por_pagina=items_por_pagina
        )
       
        return resultado
        
    except Exception as e:
        print(f"Error en productos kardex: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al obtener productos: {str(e)}")

@router.get("/buscar", response_model=BusquedaTiempoRealResponse)
def buscar_productos_tiempo_real(
    empresa_id: int,
    caja_id: int,
    prodprec_id: int,
    q: str = Query(..., min_length=2, description="Término de búsqueda (mínimo 2 caracteres)"),
    limit: Optional[int] = Query(10, ge=1, le=30, description="Límite de resultados"),
    bodega: Optional[str] = Query("%", description="Filtro de bodega"),
    db: Session = Depends(get_db),
    # current_user: dict = Depends(get_current_user)
):
    """
    🔍 Búsqueda en tiempo real - VERSIÓN SIMPLIFICADA
    """
    try:
        service = ProductosServiceORM(db)
        
        productos = service.buscar_productos_tiempo_real(
            empresa_id=empresa_id,
            caja_id=caja_id,
            prodprec_id=prodprec_id,
            busqueda=q,
            limit=limit,
            bodega=bodega
        )
        
        return {
            "productos": productos,
            "total_resultados": len(productos),
            "termino_busqueda": q
        }
        
    except Exception as e:
        print(f"Error en búsqueda tiempo real: {str(e)}")
        return {
            "productos": [],
            "total_resultados": 0,
            "termino_busqueda": q
        }

@router.get("/test-simple")
def test_productos_simple(
    empresa_id: int = Query(1),
    caja_id: int = Query(1),  
    prodprec_id: int = Query(1),
    db: Session = Depends(get_db)
):
    """
    🔍 Test simple - SIN SQL RAW
    """
    try:
        service = ProductosServiceORM(db)
        
        # Usar método ORM simple
        productos = service.get_productos_kardex_simple(
            empresa_id=empresa_id,
            caja_id=caja_id,
            prodprec_id=prodprec_id,
            busqueda="",
            limit=5,
            offset=0
        )
        
        return {
            "status": "success",
            "total_productos": len(productos),
            "productos": productos[:3] if productos else [],
            "mensaje": "Consulta ORM simple exitosa"
        }
        
    except Exception as e:
        return {
            "status": "error",
            "mensaje": str(e),
            "productos": []
        }

@router.get("/debug/{busqueda}")
def debug_busqueda(
    busqueda: str,
    empresa_id: int = Query(1),
    caja_id: int = Query(1),  
    prodprec_id: int = Query(1),
    db: Session = Depends(get_db)
):
    """
    📝 Debug de búsquedas específicas - SIN SQL RAW
    """
    try:
        service = ProductosServiceORM(db)
        
        # Probar con método ORM simple
        productos = service.get_productos_kardex_simple(
            empresa_id=empresa_id,
            caja_id=caja_id,
            prodprec_id=prodprec_id,
            busqueda=busqueda,
            limit=10,
            offset=0
        )
        
        return {
            "busqueda_original": busqueda,
            "busqueda_normalizada": f"%{busqueda}%",
            "total_encontrados": len(productos),
            "productos": productos
        }
        
    except Exception as e:
        return {
            "error": str(e),
            "busqueda_original": busqueda,
            "productos": []
        }

@router.get("/conteo-rapido")
def conteo_rapido(
    empresa_id: int = Query(1),
    caja_id: int = Query(1),  
    prodprec_id: int = Query(1),
    db: Session = Depends(get_db)
):
    """
    📊 Conteo rápido de registros
    """
    try:
        service = ProductosServiceORM(db)
        
        # Contar cada tabla por separado
        from app.models.dbo.producto import Producto
        from app.models.dbo.kardex import Kardex
        from app.models.dbo.dprodprec import DProdPrec
        
        productos_total = db.query(Producto).filter(Producto.empresa == empresa_id).count()
        productos_activos = db.query(Producto).filter(
            Producto.empresa == empresa_id, 
            Producto.activo == True
        ).count()
        
        kardex_total = db.query(Kardex).filter(Kardex.empresa == empresa_id).count()
        
        precios_total = db.query(DProdPrec).filter(
            DProdPrec.empresa == empresa_id,
            DProdPrec.prodprec == prodprec_id
        ).count()
        
        return {
            "empresa_id": empresa_id,
            "productos_total": productos_total,
            "productos_activos": productos_activos,
            "kardex_registros": kardex_total,
            "precios_registros": precios_total,
            "estado": "OK" if all([productos_activos > 0, kardex_total > 0, precios_total > 0]) else "PROBLEMA"
        }
        
    except Exception as e:
        return {
            "error": str(e),
            "estado": "ERROR"
        }