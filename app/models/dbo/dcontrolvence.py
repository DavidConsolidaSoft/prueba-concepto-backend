# Generado automáticamente
# Tabla: dbo.dcontrolvence
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dcontrolvence(Base):
    __tablename__ = "dcontrolvence"
    __table_args__ = {"schema": "dbo"}

    dcontrolvence = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dfactura = Column(Integer, nullable=False)
    uvendidas = Column(Numeric(18, 6), nullable=False)
    vendida = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    venta = Column(Numeric(16, 8), nullable=False)
    controlvence = Column(Integer, nullable=False)
    diasvence = Column(Integer, nullable=False)
    saldo = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Dcontrolvence(dcontrolvence={self.dcontrolvence})>"