# Generado automáticamente
# Tabla: dbo.pncv
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Pncv(Base):
    __tablename__ = "pncv"
    __table_args__ = {"schema": "dbo"}

    ppagos = Column(Integer, nullable=False)
    dcompra = Column(Integer, nullable=False)
    ncmonto = Column(Numeric(16, 6), nullable=False)
    ncafecta = Column(Numeric(16, 6), nullable=False)
    ncexenta = Column(Numeric(16, 6), nullable=False)
    ncviva = Column(Numeric(16, 6), nullable=False)
    pncv = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    dppagos = Column(Integer)

    def __repr__(self):
        return "<Pncv(pncv={self.pncv})>"