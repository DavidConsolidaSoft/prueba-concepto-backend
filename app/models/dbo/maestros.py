# Generado automáticamente
# Tabla: dbo.maestros
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Maestros(Base):
    __tablename__ = "maestros"
    __table_args__ = {"schema": "dbo"}

    tabla = Column(String(15), nullable=False)
    nombre = Column(String(20), nullable=False)
    ntabla = Column(String(210), nullable=False)
    activo = Column(Boolean, nullable=False)
    acceso = Column(Integer, nullable=False)
    crear = Column(Integer, nullable=False)
    modificar = Column(Integer, nullable=False)
    eliminar = Column(Integer, nullable=False)
    imprimir = Column(Integer, nullable=False)
    excel = Column(Integer, nullable=False)
    reportes = Column(Integer, nullable=False)
    modulo = Column(Integer, nullable=False)
    maestros = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Maestros(maestros={self.maestros})>"