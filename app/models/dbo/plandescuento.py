# Generado automáticamente
# Tabla: dbo.plandescuento
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Plandescuento(Base):
    __tablename__ = "plandescuento"
    __table_args__ = {"schema": "dbo"}

    plandescuento = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    plaperio = Column(Integer)
    empleado = Column(Integer)
    poldesc = Column(Integer)
    monto = Column(Numeric(19, 4))
    montopatrono = Column(Numeric(19, 4))
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)
    tipopla = Column(Integer)
    planilla = Column(Integer)
    dplanilla = Column(Integer)

    def __repr__(self):
        return "<Plandescuento(plandescuento={self.plandescuento})>"