# Generado automáticamente
# Tabla: dbo.saldocliente
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Saldocliente(Base):
    __tablename__ = "saldocliente"
    __table_args__ = {"schema": "dbo"}

    mes = Column(DateTime)
    clientes = Column(String(25), nullable=False)
    cargo = Column(Numeric(16, 6), nullable=False)
    abono = Column(Numeric(16, 6), nullable=False)
    saldocliente = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Saldocliente(saldocliente={self.saldocliente})>"