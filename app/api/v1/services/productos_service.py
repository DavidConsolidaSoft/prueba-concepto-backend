from sqlalchemy.orm import Session
from sqlalchemy import func, case, select, literal, and_, or_, not_, Integer, Float, String, Boolean, Date, desc, asc, text
from sqlalchemy.sql.expression import cast, extract
from typing import List, Optional, Dict, Any
from datetime import date, datetime
import math
import re

# Importar modelos
from app.models.dbo.producto import Producto
from app.models.dbo.kardex import Kardex
from app.models.dbo.lote import Lote
from app.models.dbo.dprodprec import DProdPrec
from app.models.dbo.prodprec import ProdPrec
from app.models.dbo.umedida import UMedida
from app.models.dbo.ubicaprod import UbicaProd
from app.models.dbo.dcambodega import DCamboBodega
from app.models.dbo.controlperiodo import ControlPeriodo

class ProductosServiceORM:
    def __init__(self, db: Session):
        self.db = db
        self.db.autoflush = False
    
    def diagnosticar_datos_basico(self, empresa_id: int, caja_id: int, prodprec_id: int) -> Dict[str, Any]:
        """
        Diagnóstico básico usando ORM simple
        """
        diagnostico = {}
        
        try:
            # 1. Contar productos
            productos_count = self.db.query(Producto).filter(
                Producto.empresa == empresa_id,
                Producto.activo == True
            ).count()
            diagnostico['productos_activos'] = productos_count
            
            # 2. Contar kardex
            kardex_count = self.db.query(Kardex).filter(
                Kardex.empresa == empresa_id
            ).count()
            diagnostico['kardex_registros'] = kardex_count
            
            # 3. Contar lotes
            lotes_count = self.db.query(Lote).count()
            diagnostico['lotes_registros'] = lotes_count
            
            # 4. Contar precios
            precios_count = self.db.query(DProdPrec).filter(
                DProdPrec.empresa == empresa_id,
                DProdPrec.prodprec == prodprec_id
            ).count()
            diagnostico['precios_registros'] = precios_count
            
            # 5. Muestra de datos
            sample_productos = self.db.query(Producto.producto, Producto.nproducto).filter(
                Producto.empresa == empresa_id,
                Producto.activo == True
            ).limit(3).all()
            diagnostico['muestra_productos'] = [
                {"id": p.producto, "nombre": p.nproducto} for p in sample_productos
            ]
            
            # 6. Muestra de kardex
            sample_kardex = self.db.query(Kardex.kardex, Kardex.producto, Kardex.cantidad).filter(
                Kardex.empresa == empresa_id
            ).limit(3).all()
            diagnostico['muestra_kardex'] = [
                {"kardex": k.kardex, "producto": k.producto, "cantidad": float(k.cantidad)} 
                for k in sample_kardex
            ]
            
            # 7. Muestra de precios
            sample_precios = self.db.query(DProdPrec.producto, DProdPrec.tprecio).filter(
                DProdPrec.empresa == empresa_id,
                DProdPrec.prodprec == prodprec_id
            ).limit(3).all()
            diagnostico['muestra_precios'] = [
                {"producto": p.producto, "precio": float(p.tprecio)} 
                for p in sample_precios
            ]
            
        except Exception as e:
            diagnostico['error'] = str(e)
            
        return diagnostico
    
    def get_fecha_periodo(self, empresa_id: int, caja_id: int) -> Optional[date]:
        """Obtiene la fecha del periodo activo"""
        try:
            resultado = self.db.query(ControlPeriodo.fecha).filter(
                ControlPeriodo.empresa == empresa_id,
                ControlPeriodo.caja == caja_id,
                ControlPeriodo.cerrado == 0,
                ControlPeriodo.caja != 0,
                ControlPeriodo.sincro == 0
            ).first()
            
            return resultado.fecha if resultado else None
        except:
            return None
    
    def get_listas_precios(self, empresa_id: int) -> List[Dict[str, Any]]:
        """Obtiene las listas de precios disponibles para la empresa"""
        try:
            listas = self.db.query(
                ProdPrec.prodprec,
                ProdPrec.fechainicial,
                ProdPrec.fechafinal
            ).filter(
                ProdPrec.empresa == empresa_id
            ).order_by(ProdPrec.prodprec).all()
            
            return [
                {"prodprec": lista.prodprec, "fechainicial": lista.fechainicial, "fechafinal": lista.fechafinal}
                for lista in listas
            ]
        except Exception as e:
            print(f"Error en get_listas_precios: {str(e)}")
            return []
    
    def verificar_lista_precios_promo(self, empresa_id: int, fecha_periodo: date) -> bool:
        """Verifica si hay promociones activas"""
        try:
            if not fecha_periodo:
                return False
            
            resultado = self.db.query(ProdPrec.prodprec).filter(
                ProdPrec.fechainicial.isnot(None),
                ProdPrec.fechafinal.isnot(None),
                cast(ProdPrec.fechainicial, Date) <= fecha_periodo,
                cast(ProdPrec.fechafinal, Date) >= fecha_periodo,
                ProdPrec.empresa == empresa_id
            ).first()
            
            return True if resultado else False
        except:
            return False
    
    def get_productos_kardex_simple(
        self,
        empresa_id: int,
        caja_id: int,
        prodprec_id: int,
        busqueda: str = "%",
        limit: int = 20,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """
        CONSULTA FINAL - Con precios reales
        """
        try:
            # CONSULTA DIRECTA de productos únicos CON PRECIOS REALES
            query = self.db.query(
                Producto.producto,
                Producto.nproducto,
                Producto.icdbarra,
                Producto.codbarra,
                Producto.servicios,
                Producto.columna,
                Producto.volumen,
                Producto.costo,
                Producto.exento,
                DProdPrec.tprecio,    # PRECIO REAL
                DProdPrec.fprecio     # PRECIO REAL
            ).distinct()
            
            # Join con precios
            query = query.join(DProdPrec, and_(
                DProdPrec.producto == Producto.producto,
                DProdPrec.prodprec == prodprec_id,
                DProdPrec.empresa == empresa_id
            ))
            
            # Filtros básicos
            query = query.filter(
                Producto.empresa == empresa_id,
                Producto.activo == True,
                Producto.showroom == False,
                Producto.enventa == True,
                Producto.incluir == False,
                Producto.cicloanterior == False
            )
            
            # Filtro de búsqueda
            if busqueda and busqueda != "%":
                search_pattern = f"%{busqueda}%"
                query = query.filter(or_(
                    Producto.nproducto.ilike(search_pattern),
                    Producto.icdbarra.ilike(search_pattern),
                    Producto.codbarra.ilike(search_pattern)
                ))
            
            # Ordenamiento
            query = query.order_by(Producto.nproducto)
            
            # Aplicar límites
            if offset > 0:
                query = query.offset(offset)
            if limit > 0:
                query = query.limit(limit)
            
            # Ejecutar consulta
            result = query.all()
            
            # Convertir a diccionarios
            productos = []
            for row in result:
                producto_dict = {
                    "producto": row.producto,
                    "nproducto": (f"(Ex) " if row.exento else "") + (row.nproducto.strip() if row.nproducto else ""),
                    "icdbarra": row.icdbarra.strip() if row.icdbarra else "",
                    "codbarra": row.codbarra.strip() if row.codbarra else "",
                    "cantidad": 100.0,  # Valor temporal
                    "rcantidad": 0.0,
                    "nolote": "LOTE001",
                    "orden": "",
                    "fecvence": None,
                    "kardex": 1,
                    "lote": 1,
                    "tprecio": float(row.tprecio) if row.tprecio else 0.0,  # PRECIO REAL
                    "fprecio": float(row.fprecio) if row.fprecio else 0.0,  # PRECIO REAL
                    "existencia": 1,
                    "columna": float(row.columna) if row.columna else 0.0,
                    "volumen": float(row.volumen) if row.volumen else 0.0,
                    "tallak": float(row.costo) if row.costo else 0.0,
                    "factor": 1.0,
                    "cant": 100,
                    "qdec": 0.0,
                    "servicios": bool(row.servicios),
                    "promo": 0,
                    "korden": 0
                }
                productos.append(producto_dict)
            
            return productos
            
        except Exception as e:
            print(f"Error en get_productos_kardex_simple: {str(e)}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            return []
   
    def contar_productos_total(
        self,
        empresa_id: int,
        caja_id: int,
        prodprec_id: int,
        busqueda: str = "%"
    ) -> int:
        """
        Contar total de productos que coinciden con los filtros
        """
        try:
            query = self.db.query(func.count(Producto.producto))
            
            # Mismos joins que en get_productos_kardex_simple
            query = query.join(Kardex, and_(
                Kardex.producto == Producto.producto,
                Kardex.bodega.like('%')
            ))
            
            query = query.join(Lote, Lote.lote == Kardex.lote)
            
            query = query.join(DProdPrec, and_(
                DProdPrec.producto == Producto.producto,
                DProdPrec.prodprec == prodprec_id,
                DProdPrec.empresa == empresa_id
            ))
            
            # Mismos filtros
            query = query.filter(
                Producto.empresa == empresa_id,
                Kardex.empresa == empresa_id,
                Producto.activo == True,
                Producto.showroom == False,
                Producto.enventa == True,
                Producto.incluir == False,
                Producto.cicloanterior == False
            )
            
            # Mismo filtro de búsqueda
            if busqueda and busqueda != "%":
                search_pattern = f"%{busqueda}%"
                query = query.filter(or_(
                    Producto.nproducto.ilike(search_pattern),
                    Producto.icdbarra.ilike(search_pattern),
                    Producto.codbarra.ilike(search_pattern),
                    Lote.nolote.ilike(search_pattern)
                ))
            
            return query.scalar() or 0
            
        except Exception as e:
            print(f"Error en contar_productos_total: {str(e)}")
            return 0
    
    def get_productos_kardex(
        self,
        empresa_id: int,
        caja_id: int,
        prodprec_id: int,
        busqueda: str = "%",
        bodega: str = "%",
        solo_existencias: bool = True,
        con_estante: bool = True,
        precio_promo: bool = False,
        es_control_mesa: bool = False,
        pagina: int = 1,
        items_por_pagina: int = 20
    ) -> Dict[str, Any]:
        """
        Método principal SIMPLIFICADO que usa las funciones básicas
        """
        try:
            # Calcular offset
            offset = (pagina - 1) * items_por_pagina
            
            # Obtener productos usando método simple
            productos = self.get_productos_kardex_simple(
                empresa_id=empresa_id,
                caja_id=caja_id,
                prodprec_id=prodprec_id,
                busqueda=busqueda,
                limit=items_por_pagina,
                offset=offset
            )
            
            # Contar total
            total_count = self.contar_productos_total(
                empresa_id=empresa_id,
                caja_id=caja_id,
                prodprec_id=prodprec_id,
                busqueda=busqueda
            )
            
            # Verificar promociones
            fecha_periodo = self.get_fecha_periodo(empresa_id, caja_id)
            tiene_promociones = self.verificar_lista_precios_promo(empresa_id, fecha_periodo) if fecha_periodo else False
            
            # Calcular metadatos
            total_paginas = math.ceil(total_count / items_por_pagina) if total_count > 0 else 1
            
            return {
                "productos": productos,
                "total": total_count,
                "pagina": pagina,
                "total_paginas": total_paginas,
                "items_por_pagina": items_por_pagina,
                "tiene_promociones": tiene_promociones
            }
            
        except Exception as e:
            print(f"Error en get_productos_kardex: {str(e)}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            
            return {
                "productos": [],
                "total": 0,
                "pagina": pagina,
                "total_paginas": 1,
                "items_por_pagina": items_por_pagina,
                "tiene_promociones": False
            }
    
    def buscar_productos_tiempo_real(
        self,
        empresa_id: int,
        caja_id: int,
        prodprec_id: int,
        busqueda: str,
        limit: int = 10,
        bodega: str = "%"
    ) -> List[Dict[str, Any]]:
        """
        Búsqueda en tiempo real usando método simple
        """
        if not busqueda or len(busqueda.strip()) < 2:
            return []
        
        try:
            return self.get_productos_kardex_simple(
                empresa_id=empresa_id,
                caja_id=caja_id,
                prodprec_id=prodprec_id,
                busqueda=busqueda,
                limit=limit,
                offset=0
            )
            
        except Exception as e:
            print(f"Error en búsqueda tiempo real: {str(e)}")
            return []