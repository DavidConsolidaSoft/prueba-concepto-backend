# app/models/facturacion/factura_lista_models.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class FacturaListItem(BaseModel):
    """Modelo simplificado para la lista de facturas"""
    empresa: int
    factura: int
    numedocu: str
    fecha: datetime
    nombre_cliente: str
    nombre_vendedor: str
    monto_total: float
    estado: str  # "Abierta", "Cerrada", "Nula" - basado en impresa y nula
    impresa: bool
    nula: bool
    
    # Campos adicionales del query completo
    pedido: Optional[str] = None
    tipo_movimiento: Optional[str] = None
    codigo_cliente: Optional[str] = None
    registro: Optional[str] = None
    nit: Optional[str] = None
    dui: Optional[str] = None
    vendedor_codigo: Optional[int] = None
    tasa_cambio: float = 0
    tasa_cambio_seg: float = 0
    tasa_cambio_tres: float = 0
    caja: Optional[str] = None
    estado_codigo: int = 0  # Estado original de la base de datos
    estado_proceso: Optional[str] = None  # Descripción del estado del proceso (Preparar, Terminado, etc.)
    notas: Optional[str] = None
    hora: Optional[str] = None
    neto: float = 0
    propina: float = 0
    percepcion: float = 0
    retencion: float = 0
    es_contado: bool = False
    referencia: Optional[str] = None  # UUID o referencia de factura electrónica
    
    # Campos adicionales del query mejorado
    depto: Optional[str] = None  # Departamento
    municipio: Optional[str] = None  # Municipio
    telefono: Optional[str] = None  # Teléfono (puede venir de factcont)
    efectivo: Optional[float] = None  # Monto en efectivo
    tipo_venta: Optional[str] = None  # ntipovta
    usuario: Optional[str] = None  # Usuario que creó la factura
    tipo_cliente: Optional[str] = None  # ntipcli
    condicion_pago: Optional[str] = None  # ncondpago
    factura_referencia: bool = False  # Si tiene factura de referencia
    tipo_moneda: Optional[str] = None  # Símbolo de moneda ($, Q, etc.)
    factura_electronica_ref: Optional[str] = None  # Referencia FEL/DTE
    tipo_factura_electronica: Optional[str] = None  # FEL, DTE, o None
    sello_sat: Optional[str] = None  # Sello SAT si aplica
    estado_proceso: Optional[str] = None  # Descripción del estado del proceso (Preparar, Terminado, etc.)
    
    class Config:
        from_attributes = True

class FacturaListSimple(BaseModel):
    """Modelo mínimo para lista móvil/UI simple"""
    codigo_factura: str
    nombre_empresa: str
    nombre_vendedor: str
    total_factura: float
    fecha_factura: datetime
    estado_factura: str
    
    class Config:
        from_attributes = True

class ResumenDia(BaseModel):
    """Resumen de facturas por día"""
    fecha: datetime
    total_facturas: int
    monto_total: float
    facturas_impresas: int
    facturas_nulas: int
    
    class Config:
        from_attributes = True

# Mantener los modelos existentes para detalle
class DetalleProducto(BaseModel):
    """Modelo para el detalle de productos"""
    dfactura: int
    factura: int
    producto: int
    codigo_producto: str
    nombre_producto: str
    tipo_producto: str
    bodega: Optional[str]
    lote: Optional[str]
    cantidad: float
    bonificado: float = 0
    precio: float
    descuento_porcentaje: float = 0
    descuento_valor: float = 0
    subtotal: float
    iva: float = 0
    total: float
    exento: bool
    servicio: bool
    # Campos adicionales del detalle
    linea: Optional[int] = None
    gratificado: Optional[float] = 0
    reservado: Optional[float] = 0
    costo: Optional[float] = 0
    
    class Config:
        from_attributes = True

class FacturaDetalle(BaseModel):
    """Modelo para el detalle completo de la factura"""
    # Encabezado básico
    factura: int
    numedocu: str
    tipo_documento: str  # ntipomov
    estado: str  # Abierta/Cerrada/Nula
    fecha: datetime
    
    # Cliente
    codigo_cliente: str
    nombre_cliente: str
    tipo_cliente: str  # ntipcli
    direccion: Optional[str]
    telefono: Optional[str]
    nit: Optional[str]
    dui: Optional[str]
    registro: Optional[str]
    giro: Optional[str]
    
    # Vendedor
    codigo_vendedor: int
    nombre_vendedor: str
    
    # Información de pago
    forma_pago: str  # ncondpago
    tipo_pago: Optional[str]  # contado/crédito
    plazo: Optional[int] = 0
    
    # Totales y descuentos
    subtotal: float
    descuento_aplicado: float  # vdesc
    descuento_porcentaje: float  # pdesc
    iva: float
    percepcion: float = 0
    retencion: float = 0
    propina: float = 0
    total_pagar: float  # montfact
    
    # Información adicional
    saldo_disponible: float = 0  # Esto vendría de otro cálculo
    vencidas: int = 0  # Facturas vencidas del cliente
    monto_adeudado: float = 0  # Total adeudado del cliente
    
    # Otros datos
    bodega: Optional[str]
    caja: Optional[str]
    notas: Optional[str]
    empresa: int
    moneda: Optional[str]
    tasa_cambio: float = 1
    
    # Productos
    productos: List[DetalleProducto] = []
    
    class Config:
        from_attributes = True

# Nuevos modelos para soporte de facturación electrónica
class FacturaElectronicaInfo(BaseModel):
    """Información específica de facturación electrónica"""
    factura: int
    tipo: str  # FEL, DTE
    uuid: Optional[str] = None
    sello_recibido: Optional[str] = None
    fecha_certificacion: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# Modelo para filtros de búsqueda
class FiltrosBusquedaFactura(BaseModel):
    """Filtros disponibles para búsqueda de facturas"""
    fecha_inicio: datetime
    fecha_fin: datetime
    cliente: Optional[str] = None
    pedido: Optional[str] = None
    caja: Optional[str] = None
    solo_sin_imprimir: bool = False
    orden: int = 1  # 1-6 según las opciones del sistema
    tipo_sat: Optional[int] = None  # 0: normal, 1-2: FEL, 3: DTE
    moneda: Optional[int] = None
    vendedor: Optional[int] = None
    tipo_cliente: Optional[int] = None
    tipo_movimiento: Optional[int] = None
    
    class Config:
        from_attributes = True