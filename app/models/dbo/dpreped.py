# Generado automáticamente
# Tabla: dbo.dprePed
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dpreped(Base):
    __tablename__ = "dprePed"
    __table_args__ = {"schema": "dbo"}

    producto = Column(Integer)
    lote = Column(Integer)
    prePed = Column(Integer)
    cantidad = Column(Numeric(18, 2))
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    dprePed = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Dpreped(dprePed={self.dprePed})>"