from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, func, case
from datetime import datetime, timedelta
from app.models.facturacion.factura_lista_models import (
    FacturaListItem, 
    FacturaDetalle, 
    DetalleProducto
)
import logging
import re

logger = logging.getLogger(__name__)

class FacturaServiceSimpleORM:
    def __init__(self, db: Session):
        self.db = db
        # Deshabilitar la carga automática de relaciones
        self.db.autoflush = False
        
    def _normalize_search_term(self, search_term: str) -> str:
        """
        Normaliza el término de búsqueda eliminando espacios extra,
        caracteres especiales y convirtiendo a minúsculas.
        """
        if not search_term:
            return ""
        
        # Eliminar espacios al inicio y final, convertir a minúsculas
        normalized = search_term.strip().lower()
        
        # Eliminar espacios múltiples y dejar solo uno
        normalized = re.sub(r'\s+', ' ', normalized)
        
        # Log para debugging
        if search_term != normalized:
            logger.debug(f"Término normalizado: '{search_term}' -> '{normalized}'")
        
        return normalized
    
    def get_facturas_list(
        self,
        empresa: int,
        fecha_inicio: datetime,
        fecha_fin: datetime,
        cliente: Optional[str] = None,
        pedido: Optional[str] = None,
        caja: Optional[str] = None,
        solo_sin_imprimir: bool = False,
        orden: int = 1,
        psat_tipo: int = 0,
        moneda: int = 1,
        search: Optional[str] = None,
        skip: int = 0,
        limit: int = 100,
        count_only: bool = False
    ) -> tuple[List[FacturaListItem], int]:
        """
        Obtiene la lista de facturas usando ORM sin relaciones automáticas
        MEJORADO: Con búsqueda optimizada y paginación
        """
        try:
            # Normalizar término de búsqueda
            search_normalized = self._normalize_search_term(search) if search else None
            
            logger.info(f"Obteniendo facturas para empresa={empresa}, búsqueda='{search_normalized}', skip={skip}, limit={limit}")
            
            # Importar modelos localmente
            from app.models.dbo.factura import Factura
            from app.models.dbo.tipomov import TipoMov
            from app.models.dbo.clientes import Clientes
            from app.models.dbo.vendedor import Vendedor
            from app.models.dbo.caja import Caja
            from app.models.dbo.factelec import FactElec
            from app.models.dbo.factcont import FactCont
            from app.models.dbo.municip import Municip
            from app.models.dbo.depto import Depto
            from app.models.dbo.tipcli import TipCli
            from app.models.dbo.condpago import CondPago
            from app.models.dbo.tipovta import TipoVta
            from app.models.dbo.usuario import Usuario
            from sqlalchemy import case, literal, cast, String, func, and_, or_
            
            # Preparar subqueries para factura electrónica
            sello_subquery = None
            doc_subquery = None
            
            if psat_tipo in [1, 2]:  # FEL
                sello_subquery = self.db.query(
                    literal('*FEL*')
                ).filter(
                    FactElec.factura == Factura.factura
                ).scalar_subquery()
                
                doc_subquery = sello_subquery
            elif psat_tipo == 3:  # DTE
                sello_subquery = self.db.query(
                    case(
                        (FactElec.sellorecibido.isnot(None), literal('*DTE')),
                        else_=literal('-SS-')
                    )
                ).filter(
                    FactElec.factura == Factura.factura
                ).scalar_subquery()
                
                doc_subquery = self.db.query(
                    FactElec.uuid
                ).filter(
                    FactElec.factura == Factura.factura
                ).scalar_subquery()
            
            # Construir la columna numedocu dependiendo de si hay sello
            if sello_subquery is not None:
                numedocu_col = func.concat(sello_subquery, ' ', Factura.numedocu).label('numedocu')
            else:
                numedocu_col = Factura.numedocu.label('numedocu')
            
            # Construir la columna referencia dependiendo de si hay doc_subquery
            if doc_subquery is not None:
                referencia_col = doc_subquery.label('referencia')
            else:
                referencia_col = literal('').label('referencia')
            
            # Subqueries para clientes de contado
            nclientes_contado_subq = self.db.query(
                FactCont.nclientes
            ).filter(
                FactCont.factura == Factura.factura
            ).scalar_subquery()
            
            registro_contado_subq = self.db.query(
                FactCont.registro
            ).filter(
                FactCont.factura == Factura.factura
            ).scalar_subquery()
            
            nmunicipio_contado_subq = self.db.query(
                FactCont.nmunicip
            ).filter(
                FactCont.factura == Factura.factura
            ).scalar_subquery()
            
            telefono_contado_subq = self.db.query(
                FactCont.telefono
            ).filter(
                FactCont.factura == Factura.factura
            ).scalar_subquery()
            
            # Query base con todas las columnas necesarias
            query = self.db.query(
                Factura.pedido,
                TipoMov.ntipomov,
                numedocu_col,
                Factura.fecha,
                # Símbolo de moneda (SM en el query original)
                case(
                    (Factura.moneda == moneda, literal('$')),
                    else_=literal('Q')
                ).label('sm'),
                Factura.montfact,
                Factura.impresa,
                Factura.nula,
                Factura.clientes,
                # Manejo especial para clientes de contado
                case(
                    (Clientes.contado == 1, nclientes_contado_subq),
                    else_=Clientes.nclientes
                ).label('nclientes'),
                case(
                    (Clientes.contado == 1, registro_contado_subq),
                    else_=Clientes.registro
                ).label('registro'),
                Factura.tasacambio.label('ts'),
                Factura.tasacambioseg.label('ts2'),
                Factura.tasacambiotres.label('ts3'),
                Depto.ndepto,
                case(
                    ((Clientes.contado == 1) & (nclientes_contado_subq.isnot(None)), 
                    nmunicipio_contado_subq),
                    else_=Municip.nmunicip
                ).label('nmunicipio'),
                case(
                    ((Clientes.contado == 1) & (telefono_contado_subq.isnot(None)), 
                    telefono_contado_subq),
                    else_=Clientes.telefono1
                ).label('telefono1'),
                Factura.factura,
                Factura.caja,
                Caja.ncaja.label('n'),
                Factura.efectivo,
                Factura.tipomov,
                TipoVta.ntipovta,
                Factura.estado,
                case(
                    (Factura.estado == 0, 'sin estado'),
                    (Factura.estado == 1, 'Preparar'),
                    (Factura.estado == 2, 'Terminado'),
                    (Factura.estado == 3, 'Cancelado'),
                    (Factura.estado == 4, 'Dar Prioridad'),
                    else_='Preparando'
                ).label('estatus'),
                Usuario.nusuario.label('usuario'),
                Vendedor.nvendedor,
                TipCli.ntipcli,
                CondPago.ncondpago,
                case(
                    ((Factura.facturaReferencia == 0) & (Factura.nula == 0), 0),
                    else_=1
                ).label('si'),
                Factura.notas,
                Factura.horatiempo.label('hora'),
                (Factura.afecta + Factura.exenta).label('neto'),
                Factura.propina,
                Factura.percepcion,
                Factura.retencion,
                referencia_col
            )
            
            # Joins manuales específicos
            query = query.join(
                TipoMov,
                TipoMov.tipomov == Factura.tipomov
            ).outerjoin(
                Clientes,
                and_(
                    Clientes.clientes == Factura.clientes,
                    Clientes.empresa == empresa
                )
            ).outerjoin(
                Municip,
                Clientes.municip == Municip.municip
            ).outerjoin(
                Depto,
                Municip.depto == Depto.depto
            ).outerjoin(
                Vendedor,
                Factura.vendedor == Vendedor.vendedor
            ).outerjoin(
                Caja,
                and_(
                    Factura.caja == Caja.caja,
                    Caja.empresa == empresa
                )
            ).outerjoin(
                TipoVta,
                Factura.tipovta == TipoVta.tipovta
            ).outerjoin(
                Usuario,
                Factura.usuario == Usuario.usuario
            ).outerjoin(
                TipCli,
                Clientes.tipcli == TipCli.tipcli
            ).outerjoin(
                CondPago,
                Factura.condpago == CondPago.condpago
            )
            
            # Filtros base
            query = query.filter(
                Factura.empresa == empresa,
                TipoMov.factura == 1,
                TipoMov.ANTICIPO == 0,
                TipoMov.notacred == 0,
                Factura.fecha >= fecha_inicio,
                Factura.fecha <= fecha_fin
            )
            
            # NUEVO: Aplicar búsqueda mejorada si hay término
            if search_normalized and len(search_normalized) >= 2:
                search_words = search_normalized.split()
                search_conditions = []
                
                for word in search_words:
                    word_pattern = f"%{word}%"
                    word_conditions = or_(
                        # Buscar en nombre del cliente
                        and_(Clientes.nclientes.isnot(None), func.lower(Clientes.nclientes).like(word_pattern)),
                        # Buscar en código del cliente
                        and_(Clientes.clientes.isnot(None), func.lower(Clientes.clientes).like(word_pattern)),
                        # Buscar en número de documento/factura
                        and_(Factura.numedocu.isnot(None), func.lower(Factura.numedocu).like(word_pattern)),
                        # Buscar en pedido
                        and_(Factura.pedido.isnot(None), func.lower(Factura.pedido).like(word_pattern)),
                        # Buscar en nombre del vendedor
                        and_(Vendedor.nvendedor.isnot(None), func.lower(Vendedor.nvendedor).like(word_pattern)),
                        # Buscar en notas
                        and_(Factura.notas.isnot(None), func.lower(Factura.notas).like(word_pattern)),
                        # Buscar en clientes de contado
                        and_(nclientes_contado_subq.isnot(None), func.lower(nclientes_contado_subq).like(word_pattern))
                    )
                    search_conditions.append(word_conditions)
                
                # Aplicar condiciones de búsqueda
                if len(search_conditions) > 1:
                    query = query.filter(and_(*search_conditions))
                elif len(search_conditions) == 1:
                    query = query.filter(search_conditions[0])
                
                logger.debug(f"Aplicando búsqueda con {len(search_words)} palabra(s): {search_words}")
            
            # Aplicar filtros opcionales originales
            if cliente:
                cliente_pattern = f"%{cliente}%"
                query = query.filter(
                    or_(
                        Clientes.nclientes.like(cliente_pattern),
                        Clientes.clientes.like(cliente_pattern),
                        Clientes.registro.like(cliente_pattern)
                    )
                )
            
            if pedido:
                pedido_pattern = f"%{pedido}%"
                query = query.filter(
                    or_(
                        Factura.pedido.like(pedido_pattern),
                        Factura.numedocu.like(pedido_pattern)
                    )
                )
            
            if caja and caja != '%':
                query = query.filter(Factura.caja.like(f"%{caja}%"))
            
            if solo_sin_imprimir:
                query = query.filter(
                    Factura.impresa == 0,
                    Factura.nula == 0
                )
            
            # Obtener conteo total
            total = query.count()
            logger.info(f"Total de facturas encontradas: {total}")
            
            # Si solo queremos el conteo, retornamos temprano
            if count_only:
                return [], total
            
            # Aplicar ordenamiento según el parámetro
            if orden == 2:
                query = query.order_by(
                    Factura.fecha.desc(),
                    TipoMov.ntipomov,
                    Factura.numedocu.desc()
                )
            elif orden == 3:
                query = query.order_by(
                    Vendedor.nvendedor,
                    Factura.fecha.desc(),
                    TipoMov.ntipomov,
                    Factura.numedocu.desc()
                )
            elif orden == 4:
                query = query.order_by(
                    TipCli.ntipcli,
                    Factura.fecha.desc(),
                    TipoMov.ntipomov,
                    Factura.numedocu.desc()
                )
            elif orden == 6:
                query = query.order_by(
                    Clientes.nclientes,
                    Factura.fecha.desc(),
                    TipoMov.ntipomov,
                    Factura.numedocu.desc()
                )
            elif orden == 1:
                query = query.order_by(
                    Factura.fecha.desc(),  # Ordenar por fecha simple
                    TipoMov.ntipomov,
                    Factura.numedocu.desc()
                )
            else:
                query = query.order_by(Factura.pedido.desc())
            
            # NUEVO: Aplicar paginación
            if limit > 0:
                query = query.offset(skip).limit(limit)
            
            # Ejecutar query
            results = query.all()
            logger.info(f"Obtenidas {len(results)} facturas después de aplicar paginación")
            
            # Convertir resultados (el código de conversión permanece igual)
            facturas = []
            for row in results:
                # Extraer los valores del row
                pedido = row.pedido
                ntipomov = row.ntipomov
                numedocu = row.numedocu
                fecha = row.fecha
                sm = row.sm
                montfact = row.montfact
                impresa = row.impresa
                nula = row.nula
                clientes = row.clientes
                nclientes = row.nclientes
                registro = row.registro
                ts = row.ts
                ts2 = row.ts2
                ts3 = row.ts3
                ndepto = row.ndepto
                nmunicipio = row.nmunicipio
                telefono1 = row.telefono1
                factura_id = row.factura
                caja = row.caja
                ncaja = row.n
                efectivo = row.efectivo
                tipomov = row.tipomov
                ntipovta = row.ntipovta
                estado_original = row.estado  # Estado original de la BD
                estatus = row.estatus  # Estado de proceso
                usuario = row.usuario
                nvendedor = row.nvendedor
                ntipcli = row.ntipcli
                ncondpago = row.ncondpago
                si = row.si
                notas = row.notas
                hora_datetime = row.hora  # Este es el datetime completo
                neto = row.neto
                propina = row.propina
                percepcion = row.percepcion
                retencion = row.retencion
                referencia = row.referencia
                
                # Formatear hora
                hora = hora_datetime.strftime('%H:%M:%S') if hora_datetime else ''
                
                # Determinar estado basado en tu lógica
                if nula:
                    estado_texto = 'Nula'
                elif not impresa:
                    estado_texto = 'Abierta'
                else:
                    estado_texto = 'Cerrada'
                
                # Limpiar nombres de espacios
                nombre_cliente_limpio = (nclientes or '').strip()
                nombre_vendedor_limpio = (nvendedor or '').strip()
                
                factura = FacturaListItem(
                    empresa=empresa,
                    factura=factura_id,
                    numedocu=numedocu,
                    fecha=fecha,
                    nombre_cliente=nombre_cliente_limpio,
                    nombre_vendedor=nombre_vendedor_limpio,
                    monto_total=float(montfact or 0),
                    estado=estado_texto,
                    impresa=bool(impresa),
                    nula=bool(nula),
                    pedido=pedido,
                    tipo_movimiento=ntipomov,
                    codigo_cliente=clientes,
                    registro=registro,
                    nit=registro,
                    dui=registro,  # En el SQL original usa registro para todo
                    vendedor_codigo=None,  # No está en el query original
                    tasa_cambio=float(ts or 0),
                    tasa_cambio_seg=float(ts2 or 0),
                    tasa_cambio_tres=float(ts3 or 0),
                    caja=ncaja,
                    estado_codigo=estado_original,  # Estado original de la BD
                    estado_proceso=estatus,  # Estado de preparación (texto)
                    notas=notas,
                    hora=hora or '',
                    neto=float(neto or 0),
                    propina=float(propina or 0),
                    percepcion=float(percepcion or 0),
                    retencion=float(retencion or 0),
                    # Campos adicionales del query original
                    depto=ndepto,
                    municipio=nmunicipio,
                    telefono=telefono1,
                    efectivo=efectivo,
                    tipo_venta=ntipovta,
                    usuario=usuario,
                    tipo_cliente=ntipcli,
                    condicion_pago=ncondpago,
                    factura_referencia=bool(si),
                    tipo_moneda=sm,
                    factura_electronica_ref=referencia
                )
                facturas.append(factura)
            
            logger.info(f"Retornando {len(facturas)} facturas procesadas")
            return facturas, total
            
        except Exception as e:
            logger.error(f"Error al obtener facturas: {str(e)}", exc_info=True)
            return [], 0
        
    def search_facturas_optimized(
        self, 
        empresa: int,
        search_term: str,
        fecha_inicio: datetime,
        fecha_fin: datetime,
        limit: int = 20
    ) -> List[FacturaListItem]:
        """
        Búsqueda optimizada de facturas para autocompletado.
        """
        try:
            search_normalized = self._normalize_search_term(search_term)
            
            if not search_normalized or len(search_normalized) < 2:
                logger.debug(f"Término de búsqueda muy corto: '{search_term}'")
                return []
            
            logger.debug(f"Búsqueda optimizada de facturas: '{search_normalized}' (empresa: {empresa})")
            
            # Usar el método principal mejorado
            facturas, total = self.get_facturas_list(
                empresa=empresa,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                search=search_normalized,
                skip=0,
                limit=limit
            )
            
            logger.debug(f"Búsqueda de facturas devolvió {len(facturas)} resultados de {total} totales")
            return facturas
            
        except Exception as e:
            logger.error(f"Error en búsqueda optimizada de facturas: {str(e)}", exc_info=True)
            return []
    
    def get_factura_detalle(self, factura_id: int, empresa: int) -> Optional[FacturaDetalle]:
        """
        Obtiene el detalle completo de una factura específica
        """
        from app.models.dbo.factura import Factura
        from app.models.dbo.tipomov import TipoMov
        from app.models.dbo.clientes import Clientes
        from app.models.dbo.vendedor import Vendedor
        from app.models.dbo.caja import Caja
        from app.models.dbo.bodega import Bodega
        from app.models.dbo.condpago import CondPago
        from app.models.dbo.tipcli import TipCli
        from app.models.dbo.moneda import Moneda
        from app.models.dbo.dfactura import DFactura
        from app.models.dbo.producto import Producto
        from app.models.dbo.tipoprod import TipoProd
        from app.models.dbo.kardex import Kardex
        from app.models.dbo.lote import Lote
        from app.models.dbo.umedida import UMedida
        
        # Query para obtener datos de la factura  
        factura_query = self.db.query(
            Factura,
            TipoMov.ntipomov,
            Clientes.nclientes,
            Clientes.direccion,
            Clientes.telefono1,
            Clientes.nit,
            Clientes.dui,
            Clientes.registro,
            Clientes.giro,
            Vendedor.nvendedor,
            Caja.ncaja,
            Bodega.nbodega,
            CondPago.ncondpago,
            CondPago.contado,
            CondPago.plazo,
            TipCli.ntipcli,
            Moneda.nmoneda
        ).join(
            TipoMov, Factura.tipomov == TipoMov.tipomov
        ).outerjoin(
            Clientes, and_(
                Factura.clientes == Clientes.clientes,
                Clientes.empresa == empresa
            )
        ).outerjoin(
            Vendedor, Factura.vendedor == Vendedor.vendedor
        ).outerjoin(
            Caja, and_(
                Factura.caja == Caja.caja,
                Caja.empresa == empresa
            )
        ).outerjoin(
            Bodega, and_(
                Factura.bodega == Bodega.bodega,
                Bodega.empresa == empresa
            )
        ).outerjoin(
            CondPago, Factura.condpago == CondPago.condpago
        ).outerjoin(
            TipCli, Clientes.tipcli == TipCli.tipcli
        ).outerjoin(
            Moneda, Factura.moneda == Moneda.moneda
        ).filter(
            Factura.factura == factura_id,
            Factura.empresa == empresa
        ).first()
        
        if not factura_query:
            return None
        
        # Desempaquetar resultados
        (factura_obj, ntipomov, nclientes, direccion, telefono1, nit, dui, 
         registro, giro, nvendedor, ncaja, nbodega, ncondpago, contado, 
         plazo, ntipcli, nmoneda) = factura_query
        
        # Determinar estado
        if factura_obj.nula:
            estado = 'Nula'
        elif not factura_obj.impresa:
            estado = 'Abierta'
        else:
            estado = 'Cerrada'
        
        # Determinar tipo de pago
        tipo_pago = 'Contado' if contado else 'Crédito'
        
        # Calcular totales
        subtotal = float((factura_obj.afecta or 0) + (factura_obj.exenta or 0))
        
        # Calcular saldo disponible y deudas del cliente
        saldo_disponible = 0.0
        vencidas = 0
        monto_adeudado = 0.0
        
        # Query para obtener información crediticia del cliente
        if factura_obj.clientes:
            # Obtener el límite de crédito del cliente
            cliente_info = self.db.query(
                Clientes.limitecredito,
                Clientes.saldo
            ).filter(
                Clientes.clientes == factura_obj.clientes,
                Clientes.empresa == empresa
            ).first()
            
            if cliente_info:
                limite_credito = float(cliente_info.limitecredito or 0)
                
                # Obtener el ID de condición de pago de contado para excluirlas
                condpago_contado = self.db.query(CondPago.condpago).filter(
                    CondPago.contado == 1,
                    CondPago.empresa == empresa
                ).all()
                condpago_contado_ids = [cp.condpago for cp in condpago_contado]
                
                # Calcular el total adeudado por el cliente (solo facturas a crédito)
                facturas_pendientes = self.db.query(
                    func.sum(Factura.montfact).label('total_adeudado'),
                    func.count(Factura.factura).label('cantidad_vencidas')
                ).filter(
                    Factura.clientes == factura_obj.clientes,
                    Factura.empresa == empresa,
                    Factura.nula == 0,
                    Factura.cancelada == 0,
                    ~Factura.condpago.in_(condpago_contado_ids)  # Excluir facturas de contado
                ).filter(
                    or_(
                        Factura.estado == 0,  # Facturas pendientes
                        and_(
                            Factura.estado != 0,
                            Factura.fecha < datetime.now() - timedelta(days=plazo if plazo else 30)
                        )
                    )
                ).first()
                
                if facturas_pendientes:
                    monto_adeudado = float(facturas_pendientes.total_adeudado or 0)
                    vencidas = int(facturas_pendientes.cantidad_vencidas or 0)
                    
                # Calcular saldo disponible
                saldo_disponible = limite_credito - monto_adeudado
        
        # Query para obtener los productos - basado en el query del sistema legacy
        productos_query = self.db.query(
            DFactura,
            TipoProd.ntipoprod,
            Producto.icdbarra,
            Producto.nproducto,
            Producto.codbarra,
            Producto.exento,
            Producto.servicios,
            Producto.parte,
            Producto.peso,
            Producto.nosujeto,
            Producto.condicion1,
            Producto.recargo,
            Kardex.producto,
            Lote.nolote,
            Lote.fecvence,
            Bodega.nbodega,
            UMedida.numedida,
            UMedida.factor
        ).join(
            Kardex, DFactura.kardex == Kardex.kardex
        ).join(
            Producto, Kardex.producto == Producto.producto
        ).join(
            TipoProd, Producto.tipoprod == TipoProd.tipoprod
        ).outerjoin(
            Lote, Kardex.lote == Lote.lote
        ).outerjoin(
            UMedida, Producto.umedida == UMedida.umedida
        ).outerjoin(
            Bodega, and_(
                Kardex.bodega == Bodega.bodega,
                Bodega.empresa == empresa
            )
        ).filter(
            DFactura.factura == factura_id,
            DFactura.empresa == empresa,
            DFactura.preciolista == 0  # Del query legacy
        ).order_by(
            DFactura.dfactura
        ).all()
        
        # Convertir productos
        productos = []
        for row in productos_query:
            (dfactura_obj, ntipoprod, icdbarra, nproducto, codbarra, exento,
             servicios, parte, peso, nosujeto, condicion1, recargo, producto_id,
             nolote, fecvence, nbodega, numedida, factor) = row
            
            # Construir nombre del producto con el prefijo (Ex) si es exento
            nombre_producto = f"{'(Ex) ' if exento else ''}{nproducto or ''}"
            
            # Usar el nombre del campo DFactura si está disponible
            if dfactura_obj.nombre:
                nombre_producto = dfactura_obj.nombre
                
            # Calcular valores del producto
            cantidad = float(dfactura_obj.cantidad or 0)
            precio = float(dfactura_obj.precio or 0)
            descuento_porcentaje = float(dfactura_obj.pdesc or 0)
            
            # Cálculos del detalle según el query legacy
            subtotal_prod = cantidad * precio
            descuento_valor = float(dfactura_obj.vdesc or 0)
            
            # Si hay afecta y montfact, calcular descuento proporcional
            if dfactura_obj.afecta and dfactura_obj.montfact and dfactura_obj.montfact != 0:
                yvdesc = round(dfactura_obj.vdesc * dfactura_obj.afecta / dfactura_obj.montfact, 2)
            else:
                yvdesc = dfactura_obj.vdesc
            
            # Usar valores del modelo DFactura
            afecta = float(dfactura_obj.afecta or 0)
            exenta = float(dfactura_obj.exenta or 0)
            viva = float(dfactura_obj.viva or 0)
            montfact = float(dfactura_obj.montfact or 0)
            
            producto = DetalleProducto(
                dfactura=dfactura_obj.dfactura,
                factura=factura_id,
                producto=producto_id,
                codigo_producto=codbarra,
                nombre_producto=nombre_producto,
                tipo_producto=ntipoprod or '',
                bodega=nbodega or '',
                lote=nolote,
                cantidad=cantidad,
                bonificado=float(dfactura_obj.bonificado or 0),
                precio=precio,
                descuento_porcentaje=descuento_porcentaje,
                descuento_valor=descuento_valor,
                subtotal=afecta + exenta,  # Del query legacy
                iva=viva,
                total=montfact,
                exento=bool(exento),
                servicio=bool(servicios),
                linea=dfactura_obj.linea,
                gratificado=float(dfactura_obj.gratificado or 0),
                reservado=float(dfactura_obj.reservado or 0),
                costo=float(dfactura_obj.costo or 0)
            )
            productos.append(producto)
        
        # Crear objeto FacturaDetalle
        factura_detalle = FacturaDetalle(
            factura=factura_id,
            numedocu=factura_obj.numedocu,
            tipo_documento=ntipomov or '',
            estado=estado,
            fecha=factura_obj.fecha,
            codigo_cliente=factura_obj.clientes,
            nombre_cliente=nclientes or '',
            tipo_cliente=ntipcli or '',
            direccion=direccion,
            telefono=telefono1,
            nit=nit or '',
            dui=dui or '',
            registro=registro or '',
            giro=giro,
            codigo_vendedor=factura_obj.vendedor,
            nombre_vendedor=nvendedor or '',
            forma_pago=ncondpago or '',
            tipo_pago=tipo_pago,
            plazo=plazo or 0,
            subtotal=subtotal,
            descuento_aplicado=float(factura_obj.vdesc or 0),
            descuento_porcentaje=float(factura_obj.pdesc or 0),
            iva=float(factura_obj.viva or 0),
            percepcion=float(factura_obj.percepcion or 0),
            retencion=float(factura_obj.retencion or 0),
            propina=float(factura_obj.propina or 0),
            total_pagar=float(factura_obj.montfact or 0),
            saldo_disponible=saldo_disponible,
            vencidas=vencidas,
            monto_adeudado=monto_adeudado,
            bodega=nbodega,
            caja=ncaja,
            notas=factura_obj.notas or '',
            empresa=empresa,
            moneda=nmoneda or '',
            tasa_cambio=float(factura_obj.tasacambio or 1),
            productos=productos
        )
        
        return factura_detalle