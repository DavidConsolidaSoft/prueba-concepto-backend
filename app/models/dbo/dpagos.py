# Generado automáticamente
# Tabla: dbo.dpagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dpagos(Base):
    __tablename__ = "dpagos"
    __table_args__ = {"schema": "dbo"}

    cargo = Column(Numeric(15, 6), nullable=False)
    abono = Column(Numeric(15, 6), nullable=False)
    pagos = Column(Integer, nullable=False)
    invcliente = Column(Integer, nullable=False)
    dpagos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    hcargo = Column(Numeric(15, 6), nullable=False)
    habono = Column(Numeric(15, 6), nullable=False)
    vendedor = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    recibo = Column(String(12), nullable=False)
    afecta = Column(Numeric(18, 6), nullable=False)
    exenta = Column(Numeric(18, 6), nullable=False)
    viva = Column(Numeric(18, 6), nullable=False)
    retencion = Column(Numeric(18, 6), nullable=False)
    nocheque = Column(String(25), nullable=False)
    fechacheque = Column(DateTime)
    rechazado = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    chcobrado = Column(Boolean, nullable=False)
    FechaCobrado = Column(DateTime)
    enfirme = Column(Boolean, nullable=False)
    pagada = Column(Boolean, nullable=False)
    percepcion = Column(Numeric(18, 6), nullable=False)
    nosujeto = Column(Numeric(18, 6), nullable=False)
    chrechazado = Column(Boolean, nullable=False)
    chpagado = Column(Boolean, nullable=False)
    noRemesa = Column(String(15), nullable=False)
    bancoRemesa = Column(Integer, nullable=False)
    fechadeposito = Column(DateTime)
    qlinea = Column(Integer, nullable=False)
    montopost = Column(Numeric(18, 6), nullable=False)
    nocuenta = Column(String(50), nullable=False)

    # Relaciones
    # invcliente_rel = relationship("Invcliente", back_populates="dpagos_set")  # Comentado automáticamente
    # pagos_rel = relationship("Pagos", back_populates="dpagos_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dpagos(dpagos={self.dpagos})>"