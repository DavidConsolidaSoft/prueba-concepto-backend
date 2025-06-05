# Generado automáticamente
# Tabla: dbo.miscompras
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Miscompras(Base):
    __tablename__ = "miscompras"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    TipoCompra = Column(String(255))
    dia = Column(DateTime)
    CodigoProveedor = Column(Integer)
    CodigoProducto = Column(String(25))
    Producto = Column(String(255))
    Propio = Column(String(6))
    Presentacion = Column(String(100))
    Factor = Column(Numeric(18, 6))
    Bodega = Column(String(100))
    Lote = Column(String(40))
    CantidadCompra = Column(Numeric(18, 6))
    DevolucionCompra = Column(Numeric(18, 6))
    Bonificacion = Column(Numeric(18, 6))
    DevolucionBonificacion = Column(Numeric(18, 6))
    idKardex = Column(Integer)
    CompraNeta = Column(Numeric(18, 6))
    CompraBruta = Column(Numeric(18, 6))
    Factor1 = Column(Numeric(18, 6))
    Factor2 = Column(Numeric(18, 6))
    Factor3 = Column(Numeric(18, 6))
    NCxPrecio = Column(Numeric(18, 6))
    PrecioCompra = Column(Numeric(18, 6))
    EncargadoCompra = Column(String(50))
    TipoProveedor = Column(String(100))
    Registro = Column(String(30))
    Proveedor = Column(String(150))
    Plazo = Column(Integer)
    CompraContado = Column(Boolean)
    Pais = Column(String(80))
    Departamento = Column(String(90))
    Municipio = Column(String(90))
    TipoProducto = Column(String(90))
    CasaProducto = Column(String(90))
    CategoriaProducto = Column(String(90))
    gastos = Column(Numeric(18, 6))
    aranceles = Column(Numeric(18, 6))
    OtrosValores = Column(Numeric(18, 6))
    CostoCompra = Column(Numeric(18, 6))
    costoPromedio = Column(Numeric(18, 6))
    fecvence = Column(DateTime)
    empresa = Column(String(55))
    fechadesde = Column(DateTime)
    fechaHasta = Column(DateTime)
    CostoUnitarioCompra = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Miscompras(TipoCompra={self.TipoCompra})>"