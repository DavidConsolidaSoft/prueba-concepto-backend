# Generado automáticamente
# Tabla: dbo.permisos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Permisos(Base):
    __tablename__ = "permisos"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    modulo = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    permisos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    acceso = Column(Integer, nullable=False)
    crear = Column(Integer, nullable=False)
    modificar = Column(Integer, nullable=False)
    eliminar = Column(Integer, nullable=False)
    imprimir = Column(Integer, nullable=False)
    excel = Column(Integer, nullable=False)
    reporte = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Permisos(permisos={self.permisos})>"