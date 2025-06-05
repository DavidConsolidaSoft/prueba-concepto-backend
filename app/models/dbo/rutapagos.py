# Generado automáticamente
# Tabla: dbo.rutapagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Rutapagos(Base):
    __tablename__ = "rutapagos"
    __table_args__ = {"schema": "dbo"}

    rutapagos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    rutacobro = Column(Integer)
    pagos = Column(Integer)
    dpagos = Column(Integer)
    cambodega = Column(Integer)
    factura = Column(Integer)
    invcliente = Column(Integer)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Rutapagos(rutapagos={self.rutapagos})>"