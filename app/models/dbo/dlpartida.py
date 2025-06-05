# Generado automáticamente
# Tabla: dbo.dlpartida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dlpartida(Base):
    __tablename__ = "dlpartida"
    __table_args__ = {"schema": "dbo"}

    orden = Column(String(1), nullable=False)
    concepto = Column(String(254), nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    debemont = Column(Numeric(16, 6), nullable=False)
    habermont = Column(Numeric(16, 6), nullable=False)
    lpartida = Column(Integer, nullable=False)
    dfpartida = Column(Integer, nullable=False)
    cuenta = Column(Integer, nullable=False)
    ctrocosto = Column(Integer, nullable=False)
    dlpartida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    # Relaciones
    # ctrocosto_rel = relationship("Ctrocosto", back_populates="dlpartida_set")  # Comentado automáticamente
    # ctrocosto_rel = relationship("Ctrocosto", back_populates="dlpartida_set")  # Comentado automáticamente
    # cuenta_rel = relationship("Cuenta", back_populates="dlpartida_set")  # Comentado automáticamente
    # lpartida_rel = relationship("Lpartida", back_populates="dlpartida_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dlpartida(dlpartida={self.dlpartida})>"