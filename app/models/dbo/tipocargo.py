# Generado automáticamente
# Tabla: dbo.TipoCargo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipocargo(Base):
    __tablename__ = "TipoCargo"
    __table_args__ = {"schema": "dbo"}

    TipoCargo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nTipoCargo = Column(String(35))
    Naturaleza = Column(Integer)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    operador = Column(Integer)

    def __repr__(self):
        return "<Tipocargo(TipoCargo={self.TipoCargo})>"