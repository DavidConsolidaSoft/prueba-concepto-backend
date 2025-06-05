# Generado automáticamente
# Tabla: dbo.cpagocompra
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Cpagocompra(Base):
    __tablename__ = "cpagocompra"
    __table_args__ = {"schema": "dbo"}

    cpagocompra = Column(Integer, nullable=False, autoincrement=True)
    pagocompra = Column(Integer, primary_key=True, nullable=False)
    npagocompra = Column(String(50))
    Fecha = Column(DateTime)
    monto = Column(Numeric(9, 2))
    montoOriginal = Column(Numeric(9, 2))
    pagado = Column(Numeric(9, 2))
    factor = Column(Numeric(9, 2))
    moneda = Column(Integer)
    tasacambio = Column(Numeric(9, 6))
    compraFirme = Column(Integer)
    ocompra = Column(Integer)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Cpagocompra(pagocompra={self.pagocompra})>"