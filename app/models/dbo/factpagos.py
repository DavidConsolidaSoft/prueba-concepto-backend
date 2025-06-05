# Generado automáticamente
# Tabla: dbo.factpagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer


class Factpagos(Base):
    __tablename__ = "factpagos"
    __table_args__ = {"schema": "dbo"}

    factpagos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    factura = Column(Integer, nullable=False)
    pagos = Column(Integer, nullable=False)
    facturanula = Column(Integer, nullable=False)
    pagosnula = Column(Integer, nullable=False)
    empresa = Column(Integer)

    def __repr__(self):
        return "<Factpagos(factpagos={self.factpagos})>"