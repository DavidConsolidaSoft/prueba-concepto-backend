import logging
import time
import traceback
import math
from fastapi import APIRouter, Depends, HTTPException, Query, BackgroundTasks
from sqlalchemy.orm import Session
from sqlalchemy import func, and_, desc, extract, cast, Date, String
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from app.db.database import get_db
from app.api.v1.routers.auth.azure_auth import get_current_user
from app.models.models import Factura, DFactura, Producto, Kardex, Vendedor, Clientes
from app.api.v1.services.reporte_cache_service import ReporteCacheService

# Configurar logger
logger = logging.getLogger(__name__)

# Crear router para gráficos
router = APIRouter()

# Instanciar servicio de caché
reporte_cache = ReporteCacheService()

# Función auxiliar para formatear números grandes
def format_large_number(num):
    """
    Formatea números grandes para mejor visualización:
    - Si es mayor a 1 millón, muestra como X.XM
    - Si es mayor a 1000, muestra como X.XK
    - Redondea a 1 decimal
    """
    if num >= 1000000:
        return f"{num/1000000:.1f}M"
    elif num >= 1000:
        return f"{num/1000:.1f}K"
    else:
        return f"{num:.0f}"

# Función para actualizar la caché en segundo plano
def update_cache_background(reporte_tipo: str, params: Dict[str, Any], data: Dict[str, Any]):
    """Función para actualizar la caché en segundo plano."""
    try:
        reporte_cache.cache_report(reporte_tipo, params, data)
    except Exception as e:
        logger.error(f"Error actualizando caché en segundo plano: {str(e)}")

@router.get("/top-vendedores")
async def get_top_vendedores(
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    fecha_inicio: Optional[str] = Query(None, description="Fecha de inicio en formato YYYY-MM-DD"),
    fecha_fin: Optional[str] = Query(None, description="Fecha de fin en formato YYYY-MM-DD"),
    empresa: int = Query(1, description="ID de la empresa"),
    limit: int = Query(10, description="Número de vendedores a retornar"),
    bypass_cache: bool = Query(False, description="Ignorar caché y forzar consulta a BD")
):
    """
    Retorna los top vendedores por ventas netas en un período determinado.
    """
    try:
        # Configurar fechas por defecto si no se proporcionan
        if not fecha_inicio:
            fecha_inicio = datetime(datetime.now().year, 1, 1).strftime("%Y-%m-%d")
        if not fecha_fin:
            fecha_fin = datetime.now().strftime("%Y-%m-%d")
        
        # Parámetros para la caché
        cache_params = {
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "empresa": empresa,
            "limit": limit
        }
        
        # Verificar si los datos están en caché y no se solicitó bypass
        if not bypass_cache:
            cached_data = reporte_cache.get_cached_report("top_vendedores", cache_params)
            if cached_data:
                return {
                    "success": True,
                    "data": cached_data,
                    "from_cache": True
                }
            
        # Si no está en caché o se solicitó bypass, ejecutar consulta
        start_time = time.time()
        
        # Consulta usando ORM
        resultado = db.query(
            Vendedor.nvendedor,
            func.sum(DFactura.afecta + DFactura.exenta - DFactura.vdesc - DFactura.vgdesc).label('ventaNeta')
        ).join(
            Factura, Factura.vendedor == Vendedor.vendedor
        ).join(
            DFactura, DFactura.factura == Factura.factura
        ).filter(
            and_(
                Factura.empresa == empresa,
                Factura.fecha >= fecha_inicio,
                Factura.fecha <= fecha_fin,
                Factura.impresa == 1,
                Factura.nula == 0
            )
        ).group_by(
            Vendedor.nvendedor
        ).order_by(
            func.sum(DFactura.afecta + DFactura.exenta).desc()
        ).limit(limit).all()
        
        # Procesar resultados
        vendedores_data = []
        
        for row in resultado:
            # Acortar el nombre del vendedor si es muy largo
            vendedor_name = row.nvendedor.strip() if row.nvendedor else "Sin nombre"
            if len(vendedor_name) > 10:
                vendedor_name = vendedor_name[:7] + "..."

            # Obtener el valor numérico y redondearlo para presentación
            venta_neta = float(row.ventaNeta) if row.ventaNeta is not None else 0
            
            vendedores_data.append({
                "nvendedor": vendedor_name,
                "ventaNeta": venta_neta,
                "ventaNetaFormatted": format_large_number(venta_neta)  # Versión formateada para mostrar
            })
            
        # Preparar datos para gráficos
        labels = [item["nvendedor"] for item in vendedores_data]
        values = [item["ventaNeta"] for item in vendedores_data]
        formatted_values = [item["ventaNetaFormatted"] for item in vendedores_data]
        
        # Generar colores para el gráfico
        colors = [
            "rgba(75, 192, 192, 0.6)",
            "rgba(54, 162, 235, 0.6)",
            "rgba(255, 206, 86, 0.6)",
            "rgba(255, 99, 132, 0.6)",
            "rgba(153, 102, 255, 0.6)",
            "rgba(255, 159, 64, 0.6)",
            "rgba(199, 199, 199, 0.6)",
            "rgba(83, 102, 255, 0.6)",
            "rgba(40, 159, 64, 0.6)",
            "rgba(210, 199, 199, 0.6)"
        ] * 2  # Duplicar la lista para asegurar suficientes colores
        
        # Preparar respuesta
        response_data = {
            "vendedores": vendedores_data,
            "chart": {
                "labels": labels,
                "datasets": [
                    {
                        "data": values,
                        "formattedData": formatted_values,  # Valores formateados para mostrar
                        "label": "Venta Neta",
                        "backgroundColor": colors[:len(values)]
                    }
                ]
            }
        }
        
        # Guardar en caché en segundo plano para no afectar el tiempo de respuesta
        background_tasks.add_task(update_cache_background, "top_vendedores", cache_params, response_data)
        
        return {
            "success": True,
            "data": response_data,
            "processing_time": time.time() - start_time,
            "from_cache": False
        }
        
    except Exception as e:
        logger.error(f"Error en top-vendedores: {str(e)}\n{traceback.format_exc()}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al procesar consulta: {str(e)}"
        )

