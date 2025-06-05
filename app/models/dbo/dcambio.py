# Generado automáticamente
# Tabla: dbo.dcambio
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dcambio(Base):
    __tablename__ = "dcambio"
    __table_args__ = {"schema": "dbo"}

    cambio = Column(Numeric(18, 6))
    cambio2 = Column(Numeric(18, 6))
    fecha = Column(DateTime)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    dcambio = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Dcambio(dcambio={self.dcambio})>"