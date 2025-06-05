# Generado automáticamente
# Tabla: dbo.letras
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Letras(Base):
    __tablename__ = "letras"
    __table_args__ = {"schema": "dbo"}

    clientes = Column(String(25), nullable=False)
    tipomov = Column(Integer, nullable=False)
    contrato = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    numedocu = Column(String(15), nullable=False)
    fecha = Column(DateTime, nullable=False)
    fechacanc = Column(DateTime)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    montfact = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(18, 6), nullable=False)
    viva = Column(Numeric(18, 6), nullable=False)
    hmontfact = Column(Numeric(16, 6), nullable=False)
    habono = Column(Numeric(16, 6), nullable=False)
    hcargo = Column(Numeric(16, 6), nullable=False)
    abono = Column(Numeric(16, 6), nullable=False)
    cargo = Column(Numeric(16, 6), nullable=False)
    cuotas = Column(Numeric(16, 6), nullable=False)
    moneda = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    vendedor = Column(Integer, nullable=False)
    letras = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    noletras = Column(String(10), nullable=False)
    saldoanterior = Column(Numeric(16, 6), nullable=False)

    def __repr__(self):
        return "<Letras(letras={self.letras})>"