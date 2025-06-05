# Generado automáticamente
# Tabla: dbo.grupoempleado
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Grupoempleado(Base):
    __tablename__ = "grupoempleado"
    __table_args__ = {"schema": "dbo"}

    grupo = Column(Integer, nullable=False)
    empleado = Column(Integer, nullable=False)
    grupoempleado = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    usuario = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Grupoempleado(grupoempleado={self.grupoempleado})>"