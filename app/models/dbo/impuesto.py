# Generado automáticamente
# Tabla: dbo.impuesto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Impuesto(Base):
    __tablename__ = "impuesto"
    __table_args__ = {"schema": "dbo"}

    nimpuesto = Column(String(25))
    factor = Column(Numeric(5, 2))
    impuesto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Impuesto(impuesto={self.impuesto})>"