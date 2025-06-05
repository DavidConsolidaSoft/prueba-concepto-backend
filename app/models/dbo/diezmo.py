# Generado automáticamente
# Tabla: dbo.Diezmo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Diezmo(Base):
    __tablename__ = "Diezmo"
    __table_args__ = {"schema": "dbo"}

    Diezmo = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    Numedocu = Column(String(9), nullable=False)
    fecha = Column(DateTime, nullable=False)
    distrito = Column(Integer, nullable=False)
    lider = Column(Integer, nullable=False)
    entrega = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    conceptodiezmo = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Diezmo(Diezmo={self.Diezmo})>"