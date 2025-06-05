# Generado automáticamente
# Tabla: dbo.subproyecto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Subproyecto(Base):
    __tablename__ = "subproyecto"
    __table_args__ = {"schema": "dbo"}

    proyecto = Column(Integer, nullable=False)
    nsubproyecto = Column(String(50), nullable=False)
    descripcion = Column(String(75), nullable=False)
    fechainicion = Column(DateTime)
    fechafin = Column(DateTime)
    activo = Column(Boolean, nullable=False)
    encargado = Column(Integer, nullable=False)
    subproyecto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Subproyecto(subproyecto={self.subproyecto})>"