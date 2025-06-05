# Generado automáticamente
# Tabla: dbo.ffgasto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Ffgasto(Base):
    __tablename__ = "ffgasto"
    __table_args__ = {"schema": "dbo"}

    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    gastoacum = Column(Numeric(16, 6), nullable=False)
    gastoacumlocal = Column(Numeric(16, 6), nullable=False)
    gastoacumseg = Column(Numeric(16, 6), nullable=False)
    gastomes = Column(Numeric(16, 6), nullable=False)
    gastomeslocal = Column(Numeric(16, 6), nullable=False)
    gastomesseg = Column(Numeric(16, 6), nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    costolocal = Column(Numeric(16, 6), nullable=False)
    costoseg = Column(Numeric(16, 6), nullable=False)
    vrescate = Column(Numeric(16, 6), nullable=False)
    vrescatelocal = Column(Numeric(16, 6), nullable=False)
    vrescateseg = Column(Numeric(16, 6), nullable=False)
    activo = Column(Boolean, nullable=False)
    moneda = Column(Integer, nullable=False)
    ffgasto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fecha = Column(DateTime, nullable=False)
    periodoaf = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Ffgasto(ffgasto={self.ffgasto})>"