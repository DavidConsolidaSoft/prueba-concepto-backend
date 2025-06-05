# Generado automáticamente
# Tabla: dbo.prestemp
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Prestemp(Base):
    __tablename__ = "prestemp"
    __table_args__ = {"schema": "dbo"}

    nprestemp = Column(String(80), nullable=False)
    tipoprest = Column(Integer)
    banco = Column(Integer)
    montoprest = Column(Numeric(18, 6), nullable=False)
    fecprestam = Column(DateTime)
    fecucuota = Column(DateTime)
    numcuotas = Column(Integer, nullable=False)
    numpcuota = Column(Integer, nullable=False)
    ultimacuota = Column(Integer, nullable=False)
    montocuota = Column(Numeric(18, 6), nullable=False)
    cuotanum = Column(Integer, nullable=False)
    saldo = Column(Numeric(18, 6), nullable=False)
    nota = Column(String(100), nullable=False)
    frecpago = Column(Integer)
    activo = Column(Boolean, nullable=False)
    empleado = Column(Integer)
    usuario = Column(Integer)
    prestemp = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime, nullable=False)
    montoprestseg = Column(Numeric(18, 6), nullable=False)
    montocuotaseg = Column(Numeric(18, 6), nullable=False)
    saldoseg = Column(Numeric(18, 6), nullable=False)
    empresa = Column(Integer)
    cancelado = Column(Boolean)
    noprestamo = Column(String(50))
    fechavence = Column(DateTime)
    suspendido = Column(Boolean)
    montocuota2 = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Prestemp(nprestemp={self.nprestemp})>"