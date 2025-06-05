# Generado automáticamente
# Tabla: dbo.rpImpuesto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Rpimpuesto(Base):
    __tablename__ = "rpImpuesto"
    __table_args__ = {"schema": "dbo"}

    rpImpuesto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    numedocu = Column(String(20))
    Impreso = Column(Boolean)
    descrip = Column(String(100))
    fecha = Column(DateTime)
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)
    monto = Column(Numeric(18, 6))

    def __repr__(self):
        return "<Rpimpuesto(rpImpuesto={self.rpImpuesto})>"