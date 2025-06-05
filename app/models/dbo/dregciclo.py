# Generado automáticamente
# Tabla: dbo.dregciclo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dregciclo(Base):
    __tablename__ = "dregciclo"
    __table_args__ = {"schema": "dbo"}

    regciclo = Column(Integer, nullable=False)
    dregciclo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    cBarra = Column(String(55), nullable=False)
    precio1 = Column(Numeric(16, 6), nullable=False)
    precio2 = Column(Numeric(16, 6), nullable=False)
    precio3 = Column(Numeric(16, 6), nullable=False)
    precio4 = Column(Numeric(16, 6), nullable=False)
    factura = Column(Integer, nullable=False)
    impresa = Column(Boolean, nullable=False)
    pagos = Column(Integer, nullable=False)
    automatico = Column(Boolean, nullable=False)
    clientes = Column(String(25), nullable=False)
    mes = Column(DateTime)
    GENERADO = Column(Boolean)
    nula = Column(Boolean)
    empresa = Column(Integer, nullable=False)

    # Relaciones
    # clientes_rel = relationship("Clientes", back_populates="dregciclo_set")  # Comentado automáticamente
    # regciclo_rel = relationship("Regciclo", back_populates="dregciclo_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dregciclo(dregciclo={self.dregciclo})>"