@router.get("/top-productos")
async def get_top_productos(
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    fecha_inicio: Optional[str] = Query(None, description="Fecha de inicio en formato YYYY-MM-DD"),
    fecha_fin: Optional[str] = Query(None, description="Fecha de fin en formato YYYY-MM-DD"),
    empresa: int = Query(1, description="ID de la empresa"),
    limit: int = Query(20, description="Número de productos a retornar"),
    grafico_tipo: str = Query("barras", description="Tipo de gráfico: barras, pie, pie_agrupado"),
    bypass_cache: bool = Query(False, description="Ignorar caché y forzar consulta a BD")
):
    """
    Retorna los top productos más vendidos por ventas netas en un período determinado.
    """
    try:
        # Configurar fechas por defecto si no se proporcionan
        if not fecha_inicio:
            fecha_inicio = datetime(datetime.now().year, 1, 1).strftime("%Y-%m-%d")
        if not fecha_fin:
            fecha_fin = datetime.now().strftime("%Y-%m-%d")
        
        # Parámetros para la caché
        cache_params = {
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "empresa": empresa,
            "limit": limit,
            "grafico_tipo": grafico_tipo
        }
        
        # Verificar si los datos están en caché y no se solicitó bypass
        if not bypass_cache:
            cached_data = reporte_cache.get_cached_report("top_productos", cache_params)
            if cached_data:
                return {
                    "success": True,
                    "data": cached_data,
                    "from_cache": True
                }
            
        # Si no está en caché o se solicitó bypass, ejecutar consulta
        start_time = time.time()
        
        # Consulta usando ORM
        resultado = db.query(
            Producto.nproducto,
            func.sum(DFactura.afecta + DFactura.exenta - DFactura.vdesc - DFactura.vgdesc).label('ventaNeta')
        ).join(
            Kardex, Kardex.producto == Producto.producto
        ).join(
            DFactura, DFactura.kardex == Kardex.kardex
        ).join(
            Factura, Factura.factura == DFactura.factura
        ).filter(
            and_(
                Factura.empresa == empresa,
                Factura.fecha >= fecha_inicio,
                Factura.fecha <= fecha_fin,
                Factura.impresa == 1,
                Factura.nula == 0
            )
        ).group_by(
            Producto.nproducto
        ).order_by(
            func.sum(DFactura.afecta + DFactura.exenta).desc()
        ).limit(limit).all()
        
        # Procesar resultados
        productos_data = []
        
        for row in resultado:
            # Limpiar el nombre del producto (quitar espacios en blanco adicionales)
            product_name = row.nproducto.strip() if row.nproducto else "Sin nombre"
            
            # Truncar nombres largos
            if len(product_name) > 40:
                product_name = product_name[:37] + "..."
            
            # Obtener el valor numérico
            venta_neta = float(row.ventaNeta) if row.ventaNeta is not None else 0
                
            productos_data.append({
                "producto": product_name,
                "ventaNeta": venta_neta,
                "ventaNetaFormatted": format_large_number(venta_neta)
            })
        
        # Preparar datos para diferentes tipos de gráficos
        if grafico_tipo == "pie_agrupado":
            # Agrupar productos pequeños como "Otros"
            # Primero, calcular el total
            total = sum(item["ventaNeta"] for item in productos_data)
            
            # Definir umbral para agrupar (productos con menos del 5% del total)
            umbral_porcentaje = 0.05
            
            # Separar productos grandes y pequeños
            productos_grandes = []
            productos_pequenos = []
            
            for item in productos_data:
                if item["ventaNeta"] / total >= umbral_porcentaje:
                    productos_grandes.append(item)
                else:
                    productos_pequenos.append(item)
            
            # Crear categoría "Otros" si hay productos pequeños
            if productos_pequenos:
                otros_total = sum(item["ventaNeta"] for item in productos_pequenos)
                productos_grandes.append({
                    "producto": f"Otros ({len(productos_pequenos)} productos)",
                    "ventaNeta": otros_total,
                    "ventaNetaFormatted": format_large_number(otros_total)
                })
            
            # Preparar datos para el gráfico
            labels = [item["producto"] for item in productos_grandes]
            values = [item["ventaNeta"] for item in productos_grandes]
            formatted_values = [item["ventaNetaFormatted"] for item in productos_grandes]
            
            # Si sólo queda un producto, añadir un producto ficticio para evitar un gráfico de una sola sección
            if len(labels) == 1:
                labels.append("Sin ventas")
                values.append(0.1)  # Valor muy pequeño
                formatted_values.append("0")
            
        else:
            # Para gráficos normales, usar todos los productos
            labels = [item["producto"] for item in productos_data]
            values = [item["ventaNeta"] for item in productos_data]
            formatted_values = [item["ventaNetaFormatted"] for item in productos_data]
        
        # Generar colores para el gráfico
        colors = [
            "rgba(255, 99, 132, 0.6)",
            "rgba(54, 162, 235, 0.6)",
            "rgba(255, 206, 86, 0.6)",
            "rgba(75, 192, 192, 0.6)",
            "rgba(153, 102, 255, 0.6)",
            "rgba(255, 159, 64, 0.6)",
            "rgba(199, 199, 199, 0.6)",
            "rgba(83, 102, 255, 0.6)",
            "rgba(40, 159, 64, 0.6)",
            "rgba(210, 199, 199, 0.6)",
            "rgba(78, 52, 199, 0.6)",
            "rgba(225, 99, 132, 0.6)",
            "rgba(24, 162, 235, 0.6)",
            "rgba(215, 206, 86, 0.6)",
            "rgba(95, 192, 192, 0.6)",
            "rgba(183, 102, 255, 0.6)",
            "rgba(200, 159, 64, 0.6)",
            "rgba(129, 199, 199, 0.6)",
            "rgba(63, 102, 255, 0.6)",
            "rgba(140, 159, 64, 0.6)"
        ]
        
        # Agregar metadatos adicionales para gráficos
        chart_data = {
            "labels": labels,
            "datasets": [
                {
                    "data": values,
                    "formattedData": formatted_values,  # Valores formateados
                    "backgroundColor": colors[:len(values)]
                }
            ]
        }
        
        # Agregar información adicional según el tipo de gráfico
        if grafico_tipo == "barras":
            chart_data["chart_type"] = "bar"
            chart_data["datasets"][0]["label"] = "Venta Neta"
        elif grafico_tipo == "pie" or grafico_tipo == "pie_agrupado":
            chart_data["chart_type"] = "pie"
        
        # Preparar respuesta
        response_data = {
            "productos": productos_data,
            "chart": chart_data,
            "chart_type": grafico_tipo
        }
        
        # Guardar en caché en segundo plano
        background_tasks.add_task(update_cache_background, "top_productos", cache_params, response_data)
        
        return {
            "success": True,
            "data": response_data,
            "processing_time": time.time() - start_time,
            "from_cache": False
        }
        
    except Exception as e:
        logger.error(f"Error en top-productos: {str(e)}\n{traceback.format_exc()}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al procesar consulta: {str(e)}"
        )

