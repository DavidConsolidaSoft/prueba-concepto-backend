# Generado automáticamente
# Tabla: dbo.mispagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Mispagos(Base):
    __tablename__ = "mispagos"
    __table_args__ = {"schema": "dbo"}

    mispagos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    misFinanzas = Column(Integer)
    doctipo = Column(Integer)
    fechaPago = Column(DateTime)
    fechaPlan = Column(DateTime, nullable=False)
    documento = Column(String(12))
    cargo = Column(Numeric(9, 2))
    abono = Column(Numeric(9, 2))
    notas = Column(String(250))
    impresa = Column(Boolean)
    nula = Column(Boolean)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    # Relaciones
    # misfinanzas = relationship("Misfinanzas", back_populates="mispagos_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Mispagos(mispagos={self.mispagos})>"