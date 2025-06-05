# Generado automáticamente
# Tabla: dbo.proceso
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Proceso(Base):
    __tablename__ = "proceso"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    descrip = Column(String(50), nullable=False)
    nproceso = Column(String(100))
    proceso = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    SISTEMA = Column(Boolean, nullable=False)
    micolor = Column(Integer, nullable=False)
    diasDeGracia = Column(Integer, nullable=False)
    esProceso = Column(Boolean, nullable=False)
    validado = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Proceso(proceso={self.proceso})>"