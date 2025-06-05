# Generado automáticamente
# Tabla: dbo.dppartida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dppartida(Base):
    __tablename__ = "dppartida"
    __table_args__ = {"schema": "dbo"}

    dppartida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    orden = Column(String(1), nullable=False)
    banco = Column(Boolean, nullable=False)
    cheque = Column(Boolean, nullable=False)
    cheqnulo = Column(Boolean, nullable=False)
    aquien = Column(Boolean, nullable=False)
    cheqimp = Column(Boolean, nullable=False)
    concepto = Column(String(254), nullable=False)
    debe = Column(Numeric(16, 6), nullable=False)
    haber = Column(Numeric(16, 6), nullable=False)
    pdebe = Column(Numeric(16, 6), nullable=False)
    phaber = Column(Numeric(16, 6), nullable=False)
    hdebe = Column(Numeric(16, 6), nullable=False)
    hhaber = Column(Numeric(16, 6), nullable=False)
    hpdebe = Column(Numeric(16, 6), nullable=False)
    hphaber = Column(Numeric(16, 6), nullable=False)
    hconcepto = Column(String(254), nullable=False)
    ppartida = Column(Integer, nullable=False)
    cuenta = Column(Integer, nullable=False)
    ctrocosto = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    moneda = Column(Integer, nullable=False)

    # Relaciones
    # ctrocosto_rel = relationship("Ctrocosto", back_populates="dppartida_set")  # Comentado automáticamente
    # cuenta_rel = relationship("Cuenta", back_populates="dppartida_set")  # Comentado automáticamente
    # ppartida_rel = relationship("Ppartida", back_populates="dppartida_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dppartida(dppartida={self.dppartida})>"