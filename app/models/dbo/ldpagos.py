# Generado automáticamente
# Tabla: dbo.ldpagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Ldpagos(Base):
    __tablename__ = "ldpagos"
    __table_args__ = {"schema": "dbo"}

    cargo = Column(Numeric(16, 6), nullable=False)
    nula = Column(Boolean, nullable=False)
    abono = Column(Numeric(16, 6), nullable=False)
    hcargo = Column(Numeric(16, 6), nullable=False)
    habono = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    vdesc = Column(Numeric(16, 6), nullable=False)
    letras = Column(Integer, nullable=False)
    pagos = Column(Integer, nullable=False)
    dpagos = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    ldpagos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Ldpagos(ldpagos={self.ldpagos})>"