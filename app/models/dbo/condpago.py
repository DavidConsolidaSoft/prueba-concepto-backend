# Generado automáticamente
# Tabla: dbo.condpago
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class CondPago(Base):
    __tablename__ = "condpago"
    __table_args__ = {"schema": "dbo"}

    ncondpago = Column(String(50), nullable=False)
    plazo = Column(Integer, nullable=False)
    contado = Column(Boolean, nullable=False)
    preferido = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    condpago = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    cheque = Column(Boolean, nullable=False)
    tarjeta = Column(Boolean, nullable=False)
    remesa = Column(Boolean, nullable=False)
    otro = Column(Boolean, nullable=False)
    vueltaviaje = Column(Boolean, nullable=False)
    canjepuntos = Column(Boolean, nullable=False)
    contrato = Column(Boolean, nullable=False)
    transferencia = Column(Boolean, nullable=False)
    bitcoin = Column(Boolean, nullable=False)
    activarPromo = Column(Boolean, nullable=False)
    pdesc = Column(Numeric(5, 2), nullable=False)
    d1 = Column(Boolean, nullable=False)
    d2 = Column(Boolean, nullable=False)
    d3 = Column(Boolean, nullable=False)
    d4 = Column(Boolean, nullable=False)
    d5 = Column(Boolean, nullable=False)
    d6 = Column(Boolean, nullable=False)
    d7 = Column(Boolean, nullable=False)
    h1 = Column(Integer, nullable=False)
    h2 = Column(Integer, nullable=False)
    m1 = Column(Integer, nullable=False)
    m2 = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Condpago(condpago={self.condpago})>"