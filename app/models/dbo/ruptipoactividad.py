# Generado automáticamente
# Tabla: dbo.RupTipoActividad
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Ruptipoactividad(Base):
    __tablename__ = "RupTipoActividad"
    __table_args__ = {"schema": "dbo"}

    nRupTipoActividad = Column(String(25))
    activo = Column(Boolean, nullable=False)
    RupTipoActividad = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Ruptipoactividad(RupTipoActividad={self.RupTipoActividad})>"