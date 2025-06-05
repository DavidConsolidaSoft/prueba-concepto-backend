# Generado automáticamente
# Tabla: dbo.mformula
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Mformula(Base):
    __tablename__ = "mformula"
    __table_args__ = {"schema": "dbo"}

    nmformula = Column(String(50), nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    activo = Column(Boolean, nullable=False)
    producto = Column(Integer, nullable=False)
    pformula = Column(Integer, nullable=False)
    mformula = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Mformula(mformula={self.mformula})>"