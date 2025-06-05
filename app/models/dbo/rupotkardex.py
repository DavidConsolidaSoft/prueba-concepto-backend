# Generado automáticamente
# Tabla: dbo.rupotkardex
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Rupotkardex(Base):
    __tablename__ = "rupotkardex"
    __table_args__ = {"schema": "dbo"}

    rupot = Column(Integer, primary_key=True, nullable=False)
    kardex = Column(Integer, primary_key=True, nullable=False)
    cantidad = Column(Numeric(14, 6))
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Rupotkardex(rupot={self.rupot}, kardex={self.kardex})>"