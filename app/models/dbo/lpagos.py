# Generado automáticamente
# Tabla: dbo.lpagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Lpagos(Base):
    __tablename__ = "lpagos"
    __table_args__ = {"schema": "dbo"}

    impresa = Column(Boolean, nullable=False)
    numedocu = Column(String(10), nullable=False)
    tipomov = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    clientes = Column(String(25), nullable=False)
    fecha = Column(DateTime, nullable=False)
    nula = Column(Boolean, nullable=False)
    iva = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    referencia = Column(String(15), nullable=False)
    notas = Column(String(120), nullable=False)
    cargo = Column(Numeric(16, 6), nullable=False)
    abono = Column(Numeric(16, 6), nullable=False)
    mora = Column(Numeric(16, 6), nullable=False)
    difcambio = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    vdesc = Column(Numeric(16, 6), nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    pagos = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    lpagos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    condpago = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Lpagos(lpagos={self.lpagos})>"