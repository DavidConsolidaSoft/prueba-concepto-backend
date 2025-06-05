# Generado automáticamente
# Tabla: dbo.dimpuesto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Float
from sqlalchemy import Column, Integer


class Dimpuesto(Base):
    __tablename__ = "dimpuesto"
    __table_args__ = {"schema": "dbo"}

    compra = Column(Integer, primary_key=True, nullable=False)
    impuesto = Column(Integer, primary_key=True, nullable=False)
    valor = Column(Float)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Dimpuesto(impuesto={self.impuesto}, compra={self.compra})>"