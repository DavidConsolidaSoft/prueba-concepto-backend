# Generado automáticamente
# Tabla: dbo.donacion
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Float
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Donacion(Base):
    __tablename__ = "donacion"
    __table_args__ = {"schema": "dbo"}

    dte = Column(Integer)
    monto = Column(Float)
    referencia = Column(String(50))
    almacen = Column(Integer)
    donacion = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Donacion(donacion={self.donacion})>"