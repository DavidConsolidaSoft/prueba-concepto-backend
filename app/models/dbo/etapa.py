# Generado automáticamente
# Tabla: dbo.etapa
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Etapa(Base):
    __tablename__ = "etapa"
    __table_args__ = {"schema": "dbo"}

    fase = Column(Integer, nullable=False)
    etapa = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    netapa = Column(String(50), nullable=False)
    duracion = Column(Numeric(18, 2), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Etapa(etapa={self.etapa})>"