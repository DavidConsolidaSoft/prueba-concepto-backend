# Generado automáticamente
# Tabla: dbo.dreporte
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dreporte(Base):
    __tablename__ = "dreporte"
    __table_args__ = {"schema": "dbo"}

    filas = Column(Numeric(16, 6), nullable=False)
    impnumc = Column(Boolean, nullable=False)
    nombre = Column(String(60), nullable=False)
    saldant = Column(Numeric(16, 6), nullable=False)
    saldmen = Column(Numeric(16, 6), nullable=False)
    saldacu = Column(Numeric(16, 6), nullable=False)
    anterior = Column(Boolean, nullable=False)
    mensual = Column(Boolean, nullable=False)
    acum = Column(Boolean, nullable=False)
    fila1 = Column(Numeric(16, 6), nullable=False)
    oper1 = Column(String(1), nullable=False)
    fila2 = Column(Numeric(16, 6), nullable=False)
    oper2 = Column(String(1), nullable=False)
    fila3 = Column(Numeric(16, 6), nullable=False)
    oper3 = Column(String(1), nullable=False)
    fila4 = Column(Numeric(16, 6), nullable=False)
    oper4 = Column(String(1), nullable=False)
    expresion1 = Column(String(1), nullable=False)
    oper5 = Column(String(1), nullable=False)
    expresion2 = Column(String(1), nullable=False)
    nivel = Column(String(1), nullable=False)
    columna = Column(Numeric(16, 6), nullable=False)
    inventa = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    raya = Column(Boolean, nullable=False)
    reporte = Column(Integer, nullable=False)
    cuenta = Column(Integer, nullable=False)
    ctrocosto = Column(Integer, nullable=False)
    dreporte = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    oreporte = Column(Integer, nullable=False)
    mimoneda = Column(String(2), nullable=False)
    tipo = Column(String(1), nullable=False)
    fila5 = Column(Integer, nullable=False)
    raya1 = Column(Boolean, nullable=False)
    raya2 = Column(Boolean, nullable=False)
    raya3 = Column(Boolean, nullable=False)
    factor = Column(Numeric(6, 2), nullable=False)

    # Relaciones
    # ctrocosto_rel = relationship("Ctrocosto", back_populates="dreporte_set")  # Comentado automáticamente
    # cuenta_rel = relationship("Cuenta", back_populates="dreporte_set")  # Comentado automáticamente
    # reporte_rel = relationship("Reporte", back_populates="dreporte_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dreporte(dreporte={self.dreporte})>"