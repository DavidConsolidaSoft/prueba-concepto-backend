# Generado automáticamente
# Tabla: dbo.dpEntrega
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dpentrega(Base):
    __tablename__ = "dpEntrega"
    __table_args__ = {"schema": "dbo"}

    dpEntrega = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    Entrega = Column(Integer, nullable=False)
    monto = Column(Numeric(18, 6), nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Dpentrega(dpEntrega={self.dpEntrega})>"