# Generado automáticamente
# Tabla: dbo.dpolingpla
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dpolingpla(Base):
    __tablename__ = "dpolingpla"
    __table_args__ = {"schema": "dbo"}

    sueldodiario = Column(Boolean, nullable=False)
    diaslaborados = Column(Boolean, nullable=False)
    diasanuales = Column(Integer, nullable=False)
    diascalculo = Column(Integer, nullable=False)
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
    polingpla = Column(Integer)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    minimoseg = Column(Numeric(19, 4), nullable=False)
    maximoseg = Column(Numeric(19, 4), nullable=False)
    condic1seg = Column(Numeric(9, 4), nullable=False)
    condic2seg = Column(Numeric(9, 4), nullable=False)
    condic3seg = Column(Numeric(9, 4), nullable=False)
    condic4seg = Column(Numeric(9, 4), nullable=False)
    condic5seg = Column(Numeric(9, 4), nullable=False)
    dpolingpla = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Dpolingpla(dpolingpla={self.dpolingpla})>"