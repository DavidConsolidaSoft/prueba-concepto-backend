# Generado automáticamente
# Tabla: dbo.ProductoUnidadVenta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Productounidadventa(Base):
    __tablename__ = "ProductoUnidadVenta"
    __table_args__ = {"schema": "dbo"}

    Producto = Column(Integer, nullable=False)
    UnidadVenta = Column(Integer, nullable=False)
    Factor = Column(Numeric(16, 6), nullable=False)
    Preferido = Column(Boolean, nullable=False)
    Activo = Column(Boolean, nullable=False)
    ProductoUnidadVenta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    Precio = Column(Numeric(16, 6), nullable=False)

    def __repr__(self):
        return "<Productounidadventa(ProductoUnidadVenta={self.ProductoUnidadVenta})>"