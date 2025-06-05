# Generado automáticamente
# Tabla: dbo.dbudget
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dbudget(Base):
    __tablename__ = "dbudget"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime)
    cuenta = Column(Integer)
    monto = Column(Numeric(12, 2))
    empresa = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    dbudget = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Dbudget(dbudget={self.dbudget})>"