# Generado automáticamente
# Tabla: dbo.unidad
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Unidad(Base):
    __tablename__ = "unidad"
    __table_args__ = {"schema": "dbo"}

    nunidad = Column(String(50), nullable=False)
    descripcion = Column(String(75), nullable=False)
    activo = Column(Boolean, nullable=False)
    unidad = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Unidad(unidad={self.unidad})>"