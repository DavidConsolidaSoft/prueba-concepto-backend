# Generado automáticamente
# Tabla: dbo.ingfijo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Ingfijo(Base):
    __tablename__ = "ingfijo"
    __table_args__ = {"schema": "dbo"}

    ingfijo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empleado = Column(Integer, nullable=False)
    polingpla = Column(Integer, nullable=False)
    monto = Column(Numeric(9, 3), nullable=False)
    monto1 = Column(Numeric(9, 3), nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Ingfijo(ingfijo={self.ingfijo})>"