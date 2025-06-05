# Generado automáticamente
# Tabla: dbo.entregable
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Entregable(Base):
    __tablename__ = "entregable"
    __table_args__ = {"schema": "dbo"}

    etapa = Column(Integer, nullable=False)
    entregable = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nentregable = Column(String(50), nullable=False)
    duracion = Column(Numeric(18, 2), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Entregable(entregable={self.entregable})>"