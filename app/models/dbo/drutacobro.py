# Generado automáticamente
# Tabla: dbo.drutacobro
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Drutacobro(Base):
    __tablename__ = "drutacobro"
    __table_args__ = {"schema": "dbo"}

    invcliente = Column(Integer, nullable=False)
    factura = Column(Integer, nullable=False)
    rutacobro = Column(Integer, nullable=False)
    saldo = Column(Numeric(18, 6), nullable=False)
    drutacobro = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    liquidada = Column(Boolean, nullable=False)
    vence = Column(Integer, nullable=False)
    ANTIGUEDAD = Column(Integer, nullable=False)
    cobrada = Column(Boolean, nullable=False)
    dpagos = Column(Integer)
    monto = Column(Numeric(9, 2))
    quedan = Column(String(9))
    fechaquedan = Column(DateTime)
    noRemesa = Column(String(15))
    Recibo = Column(String(12))
    FechaDeposito = Column(DateTime)
    CondPago = Column(Integer)
    noCheque = Column(String(25))
    FechaCheque = Column(DateTime)
    cambodega = Column(Integer)
    vdesc = Column(Numeric(9, 2))
    nocuenta = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Drutacobro(drutacobro={self.drutacobro})>"