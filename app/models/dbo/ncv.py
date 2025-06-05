# Generado automáticamente
# Tabla: dbo.ncv
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Ncv(Base):
    __tablename__ = "ncv"
    __table_args__ = {"schema": "dbo"}

    pagos = Column(Integer, nullable=False)
    dfactura = Column(Integer, nullable=False)
    ncmonto = Column(Numeric(16, 6), nullable=False)
    ncafecta = Column(Numeric(16, 6), nullable=False)
    ncexenta = Column(Numeric(16, 6), nullable=False)
    ncviva = Column(Numeric(16, 6), nullable=False)
    ncv = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    qlinea = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Ncv(ncv={self.ncv})>"