# Generado automáticamente
# Tabla: dbo.dpoldesc
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dpoldesc(Base):
    __tablename__ = "dpoldesc"
    __table_args__ = {"schema": "dbo"}

    sueldmen = Column(Boolean, nullable=False)
    totdev = Column(Boolean, nullable=False)
    deducafp = Column(Boolean, nullable=False)
    minimo = Column(Numeric(19, 4), nullable=False)
    maximo = Column(Numeric(19, 4), nullable=False)
    oper0 = Column(String(1), nullable=False)
    oper1 = Column(String(1), nullable=False)
    condic1 = Column(Numeric(9, 4), nullable=False)
    oper2 = Column(String(1), nullable=False)
    condic2 = Column(Numeric(9, 4), nullable=False)
    oper3 = Column(String(1), nullable=False)
    condic3 = Column(Numeric(9, 4), nullable=False)
    oper4 = Column(String(1), nullable=False)
    condic4 = Column(Numeric(9, 4), nullable=False)
    oper5 = Column(String(1), nullable=False)
    condic5 = Column(Numeric(9, 4), nullable=False)
    oper6 = Column(String(1), nullable=False)
    oper7 = Column(String(1), nullable=False)
    oper8 = Column(String(1), nullable=False)
    oper9 = Column(String(1), nullable=False)
    oper10 = Column(String(1), nullable=False)
    oper11 = Column(String(1), nullable=False)
    oper12 = Column(String(1), nullable=False)
    oper13 = Column(String(1), nullable=False)
    activo = Column(Boolean, nullable=False)
    poldesc = Column(Integer)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    minimoseg = Column(Numeric(19, 4), nullable=False)
    maximoseg = Column(Numeric(19, 4), nullable=False)
    condic1seg = Column(Numeric(9, 4), nullable=False)
    condic2seg = Column(Numeric(9, 4), nullable=False)
    condic3seg = Column(Numeric(9, 4), nullable=False)
    condic4seg = Column(Numeric(9, 4), nullable=False)
    condic5seg = Column(Numeric(9, 4), nullable=False)
    dpoldesc = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dias = Column(Integer)

    def __repr__(self):
        return "<Dpoldesc(dpoldesc={self.dpoldesc})>"