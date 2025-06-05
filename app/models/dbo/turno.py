# Generado automáticamente
# Tabla: dbo.turno
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Turno(Base):
    __tablename__ = "turno"
    __table_args__ = {"schema": "dbo"}

    nturno = Column(String(25))
    turno = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Turno(turno={self.turno})>"