# Generado automáticamente
# Tabla: dbo.dlinea1
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dlinea1(Base):
    __tablename__ = "dlinea1"
    __table_args__ = {"schema": "dbo"}

    linea1 = Column(Integer, nullable=False)
    dlinea1 = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tarea = Column(Integer, nullable=False)
    entregable = Column(Integer, nullable=False)
    duracion = Column(Numeric(18, 2), nullable=False)
    estatus = Column(Integer, nullable=False)
    hora1 = Column(DateTime)
    hora2 = Column(DateTime)
    costohora = Column(Numeric(18, 2), nullable=False)
    notas = Column(String(200))
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Dlinea1(dlinea1={self.dlinea1})>"