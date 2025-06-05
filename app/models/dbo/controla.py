# Generado automáticamente
# Tabla: dbo.controla
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Controla(Base):
    __tablename__ = "controla"
    __table_args__ = {"schema": "dbo"}

    tabla = Column(String(50), nullable=False)
    equipo = Column(String(50), nullable=False)
    hora = Column(DateTime)
    Activo = Column(Boolean, nullable=False)
    controla = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    caja = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Controla(controla={self.controla})>"