# Generado automáticamente
# Tabla: dbo.detallecotizacion
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Detallecotizacion(Base):
    __tablename__ = "detallecotizacion"
    __table_args__ = {"schema": "dbo"}

    cotizacion = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    precio = Column(Numeric(16, 6), nullable=False)
    aceptado = Column(Boolean, nullable=False)
    entregado = Column(Boolean, nullable=False)
    comprado = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    fechaentrega = Column(DateTime)
    precioentrega = Column(Numeric(16, 6), nullable=False)
    detallecotizacion = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Detallecotizacion(detallecotizacion={self.detallecotizacion})>"