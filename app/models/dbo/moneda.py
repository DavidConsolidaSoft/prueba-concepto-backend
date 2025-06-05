# Generado automáticamente
# Tabla: dbo.moneda
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Moneda(Base):
    __tablename__ = "moneda"
    __table_args__ = {"schema": "dbo"}

    nmoneda = Column(String(40), nullable=False)
    simmoneda = Column(String(4), nullable=False)
    principal = Column(Boolean, nullable=False)
    segunda = Column(Boolean, nullable=False)
    tercera = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    moneda = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Moneda(moneda={self.moneda})>"