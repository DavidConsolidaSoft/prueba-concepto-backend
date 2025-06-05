# Generado automáticamente
# Tabla: dbo.dproducto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dproducto(Base):
    __tablename__ = "dproducto"
    __table_args__ = {"schema": "dbo"}

    dalmacen = Column(Integer)
    cantrequerida = Column(Numeric(12, 6))
    cantpendiente = Column(Numeric(12, 6))
    cantsolicita = Column(Numeric(12, 6))
    devolucion = Column(Numeric(12, 6))
    averia = Column(Numeric(12, 6))
    notas = Column(String(250))
    empresa = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    dproducto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Dproducto(dproducto={self.dproducto})>"