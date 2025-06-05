# Generado automáticamente
# Tabla: dbo.empleadoregistro
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Empleadoregistro(Base):
    __tablename__ = "empleadoregistro"
    __table_args__ = {"schema": "dbo"}

    empleado = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empleadoregistro = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    hora = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Empleadoregistro(empleadoregistro={self.empleadoregistro})>"