# Generado automáticamente
# Tabla: dbo.RupSubActivitie
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Rupsubactivitie(Base):
    __tablename__ = "RupSubActivitie"
    __table_args__ = {"schema": "dbo"}

    RupOTActividad = Column(Integer, nullable=False)
    nRupSubActividad = Column(String(45), nullable=False)
    Rupstandar = Column(Integer, nullable=False)
    Orden = Column(String(5), nullable=False)
    empleado = Column(Integer, nullable=False)
    fechaEntrega = Column(DateTime)
    fechaTerminado = Column(DateTime)
    HorasBudget = Column(Numeric(16, 6), nullable=False)
    HorasReal = Column(Numeric(16, 6), nullable=False)
    ValorHorahombre = Column(Numeric(16, 6), nullable=False)
    Activo = Column(Boolean, nullable=False)
    Terminado = Column(Boolean, nullable=False)
    RupSubActividad = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Rupsubactivitie(RupOTActividad={self.RupOTActividad})>"