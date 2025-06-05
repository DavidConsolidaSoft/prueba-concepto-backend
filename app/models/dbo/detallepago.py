# Generado automáticamente
# Tabla: dbo.detallepago
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Detallepago(Base):
    __tablename__ = "detallepago"
    __table_args__ = {"schema": "dbo"}

    detallepago = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    factura = Column(Integer, nullable=False)
    Banco1 = Column(Integer, nullable=False)
    cheque1 = Column(String(35), nullable=False)
    MontBanco1 = Column(Numeric(18, 6), nullable=False)
    Banco2 = Column(Integer, nullable=False)
    cheque2 = Column(String(35), nullable=False)
    MontBanco2 = Column(Numeric(18, 6), nullable=False)
    TarjetaCredito = Column(Integer, nullable=False)
    notarjeta = Column(String(50), nullable=False)
    montTarjeta = Column(Numeric(18, 6), nullable=False)
    Efectivo = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Detallepago(detallepago={self.detallepago})>"