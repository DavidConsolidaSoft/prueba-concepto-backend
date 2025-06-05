# Generado automáticamente
# Tabla: dbo.REMESA
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Remesa(Base):
    __tablename__ = "REMESA"
    __table_args__ = {"schema": "dbo"}

    remesa = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    fecha = Column(DateTime)
    monto = Column(Numeric(19, 8))
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    numero = Column(String(100))
    activo = Column(Boolean)
    banco = Column(Integer)
    saldo = Column(Numeric(19, 8))
    contado = Column(Boolean)
    noReserva = Column(String(25), nullable=False)
    escheque = Column(Boolean, nullable=False)
    venta = Column(Boolean, nullable=False)
    credito = Column(Numeric(18, 6), nullable=False)
    tarjeta = Column(Numeric(18, 6), nullable=False)
    cheque = Column(Numeric(18, 6), nullable=False)
    valor = Column(Numeric(18, 6), nullable=False)
    tipomov = Column(Integer, nullable=False)
    noitems = Column(Integer, nullable=False)
    caja = Column(Integer, nullable=False)
    saldocaja = Column(Boolean, nullable=False)
    estarjeta = Column(Boolean, nullable=False)
    fechadoc = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Remesa(remesa={self.remesa})>"