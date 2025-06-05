# Generado automáticamente
# Tabla: dbo.planPrestamo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Planprestamo(Base):
    __tablename__ = "planPrestamo"
    __table_args__ = {"schema": "dbo"}

    planPrestamo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    plaperio = Column(Integer)
    prestemp = Column(Integer)
    monto = Column(Numeric(19, 4))
    montopatrono = Column(Numeric(19, 4))
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)
    tipopla = Column(Integer)
    empleado = Column(Integer)
    planilla = Column(Integer)
    numero = Column(Integer)
    dplanilla = Column(Integer)

    def __repr__(self):
        return "<Planprestamo(planPrestamo={self.planPrestamo})>"