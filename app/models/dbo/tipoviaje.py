# Generado automáticamente
# Tabla: dbo.tipoviaje
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipoviaje(Base):
    __tablename__ = "tipoviaje"
    __table_args__ = {"schema": "dbo"}

    ntipoviaje = Column(String(35), nullable=False)
    tipoviaje = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Tipoviaje(tipoviaje={self.tipoviaje})>"