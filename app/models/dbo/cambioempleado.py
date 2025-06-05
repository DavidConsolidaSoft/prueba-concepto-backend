# Generado automáticamente
# Tabla: dbo.cambioempleado
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Cambioempleado(Base):
    __tablename__ = "cambioempleado"
    __table_args__ = {"schema": "dbo"}

    Activo = Column(Boolean, nullable=False)
    empleado = Column(Integer, nullable=False)
    grupo = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    cambioempleado = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Cambioempleado(cambioempleado={self.cambioempleado})>"