@router.get("/top-clientes")
async def get_top_clientes(
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    fecha_inicio: Optional[str] = Query(None, description="Fecha de inicio en formato YYYY-MM-DD"),
    fecha_fin: Optional[str] = Query(None, description="Fecha de fin en formato YYYY-MM-DD"),
    empresa: int = Query(1, description="ID de la empresa"),
    limit: int = Query(20, description="Número de clientes a retornar"),
    bypass_cache: bool = Query(False, description="Ignorar caché y forzar consulta a BD")
):
    """
    Retorna los top clientes por ventas netas en un período determinado.
    """
    try:
        # Configurar fechas por defecto si no se proporcionan
        if not fecha_inicio:
            fecha_inicio = datetime(datetime.now().year, 1, 1).strftime("%Y-%m-%d")
        if not fecha_fin:
            fecha_fin = datetime.now().strftime("%Y-%m-%d")
        
        # Parámetros para la caché
        cache_params = {
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "empresa": empresa,
            "limit": limit
        }
        
        # Verificar si los datos están en caché y no se solicitó bypass
        if not bypass_cache:
            cached_data = reporte_cache.get_cached_report("top_clientes", cache_params)
            if cached_data:
                return {
                    "success": True,
                    "data": cached_data,
                    "from_cache": True
                }
            
        # Si no está en caché o se solicitó bypass, ejecutar consulta
        start_time = time.time()
        
        # Consulta usando ORM
        resultado = db.query(
            Clientes.nclientes,
            func.sum(Factura.afecta + Factura.exenta).label('ventaNeta')
        ).join(
            Factura, and_(
                Factura.clientes == Clientes.clientes,
                Clientes.empresa == empresa
            )
        ).filter(
            and_(
                Factura.empresa == empresa,
                Factura.fecha >= fecha_inicio,
                Factura.fecha <= fecha_fin,
                Factura.impresa == 1,
                Factura.nula == 0
            )
        ).group_by(
            Clientes.nclientes
        ).order_by(
            func.sum(Factura.afecta + Factura.exenta).desc()
        ).limit(limit).all()
        
        # Procesar resultados
        clientes_data = []
        
        for row in resultado:
            # Limpiar el nombre del cliente (quitar espacios en blanco adicionales)
            client_name = row.nclientes.strip() if row.nclientes else "Sin nombre"
            
            # Acortar nombres largos
            if len(client_name) > 10:
                client_name = client_name[:7] + "..."
            
            # Obtener el valor numérico
            venta_neta = float(row.ventaNeta) if row.ventaNeta is not None else 0
            
            clientes_data.append({
                "cliente": client_name,
                "ventaNeta": venta_neta,
                "ventaNetaFormatted": format_large_number(venta_neta)
            })
            
        # Preparar datos para gráficos
        labels = [item["cliente"] for item in clientes_data]
        values = [item["ventaNeta"] for item in clientes_data]
        formatted_values = [item["ventaNetaFormatted"] for item in clientes_data]
        
        # Generar colores para el gráfico
        colors = [
            "rgba(75, 192, 192, 0.6)",
            "rgba(54, 162, 235, 0.6)",
            "rgba(255, 206, 86, 0.6)",
            "rgba(255, 99, 132, 0.6)",
            "rgba(153, 102, 255, 0.6)"
        ] * 4
        
        # Preparar respuesta
        response_data = {
            "clientes": clientes_data,
            "chart": {
                "labels": labels,
                "datasets": [
                    {
                        "data": values,
                        "formattedData": formatted_values,  # Valores formateados
                        "label": "Venta Neta",
                        "backgroundColor": colors[:len(values)]
                    }
                ],
                "chart_type": "bar"
            }
        }
        
        # Guardar en caché en segundo plano
        background_tasks.add_task(update_cache_background, "top_clientes", cache_params, response_data)
        
        return {
            "success": True,
            "data": response_data,
            "processing_time": time.time() - start_time,
            "from_cache": False
        }
        
    except Exception as e:
        logger.error(f"Error en top-clientes: {str(e)}\n{traceback.format_exc()}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al procesar consulta: {str(e)}"
        )

