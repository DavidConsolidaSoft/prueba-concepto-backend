# Generado automáticamente
# Tabla: dbo.RutaCamion
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Rutacamion(Base):
    __tablename__ = "RutaCamion"
    __table_args__ = {"schema": "dbo"}

    rutaCamion = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    nRutaCamion = Column(String(35), nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Rutacamion(rutaCamion={self.rutaCamion})>"