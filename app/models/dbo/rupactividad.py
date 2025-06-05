# Generado automáticamente
# Tabla: dbo.RupActividad
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Rupactividad(Base):
    __tablename__ = "RupActividad"
    __table_args__ = {"schema": "dbo"}

    RupFase = Column(Integer, nullable=False)
    nRupActividad = Column(String(45), nullable=False)
    Orden = Column(String(5), nullable=False)
    Activo = Column(Boolean, nullable=False)
    RupActividad = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    rupResponsable = Column(Integer)

    def __repr__(self):
        return "<Rupactividad(RupActividad={self.RupActividad})>"