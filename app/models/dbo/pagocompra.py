# Generado automáticamente
# Tabla: dbo.pagocompra
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Pagocompra(Base):
    __tablename__ = "pagocompra"
    __table_args__ = {"schema": "dbo"}

    pagocompra = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    npagocompra = Column(String(50), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    monto = Column(Numeric(18, 6), nullable=False)
    factor = Column(Numeric(18, 6), nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(18, 6), nullable=False)
    ocompra = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Pagocompra(pagocompra={self.pagocompra})>"