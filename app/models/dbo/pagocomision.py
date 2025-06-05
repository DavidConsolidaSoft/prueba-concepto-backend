# Generado automáticamente
# Tabla: dbo.pagocomision
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Pagocomision(Base):
    __tablename__ = "pagocomision"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime, nullable=False)
    CodVendedor = Column(Integer, nullable=False)
    vendedor = Column(String(50), nullable=False)
    VentaEfectivo = Column(Numeric(18, 6), nullable=False)
    VentaCredito = Column(Numeric(18, 6), nullable=False)
    recuperacion = Column(Numeric(18, 6), nullable=False)
    FactorComision = Column(Numeric(6, 4), nullable=False)
    Comision = Column(Numeric(18, 6), nullable=False)
    ajusteComision = Column(Numeric(18, 6), nullable=False)
    antiguedad = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    pagocomision = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tipomov = Column(String(100), nullable=False)
    numedocu = Column(String(50), nullable=False)
    fechadoc = Column(DateTime)
    clientes = Column(String(50))
    fechacan = Column(DateTime)

    def __repr__(self):
        return "<Pagocomision(pagocomision={self.pagocomision})>"