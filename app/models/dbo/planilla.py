# Generado automáticamente
# Tabla: dbo.planilla
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Planilla(Base):
    __tablename__ = "planilla"
    __table_args__ = {"schema": "dbo"}

    nplanilla = Column(String(60))
    plaperio = Column(Integer)
    plano = Column(Numeric(1, 0))
    nopla = Column(Numeric(1, 0))
    pais = Column(Integer)
    fechaemi = Column(DateTime)
    moneda = Column(Integer)
    totaldev = Column(Numeric(18, 6))
    totalded = Column(Numeric(18, 6))
    dias = Column(Boolean)
    tipopla = Column(Integer)
    activo = Column(Boolean)
    comentario = Column(String(50))
    contabilidad = Column(Boolean)
    patrono = Column(Integer)
    planilla = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    noplanilla = Column(String(1))
    totaldevseg = Column(Numeric(18, 6))
    totaldedseg = Column(Numeric(18, 6))
    empresa = Column(Integer)
    impresa = Column(Boolean)
    nula = Column(Boolean)
    FINICIO = Column(DateTime)
    FFIN = Column(DateTime)
    ndias = Column(Integer)
    montoapagar = Column(Numeric(16, 8))
    nopersonas = Column(Integer)
    sueldo = Column(Numeric(16, 9))
    fpago = Column(DateTime)
    identificapla = Column(Integer, nullable=False)
    IdPlanillaNormal = Column(Integer, nullable=False)
    recalculo = Column(Boolean, nullable=False)
    fecha1 = Column(DateTime)
    fecha2 = Column(DateTime)
    midia = Column(Integer)

    # Relaciones
    # plaperio_rel = relationship("Plaperio", back_populates="planilla_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Planilla(planilla={self.planilla})>"