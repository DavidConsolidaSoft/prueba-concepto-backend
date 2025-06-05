# Generado automáticamente
# Tabla: dbo.RangoCliente
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Rangocliente(Base):
    __tablename__ = "RangoCliente"
    __table_args__ = {"schema": "dbo"}

    nRangoCliente = Column(String(25), nullable=False)
    RangoCliente = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Rangocliente(nRangoCliente={self.nRangoCliente})>"