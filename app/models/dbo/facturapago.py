# Generado automáticamente
# Tabla: dbo.FacturaPago
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Facturapago(Base):
    __tablename__ = "FacturaPago"
    __table_args__ = {"schema": "dbo"}

    factura = Column(Integer)
    fecha = Column(DateTime)
    Monto = Column(Numeric(12, 2))
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    FacturaPago = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Facturapago(FacturaPago={self.FacturaPago})>"