# Generado automáticamente
# Tabla: dbo.misVentas
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Misventas(Base):
    __tablename__ = "misVentas"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    tipoVenta = Column(String(40))
    dia = Column(DateTime)
    codigoCliente = Column(String(25))
    TipoCliente = Column(String(200))
    Cliente = Column(String(100))
    Registro = Column(String(15))
    Pais = Column(String(30))
    Sucursal = Column(String(50))
    Departamento = Column(String(50))
    Provincia_Municipio = Column(String(50))
    tipovendedor = Column(String(40))
    CodigoVendedor = Column(Integer)
    Vendedor = Column(String(50))
    CodigoProducto = Column(String(25))
    Producto = Column(String(100))
    ProductoPropio = Column(String(10))
    TipoProducto = Column(String(40))
    PresentacionProducto = Column(String(40))
    FactorPresentacionProducto = Column(Numeric(18, 6))
    CategoriaProducto = Column(String(40))
    CasaProducto = Column(String(35))
    Bodega = Column(String(50))
    loteProducto = Column(String(20))
    diasCredito = Column(Numeric(18, 6))
    condicionPago = Column(String(50))
    FormaPago = Column(String(15))
    Unidadvendida = Column(Numeric(18, 6))
    UnidadDevolucion = Column(Numeric(18, 6))
    Unidadbonificada = Column(Numeric(18, 6))
    UnidadDevolucionBonificada = Column(Numeric(18, 6))
    ventaNeta = Column(Numeric(18, 6))
    ventaNetaDevolucion = Column(Numeric(18, 6))
    ImpuestoVenta = Column(Numeric(18, 6))
    ImpuestoVentaDevolucion = Column(Numeric(18, 6))
    NotaCreditoxPrecio = Column(Numeric(18, 6))
    VentaNeta_NCPrecio = Column(Numeric(18, 6))
    CostoUnitarioVenta = Column(Numeric(18, 6))
    PrecioVenta = Column(Numeric(18, 6))
    ListaPrecios = Column(String(50))
    NumeroDocumento = Column(String(9))
    existencia = Column(Numeric(18, 6))
    lotevence = Column(DateTime)
    unidadGratificada = Column(Numeric(18, 6))
    descuentoGratificado = Column(Numeric(18, 6))
    descuento = Column(Numeric(18, 6))
    unidadBonificadaProveedor = Column(Numeric(18, 6))
    descuentoProveedor = Column(Numeric(18, 6))
    fechadesde = Column(DateTime)
    fechahasta = Column(DateTime)
    VentaBruta = Column(Numeric(18, 6))
    VentaBonficada = Column(Numeric(18, 6))
    VentaGratificada = Column(Numeric(18, 6))
    VentaBonificadaProveedor = Column(Numeric(18, 6))
    direccion = Column(String(200))
    razonsocial = Column(String(50))
    propietario = Column(String(50))
    nit = Column(String(20))
    telefono = Column(String(25))
    empresa = Column(String(55))
    Conglomerado = Column(String(35))
    costoventa = Column(Numeric(18, 6), nullable=False)
    Margenventa = Column(Numeric(18, 6), nullable=False)
    PrecioFinalventa = Column(Numeric(18, 6), nullable=False)
    kardex = Column(Integer, nullable=False)
    exhibidor = Column(String(50))

    def __repr__(self):
        return "<Misventas(tipoVenta={self.tipoVenta})>"