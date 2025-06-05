# Generado automáticamente
# Tabla: dbo.invpago
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Invpago(Base):
    __tablename__ = "invpago"
    __table_args__ = {"schema": "dbo"}

    factura = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    montfact = Column(Numeric(16, 6), nullable=False)
    tarjeta = Column(String(10), nullable=False)
    cheque = Column(String(10), nullable=False)
    pcheque = Column(String(10), nullable=False)
    acheque = Column(Numeric(16, 6), nullable=False)
    atarjeta = Column(Numeric(16, 6), nullable=False)
    aefectivo = Column(Numeric(16, 6), nullable=False)
    apcheque = Column(Numeric(16, 6), nullable=False)
    abono = Column(Numeric(16, 6), nullable=False)
    cargo = Column(Numeric(16, 6), nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambi2 = Column(Numeric(16, 6), nullable=False)
    tasacambi3 = Column(Numeric(16, 6), nullable=False)
    invpago = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Invpago(invpago={self.invpago})>"