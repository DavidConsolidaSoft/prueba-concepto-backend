# Generado automáticamente
# Tabla: dbo.movimiento
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Movimiento(Base):
    __tablename__ = "movimiento"
    __table_args__ = {"schema": "dbo"}

    movimiento = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nmovimiento = Column(String(150))
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Movimiento(movimiento={self.movimiento})>"