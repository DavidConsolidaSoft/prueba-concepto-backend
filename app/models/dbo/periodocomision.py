# Generado automáticamente
# Tabla: dbo.periodocomision
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Periodocomision(Base):
    __tablename__ = "periodocomision"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime, nullable=False)
    periodocomision = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Periodocomision(periodocomision={self.periodocomision})>"