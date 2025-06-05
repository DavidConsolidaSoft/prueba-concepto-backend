# Generado automáticamente
# Tabla: dbo.dmaestro
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Dmaestro(Base):
    __tablename__ = "dmaestro"
    __table_args__ = {"schema": "dbo"}

    tabla = Column(String(15), nullable=False)
    dmaestros = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    dmaestro = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Dmaestro(dmaestro={self.dmaestro})>"