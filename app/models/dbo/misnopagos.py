# Generado automáticamente
# Tabla: dbo.misnopagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Misnopagos(Base):
    __tablename__ = "misnopagos"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    invcliente = Column(Integer, nullable=False)
    factura_a = Column(Integer, nullable=False)
    factura_b = Column(String(15), nullable=False)
    factfecha = Column(DateTime)
    montfact = Column(Numeric(15, 6), nullable=False)
    abono = Column(Numeric(15, 6), nullable=False)
    cargo = Column(Numeric(15, 6), nullable=False)
    saldo = Column(Numeric(17, 6), nullable=False)
    clientes = Column(String(25), nullable=False)
    pagos = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    numedocu = Column(String(10), nullable=False)
    tipomov = Column(Integer, nullable=False)
    ntipomov = Column(String(35), nullable=False)
    misabonos = Column(Numeric(15, 6), nullable=False)
    miscargos = Column(Numeric(15, 6), nullable=False)
    dpagos = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Misnopagos(invcliente={self.invcliente})>"