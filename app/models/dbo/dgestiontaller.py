# Generado automáticamente
# Tabla: dbo.dGestionTaller
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dgestiontaller(Base):
    __tablename__ = "dGestionTaller"
    __table_args__ = {"schema": "dbo"}

    dGestionTaller = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    GestionTaller = Column(Integer, nullable=False)
    rupfase = Column(Integer, nullable=False)
    ausuario = Column(Integer, nullable=False)
    susuario = Column(Integer, nullable=False)
    finicio = Column(DateTime)
    ffin = Column(DateTime)
    perdida = Column(Numeric(18, 6), nullable=False)
    devolucion = Column(Boolean, nullable=False)
    adicion = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    suspendida = Column(Boolean, nullable=False)
    impresa = Column(Boolean, nullable=False)
    Operadores = Column(Integer, nullable=False)
    estatus = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    ingreso = Column(Boolean, nullable=False)
    salida = Column(Boolean, nullable=False)
    notas = Column(String(250), nullable=False)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    rupstatus = Column(Integer, nullable=False)
    costo = Column(Numeric(18, 6), nullable=False)
    dias = Column(Integer, nullable=False)
    horas = Column(Integer, nullable=False)
    cantidad = Column(Numeric(18, 6), nullable=False)
    mitiempo = Column(Numeric(18, 6), nullable=False)
    resttiempo = Column(Numeric(18, 6), nullable=False)
    factura = Column(Integer, nullable=False)

    # Relaciones
    # gestiontaller = relationship("Gestiontaller", back_populates="dgestiontaller_set")  # Comentado automáticamente
    # rupfase_rel = relationship("Rupfase", back_populates="dgestiontaller_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dgestiontaller(dGestionTaller={self.dGestionTaller})>"