@router.get("/ventas-periodo")
async def get_ventas_periodo(
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    periodo: str = Query("mensual", description="Periodo: diario, semanal, mensual, anual"),
    fecha_inicio: Optional[str] = Query(None, description="Fecha de inicio en formato YYYY-MM-DD"),
    fecha_fin: Optional[str] = Query(None, description="Fecha de fin en formato YYYY-MM-DD"),
    empresa: int = Query(1, description="ID de la empresa"),
    bypass_cache: bool = Query(False, description="Ignorar caché y forzar consulta a BD")
):
    """
    Retorna las ventas agrupadas por periodo (diario, semanal, mensual, anual).
    """
    try:
        # Configurar fechas por defecto si no se proporcionan
        if not fecha_inicio:
            # Si es anual, tomamos los últimos 5 años
            if periodo == "anual":
                fecha_inicio = (datetime.now() - timedelta(days=365*5)).strftime("%Y-%m-%d")
            # Si es mensual, tomamos el último año
            elif periodo == "mensual":
                fecha_inicio = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
            # Si es semanal, tomamos los últimos 3 meses
            elif periodo == "semanal":
                fecha_inicio = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
            # Si es diario, tomamos el último mes
            else:
                fecha_inicio = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
                
        if not fecha_fin:
            fecha_fin = datetime.now().strftime("%Y-%m-%d")
        
        # Parámetros para la caché
        cache_params = {
            "periodo": periodo,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "empresa": empresa
        }
        
        # Verificar si los datos están en caché y no se solicitó bypass
        if not bypass_cache:
            cached_data = reporte_cache.get_cached_report("ventas_periodo", cache_params)
            if cached_data:
                return {
                    "success": True,
                    "data": cached_data,
                    "from_cache": True
                }
        
        start_time = time.time()
        
        # Base query
        query = db.query(
            func.sum(Factura.afecta + Factura.exenta).label('ventaNeta')
        ).filter(
            and_(
                Factura.empresa == empresa,
                Factura.fecha >= fecha_inicio,
                Factura.fecha <= fecha_fin,
                Factura.impresa == 1,
                Factura.nula == 0
            )
        )
        
        # Adaptar el group by según el período
        if periodo == "diario":
            # For daily, use cast to date to remove time component
            query = db.query(
                cast(Factura.fecha, Date).label('periodo'),
                func.sum(Factura.afecta + Factura.exenta).label('ventaNeta')
            ).filter(
                and_(
                    Factura.empresa == empresa,
                    Factura.fecha >= fecha_inicio,
                    Factura.fecha <= fecha_fin,
                    Factura.impresa == 1,
                    Factura.nula == 0
                )
            ).group_by(
                cast(Factura.fecha, Date)
            ).order_by(
                cast(Factura.fecha, Date)
            )
            
        elif periodo == "semanal":
            # Para SQL Server, usar funciones específicas para obtener año y semana
            year_expr = func.year(Factura.fecha)
            week_expr = func.datepart('week', Factura.fecha)
            
            # Combinar año y semana en un formato legible
            periodo_expr = func.concat(
                cast(year_expr, String),
                '-W',
                func.right('0' + cast(week_expr, String), 2)
            )
            
            query = db.query(
                periodo_expr.label('periodo'),
                func.sum(Factura.afecta + Factura.exenta).label('ventaNeta')
            ).filter(
                and_(
                    Factura.empresa == empresa,
                    Factura.fecha >= fecha_inicio,
                    Factura.fecha <= fecha_fin,
                    Factura.impresa == 1,
                    Factura.nula == 0
                )
            ).group_by(
                year_expr, 
                week_expr,
                periodo_expr
            ).order_by(
                year_expr,
                week_expr
            )
            
        elif periodo == "mensual":
            # Para SQL Server, usar funciones específicas
            year_expr = func.year(Factura.fecha)
            month_expr = func.month(Factura.fecha)
            
            # Formar una expresión para la parte del mes con formato "01", "02", etc.
            month_str = func.right('0' + cast(month_expr, String), 2)
            
            # Crear una expresión para el formato año-mes (YYYY-MM)
            periodo_expr = func.concat(
                cast(year_expr, String),
                '-',
                month_str
            )
            
            query = db.query(
                periodo_expr.label('periodo'),
                func.sum(Factura.afecta + Factura.exenta).label('ventaNeta')
            ).filter(
                and_(
                    Factura.empresa == empresa,
                    Factura.fecha >= fecha_inicio,
                    Factura.fecha <= fecha_fin,
                    Factura.impresa == 1,
                    Factura.nula == 0
                )
            ).group_by(
                year_expr,
                month_expr,
                periodo_expr
            ).order_by(
                year_expr,
                month_expr
            )
            
        elif periodo == "anual":
            # For yearly, just extract the year
            year_expr = func.year(Factura.fecha)
            
            query = db.query(
                year_expr.label('periodo'),
                func.sum(Factura.afecta + Factura.exenta).label('ventaNeta')
            ).filter(
                and_(
                    Factura.empresa == empresa,
                    Factura.fecha >= fecha_inicio,
                    Factura.fecha <= fecha_fin,
                    Factura.impresa == 1,
                    Factura.nula == 0
                )
            ).group_by(
                year_expr
            ).order_by(
                year_expr
            )
        
        # Ejecutar consulta
        resultado = query.all()
        
        # Procesar resultados
        ventas_data = []
        
        for row in resultado:
            # Obtener el valor numérico
            venta_neta = float(row.ventaNeta) if row.ventaNeta is not None else 0
            
            ventas_data.append({
                "periodo": str(row.periodo),
                "ventaNeta": venta_neta,
                "ventaNetaFormatted": format_large_number(venta_neta)
            })
            
        # Preparar datos para gráficos
        labels = [item["periodo"] for item in ventas_data]
        values = [item["ventaNeta"] for item in ventas_data]
        formatted_values = [item["ventaNetaFormatted"] for item in ventas_data]
        
        # Preparar respuesta
        response_data = {
            "ventas": ventas_data,
            "chart": {
                "labels": labels,
                "datasets": [
                    {
                        "data": values,
                        "formattedData": formatted_values,  # Valores formateados
                        "label": "Venta Neta",
                        "borderColor": "rgba(75, 192, 192, 1)",
                        "backgroundColor": "rgba(75, 192, 192, 0.2)",
                        "fill": True,
                        "tension": 0.4
                    }
                ],
                "chart_type": "line"
            }
        }
        
        # Guardar en caché en segundo plano
        background_tasks.add_task(update_cache_background, "ventas_periodo", cache_params, response_data)
        
        return {
            "success": True,
            "data": response_data,
            "processing_time": time.time() - start_time,
            "from_cache": False
        }
        
    except Exception as e:
        logger.error(f"Error en ventas-periodo: {str(e)}\n{traceback.format_exc()}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al procesar consulta: {str(e)}"
        )

