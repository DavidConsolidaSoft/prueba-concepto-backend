# Generado automáticamente
# Tabla: dbo.misfinanzas
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Misfinanzas(Base):
    __tablename__ = "misfinanzas"
    __table_args__ = {"schema": "dbo"}

    misfinanzas = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    TipoCargo = Column(Integer)
    fecha = Column(DateTime, nullable=False)
    documento = Column(String(12))
    monto = Column(Numeric(9, 2))
    cargo = Column(Numeric(9, 2))
    abono = Column(Numeric(9, 2))
    notas = Column(String(250))
    impresa = Column(Boolean)
    nula = Column(Boolean)
    pagada = Column(Boolean)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    # Relaciones
    # tipocargo = relationship("Tipocargo", back_populates="misfinanzas_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Misfinanzas(misfinanzas={self.misfinanzas})>"