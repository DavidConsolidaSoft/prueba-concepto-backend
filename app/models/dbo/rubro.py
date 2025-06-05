# Generado automáticamente
# Tabla: dbo.rubro
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Rubro(Base):
    __tablename__ = "rubro"
    __table_args__ = {"schema": "dbo"}

    nrubro = Column(String(25), nullable=False)
    operador = Column(Numeric(16, 6), nullable=False)
    activo = Column(Boolean, nullable=False)
    rubro = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    bienes = Column(Boolean, nullable=False)
    pasivo = Column(Boolean, nullable=False)
    capital = Column(Boolean, nullable=False)
    gastos = Column(Boolean, nullable=False)
    ingresos = Column(Boolean, nullable=False)
    liquidadora = Column(Boolean, nullable=False)
    NORUBRO = Column(String(1), nullable=False)

    def __repr__(self):
        return "<Rubro(rubro={self.rubro})>"