# Generado automáticamente
# Tabla: dbo.Entrega
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Entrega(Base):
    __tablename__ = "Entrega"
    __table_args__ = {"schema": "dbo"}

    entrega = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    nEntrega = Column(String(45), nullable=False)
    fecha = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Entrega(entrega={self.entrega})>"