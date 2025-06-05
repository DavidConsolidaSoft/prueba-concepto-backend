# Generado automáticamente
# Tabla: dbo.formulataller
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Formulataller(Base):
    __tablename__ = "formulataller"
    __table_args__ = {"schema": "dbo"}

    nformulaTaller = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
    categoriTaller = Column(Integer, nullable=False)
    formulataller = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    kilometraje = Column(String(20), nullable=False)

    def __repr__(self):
        return "<Formulataller(formulataller={self.formulataller})>"