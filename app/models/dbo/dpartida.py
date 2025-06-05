# Generado automáticamente
# Tabla: dbo.dpartida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dpartida(Base):
    __tablename__ = "dpartida"
    __table_args__ = {"schema": "dbo"}

    orden = Column(String(1), nullable=False)
    banco = Column(Boolean, nullable=False)
    cheque = Column(Boolean, nullable=False)
    cheqnulo = Column(Boolean, nullable=False)
    aquien = Column(Boolean, nullable=False)
    cheqimp = Column(Boolean, nullable=False)
    concepto = Column(String(800))
    debe = Column(Numeric(16, 6), nullable=False)
    haber = Column(Numeric(16, 6), nullable=False)
    hdebe = Column(Numeric(16, 6), nullable=False)
    hhaber = Column(Numeric(16, 6), nullable=False)
    pdebe = Column(Numeric(16, 6), nullable=False)
    phaber = Column(Numeric(16, 6), nullable=False)
    hphaber = Column(Numeric(16, 6), nullable=False)
    hpdebe = Column(Numeric(16, 6), nullable=False)
    partida = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    cuenta = Column(Integer, nullable=False)
    ctrocosto = Column(Integer, nullable=False)
    dpartida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    hconcepto = Column(String(254), nullable=False)
    linea = Column(Integer, nullable=False)
    conciliado = Column(Boolean, nullable=False)
    comparativo = Column(Numeric(18, 6), nullable=False)
    automov = Column(Boolean, nullable=False)
    fconc = Column(DateTime)

    # Relaciones
    # ctrocosto_rel = relationship("Ctrocosto", back_populates="dpartida_set")  # Comentado automáticamente
    # cuenta_rel = relationship("Cuenta", back_populates="dpartida_set")  # Comentado automáticamente
    # partida_rel = relationship("Partida", back_populates="dpartida_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dpartida(dpartida={self.dpartida})>"