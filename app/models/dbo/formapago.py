# Generado automáticamente
# Tabla: dbo.formapago
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class FormaPago(Base):
    __tablename__ = "formapago"
    __table_args__ = {"schema": "dbo"}

    efectivo = Column(Numeric(16, 6), nullable=False)
    activo = Column(Boolean, nullable=False)
    cheque = Column(Numeric(16, 6), nullable=False)
    tarjeta = Column(Numeric(16, 6), nullable=False)
    billete1 = Column(Numeric(16, 6), nullable=False)
    billete2 = Column(Numeric(16, 6), nullable=False)
    billete3 = Column(Numeric(16, 6), nullable=False)
    billete4 = Column(Numeric(16, 6), nullable=False)
    billete5 = Column(Numeric(16, 6), nullable=False)
    billete6 = Column(Numeric(16, 6), nullable=False)
    moneda1 = Column(Numeric(16, 6), nullable=False)
    reparacion = Column(Numeric(16, 6), nullable=False)
    gastos = Column(Numeric(16, 6), nullable=False)
    fondosajenos = Column(Numeric(16, 6), nullable=False)
    retencion = Column(Numeric(16, 6), nullable=False)
    fecha = Column(DateTime, nullable=False)
    nocheque = Column(Numeric(16, 6), nullable=False)
    notarjeta = Column(Numeric(16, 6), nullable=False)
    factura = Column(Numeric(16, 6), nullable=False)
    contrato = Column(Numeric(16, 6), nullable=False)
    formapago = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Formapago(formapago={self.formapago})>"