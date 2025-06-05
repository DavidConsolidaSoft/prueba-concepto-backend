# Generado automáticamente
# Tabla: dbo.mformprod
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Mformprod(Base):
    __tablename__ = "mformprod"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    mformula = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    mformprod = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    costo = Column(Boolean, nullable=False)
    tipogasto = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Mformprod(mformprod={self.mformprod})>"