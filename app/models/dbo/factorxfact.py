# Generado automáticamente
# Tabla: dbo.factorxfact
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Factorxfact(Base):
    __tablename__ = "factorxfact"
    __table_args__ = {"schema": "dbo"}

    factura = Column(Integer, nullable=False)
    dfactura = Column(Integer, nullable=False)
    kardex = Column(Integer, nullable=False)
    muestras = Column(Numeric(16, 6), nullable=False)
    factor = Column(Numeric(16, 6), nullable=False)
    factorprecio = Column(Numeric(16, 6), nullable=False)
    factorxfact = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Factorxfact(factorxfact={self.factorxfact})>"