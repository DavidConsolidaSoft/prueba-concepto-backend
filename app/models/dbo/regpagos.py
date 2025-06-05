# Generado automáticamente
# Tabla: dbo.regpagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Regpagos(Base):
    __tablename__ = "regpagos"
    __table_args__ = {"schema": "dbo"}

    tipomov = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    clientes = Column(String(25), nullable=False)
    referencia = Column(String(15), nullable=False)
    notas = Column(String(120), nullable=False)
    fecha = Column(DateTime, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    contabilidad = Column(Boolean, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    abono = Column(Numeric(16, 6), nullable=False)
    difcambio = Column(Numeric(16, 6), nullable=False)
    mora = Column(Numeric(16, 6), nullable=False)
    regpagos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    numedocu = Column(String(10))
    cargo = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    iva = Column(Integer, nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    caja = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Regpagos(regpagos={self.regpagos})>"