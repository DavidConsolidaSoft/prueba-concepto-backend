# Generado automáticamente
# Tabla: dbo.tipogasto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipogasto(Base):
    __tablename__ = "tipogasto"
    __table_args__ = {"schema": "dbo"}

    ntipogasto = Column(String(50), nullable=False)
    tipogasto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Tipogasto(tipogasto={self.tipogasto})>"