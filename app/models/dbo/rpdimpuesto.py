# Generado automáticamente
# Tabla: dbo.rpdImpuesto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Rpdimpuesto(Base):
    __tablename__ = "rpdImpuesto"
    __table_args__ = {"schema": "dbo"}

    rpdImpuesto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    clientes = Column(String(25), nullable=False)
    monto = Column(Numeric(18, 2))
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)
    rpImpuesto = Column(Integer)

    def __repr__(self):
        return "<Rpdimpuesto(rpdImpuesto={self.rpdImpuesto})>"