# Endpoints para administración de caché

@router.get("/cache/stats")
async def get_cache_stats():
    """
    Obtiene estadísticas sobre la caché de reportes.
    """
    try:
        stats = reporte_cache.get_cache_stats()
        return {
            "success": True,
            "stats": stats
        }
    except Exception as e:
        logger.error(f"Error obteniendo estadísticas de caché: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener estadísticas: {str(e)}"
        )

@router.post("/cache/invalidate")
async def invalidate_cache(
    reporte_tipo: Optional[str] = Query(None, description="Tipo de reporte a invalidar (None para todos)")
):
    """
    Invalida la caché para un tipo específico de reporte o para todos.
    """
    try:
        invalidated = reporte_cache.invalidate_cache(reporte_tipo)
        return {
            "success": True,
            "invalidated": invalidated,
            "message": f"Se invalidaron {invalidated} registros de caché"
        }
    except Exception as e:
        logger.error(f"Error invalidando caché: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al invalidar caché: {str(e)}"
        )

@router.post("/cache/purge-expired")
async def purge_expired_cache():
    """
    Elimina entradas de caché expiradas.
    """
    try:
        purged = reporte_cache.purge_expired_cache()
        return {
            "success": True,
            "purged": purged,
            "message": f"Se eliminaron {purged} registros de caché expirados"
        }
    except Exception as e:
        logger.error(f"Error purgando caché expirada: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al purgar caché: {str(e)}"
        )

