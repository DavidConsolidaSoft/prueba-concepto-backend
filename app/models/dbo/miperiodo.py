# Generado automáticamente
# Tabla: dbo.MIPERIODO
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Miperiodo(Base):
    __tablename__ = "MIPERIODO"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    FECHA = Column(DateTime, nullable=False)
    PERIODO = Column(Integer, nullable=False)
    ACTIVO = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Miperiodo(FECHA={self.FECHA})>"