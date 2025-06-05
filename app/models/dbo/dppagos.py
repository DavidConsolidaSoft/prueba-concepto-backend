# Generado automáticamente
# Tabla: dbo.dppagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dppagos(Base):
    __tablename__ = "dppagos"
    __table_args__ = {"schema": "dbo"}

    cargo = Column(Numeric(16, 6), nullable=False)
    abono = Column(Numeric(16, 6), nullable=False)
    ppagos = Column(Integer, nullable=False)
    compra = Column(Integer, nullable=False)
    dppagos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    hcargo = Column(Numeric(16, 6), nullable=False)
    habono = Column(Numeric(16, 6), nullable=False)
    partida = Column(Integer)
    retencion = Column(Integer)

    def __repr__(self):
        return "<Dppagos(dppagos={self.dppagos})>"