@router.post("/cache/preload")
async def preload_cache(
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Precarga la caché con los reportes más comunes para mejorar rendimiento.
    """
    try:
        # Fecha actual
        fecha_fin = datetime.now().strftime("%Y-%m-%d")
        
        # Fechas de inicio para distintos períodos
        fecha_inicio_anual = datetime(datetime.now().year, 1, 1).strftime("%Y-%m-%d")
        fecha_inicio_trimestral = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
        
        # Lista de tareas de precarga
        preload_tasks = [
            # Top vendedores - Anual
            {
                "endpoint": get_top_vendedores,
                "params": {
                    "db": db,
                    "fecha_inicio": fecha_inicio_anual,
                    "fecha_fin": fecha_fin,
                    "empresa": 1,
                    "limit": 10,
                    "bypass_cache": True
                }
            },
            # Top productos - Anual (formato pie)
            {
                "endpoint": get_top_productos,
                "params": {
                    "db": db,
                    "fecha_inicio": fecha_inicio_anual,
                    "fecha_fin": fecha_fin,
                    "empresa": 1,
                    "limit": 20,
                    "grafico_tipo": "pie_agrupado",
                    "bypass_cache": True
                }
            },
            # Top clientes - Anual
            {
                "endpoint": get_top_clientes,
                "params": {
                    "db": db,
                    "fecha_inicio": fecha_inicio_anual,
                    "fecha_fin": fecha_fin,
                    "empresa": 1,
                    "limit": 20,
                    "bypass_cache": True
                }
            },
            # Ventas por periodo - Mensual (último año)
            {
                "endpoint": get_ventas_periodo,
                "params": {
                    "db": db,
                    "periodo": "mensual",
                    "fecha_inicio": fecha_inicio_anual,
                    "fecha_fin": fecha_fin,
                    "empresa": 1,
                    "bypass_cache": True
                }
            },
            # Ventas por periodo - Diario (últimos 30 días)
            {
                "endpoint": get_ventas_periodo,
                "params": {
                    "db": db,
                    "periodo": "diario",
                    "fecha_inicio": fecha_inicio_trimestral,
                    "fecha_fin": fecha_fin,
                    "empresa": 1,
                    "bypass_cache": True
                }
            }
        ]
        
        # Función para ejecutar precarga en segundo plano
        async def execute_preload():
            try:
                logger.info(f"Iniciando precarga de {len(preload_tasks)} reportes")
                
                for i, task in enumerate(preload_tasks):
                    try:
                        logger.info(f"Precargando reporte {i+1}/{len(preload_tasks)}")
                        # Añadir background_tasks como parámetro
                        task["params"]["background_tasks"] = background_tasks
                        await task["endpoint"](**task["params"])
                    except Exception as task_error:
                        logger.error(f"Error en precarga de tarea {i+1}: {str(task_error)}")
                
                logger.info("Precarga de caché completada")
            except Exception as preload_error:
                logger.error(f"Error en proceso de precarga: {str(preload_error)}")
        
        # Ejecutar precarga en segundo plano
        background_tasks.add_task(execute_preload)
        
        return {
            "success": True,
            "message": f"Precarga de {len(preload_tasks)} reportes iniciada en segundo plano"
        }
    except Exception as e:
        logger.error(f"Error en precarga de caché: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al iniciar precarga: {str(e)}"
        )