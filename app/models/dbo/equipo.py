# Generado automáticamente
# Tabla: dbo.equipo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Equipo(Base):
    __tablename__ = "equipo"
    __table_args__ = {"schema": "dbo"}

    nequipo = Column(String(35))
    orden = Column(String(4))
    tiempo = Column(Numeric(6, 2))
    cantidad = Column(Numeric(12, 2))
    empresa = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    equipo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Equipo(equipo={self.equipo})>"