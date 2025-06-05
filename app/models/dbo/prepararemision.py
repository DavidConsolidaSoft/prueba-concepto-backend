# Generado automáticamente
# Tabla: dbo.PreparaRemision
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Prepararemision(Base):
    __tablename__ = "PreparaRemision"
    __table_args__ = {"schema": "dbo"}

    PreparaRemision = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    Prioridad = Column(Integer)
    fecha = Column(DateTime)
    cambodega = Column(Integer)
    bodeguero = Column(Integer)
    rupStatus = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)
    notas = Column(String(250))

    def __repr__(self):
        return "<Prepararemision(PreparaRemision={self.PreparaRemision})>"