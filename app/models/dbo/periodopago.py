# Generado automáticamente
# Tabla: dbo.periodoPago
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Periodopago(Base):
    __tablename__ = "periodoPago"
    __table_args__ = {"schema": "dbo"}

    dia = Column(Integer)
    empresa = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    periodoPago = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Periodopago(periodoPago={self.periodoPago})>"