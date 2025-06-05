# Generado automáticamente
# Tabla: dbo.historenta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Historenta(Base):
    __tablename__ = "historenta"
    __table_args__ = {"schema": "dbo"}

    historenta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    isss = Column(Numeric(18, 6), nullable=False)
    afp = Column(Numeric(18, 6), nullable=False)
    renta = Column(Numeric(18, 6), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empleado = Column(Integer, nullable=False)
    concepto = Column(String(80), nullable=False)
    monto = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Historenta(historenta={self.historenta})>"