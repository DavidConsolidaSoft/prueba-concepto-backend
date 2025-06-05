# Generado automáticamente
# Tabla: dbo.dregpagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dregpagos(Base):
    __tablename__ = "dregpagos"
    __table_args__ = {"schema": "dbo"}

    cargo = Column(Numeric(15, 6))
    abono = Column(Numeric(15, 6))
    regpagos = Column(Integer)
    invcliente = Column(Integer)
    dregpagos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    hcargo = Column(Numeric(15, 6))
    habono = Column(Numeric(15, 6))
    pagos = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Dregpagos(dregpagos={self.dregpagos})>"