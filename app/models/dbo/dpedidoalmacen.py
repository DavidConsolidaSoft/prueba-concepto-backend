# Generado automáticamente
# Tabla: dbo.dpedidoalmacen
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dpedidoalmacen(Base):
    __tablename__ = "dpedidoalmacen"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    producto = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    pedidoalmacen = Column(Integer, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    hcantidad = Column(Numeric(16, 6), nullable=False)
    cantidadsurtida = Column(Numeric(16, 6), nullable=False)
    hcantidadsurtida = Column(Numeric(16, 6), nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    dpedidoalmacen = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    PRECIO = Column(Numeric(18, 6), nullable=False)
    nula = Column(Boolean, nullable=False)
    nosuplir = Column(Boolean, nullable=False)
    entregado = Column(Boolean, nullable=False)

    # Relaciones
    # pedidoalmacen_rel = relationship("Pedidoalmacen", back_populates="dpedidoalmacen_set")  # Comentado automáticamente
    # producto_rel = relationship("Producto", back_populates="dpedidoalmacen_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dpedidoalmacen(dpedidoalmacen={self.dpedidoalmacen})>"