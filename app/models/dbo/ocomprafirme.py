# Generado automáticamente
# Tabla: dbo.ocomprafirme
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Ocomprafirme(Base):
    __tablename__ = "ocomprafirme"
    __table_args__ = {"schema": "dbo"}

    ocomprafirme = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    docompra = Column(Integer)
    opagada = Column(Integer)
    cantidad = Column(Numeric(12, 2))
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Ocomprafirme(ocomprafirme={self.ocomprafirme})>"