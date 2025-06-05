# Generado automáticamente
# Tabla: dbo.proyecto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Proyecto(Base):
    __tablename__ = "proyecto"
    __table_args__ = {"schema": "dbo"}

    nproyecto = Column(String(50), nullable=False)
    descripcion = Column(String(75), nullable=False)
    fechainicion = Column(DateTime)
    fechafin = Column(DateTime)
    activo = Column(Boolean, nullable=False)
    encargado = Column(Integer, nullable=False)
    proyecto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    NULA = Column(Boolean, nullable=False)
    PROCESADA = Column(Boolean, nullable=False)
    PRESUPUESTO = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Proyecto(proyecto={self.proyecto})>"