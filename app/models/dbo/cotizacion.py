# Generado automáticamente
# Tabla: dbo.cotizacion
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Cotizacion(Base):
    __tablename__ = "cotizacion"
    __table_args__ = {"schema": "dbo"}

    proyecto = Column(Integer, nullable=False)
    cotizacion = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    proveedor = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)
    monto = Column(Numeric(16, 6), nullable=False)
    cprodprec = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    nula = Column(Boolean, nullable=False)
    fentrega = Column(DateTime)
    condpago = Column(Integer, nullable=False)
    garantia = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Cotizacion(cotizacion={self.cotizacion})>"