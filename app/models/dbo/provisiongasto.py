# Generado automáticamente
# Tabla: dbo.ProvisionGasto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Provisiongasto(Base):
    __tablename__ = "ProvisionGasto"
    __table_args__ = {"schema": "dbo"}

    provisionGasto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    numedocu = Column(String(15), nullable=False)
    fecha = Column(DateTime, nullable=False)
    Afecta = Column(Numeric(18, 6), nullable=False)
    viva = Column(Numeric(18, 6), nullable=False)
    exenta = Column(Numeric(18, 6), nullable=False)
    retencion = Column(Numeric(18, 6), nullable=False)
    fovial = Column(Numeric(18, 6), nullable=False)
    excluidos = Column(Numeric(18, 6), nullable=False)
    partida = Column(Integer, nullable=False)
    renta = Column(Numeric(18, 6))
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    iva = Column(Integer, nullable=False)
    cotrans = Column(Numeric(16, 6))
    declarable = Column(Boolean, nullable=False)
    PERCEPCION = Column(Numeric(18, 6), nullable=False)
    deduccion1 = Column(Numeric(18, 6), nullable=False)
    deduccion2 = Column(Numeric(18, 6), nullable=False)
    linea = Column(Integer, nullable=False)
    Cuenta = Column(Integer)
    cesc = Column(Numeric(12, 2))
    serie = Column(String(15))

    # Relaciones
    # iva_rel = relationship("Iva", back_populates="provisiongasto_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Provisiongasto(provisionGasto={self.provisionGasto})>"