# Generado automáticamente
# Tabla: dbo.cambiojornadaemp
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Cambiojornadaemp(Base):
    __tablename__ = "cambiojornadaemp"
    __table_args__ = {"schema": "dbo"}

    jornada = Column(Integer, nullable=False)
    jornada2 = Column(Integer, nullable=False)
    descripcion = Column(String(100), nullable=False)
    empleado = Column(Integer, nullable=False)
    cambiojornadaemp = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fechacambio = Column(DateTime)

    def __repr__(self):
        return "<Cambiojornadaemp(cambiojornadaemp={self.cambiojornadaemp})>"