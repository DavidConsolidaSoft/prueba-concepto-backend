# Generado automáticamente
# Tabla: dbo.tarea
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Tarea(Base):
    __tablename__ = "tarea"
    __table_args__ = {"schema": "dbo"}

    tarea = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ntarea = Column(String(50), nullable=False)
    controles = Column(Integer, nullable=False)
    duracion = Column(Numeric(18, 2))

    def __repr__(self):
        return "<Tarea(tarea={self.tarea})>"