# Generado automáticamente
# Tabla: dbo.Factdelivery
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Factdelivery(Base):
    __tablename__ = "Factdelivery"
    __table_args__ = {"schema": "dbo"}

    dfactura = Column(Integer)
    cant1 = Column(Numeric(9, 2))
    cant2 = Column(Numeric(9, 2))
    cant3 = Column(Numeric(9, 2))
    cant4 = Column(Numeric(9, 2))
    cant5 = Column(Numeric(9, 2))
    cant6 = Column(Numeric(9, 2))
    cant7 = Column(Numeric(9, 2))
    cant8 = Column(Numeric(9, 2))
    cant9 = Column(Numeric(9, 2))
    cant10 = Column(Numeric(9, 2))
    cant11 = Column(Numeric(9, 2))
    cant12 = Column(Numeric(9, 2))
    cant13 = Column(Numeric(9, 2))
    cant14 = Column(Numeric(9, 2))
    cant15 = Column(Numeric(9, 2))
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    Factdelivery = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Factdelivery(Factdelivery={self.Factdelivery})>"