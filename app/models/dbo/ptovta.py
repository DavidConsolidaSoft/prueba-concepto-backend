# Generado automáticamente
# Tabla: dbo.ptovta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Ptovta(Base):
    __tablename__ = "ptovta"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    nptovta = Column(String(25), nullable=False)
    nota = Column(String(250), nullable=False)
    ptovta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Ptovta(ptovta={self.ptovta})>"