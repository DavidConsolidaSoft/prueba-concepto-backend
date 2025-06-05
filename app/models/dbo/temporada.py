# Generado automáticamente
# Tabla: dbo.Temporada
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Temporada(Base):
    __tablename__ = "Temporada"
    __table_args__ = {"schema": "dbo"}

    Temporada = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nTemporada = Column(String(15), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Temporada(Temporada={self.Temporada})>"