# Generado automáticamente
# Tabla: dbo.dpolpladeduc
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dpolpladeduc(Base):
    __tablename__ = "dpolpladeduc"
    __table_args__ = {"schema": "dbo"}

    Minimo = Column(Integer, nullable=False)
    Maximo = Column(Integer, nullable=False)
    oper0 = Column(String(1), nullable=False)
    oper1 = Column(String(1), nullable=False)
    oper2 = Column(String(1), nullable=False)
    SueldoDiario = Column(Boolean, nullable=False)
    oper3 = Column(String(1), nullable=False)
    condic0 = Column(Numeric(9, 4), nullable=False)
    oper4 = Column(String(1), nullable=False)
    oper5 = Column(String(1), nullable=False)
    oper6 = Column(String(1), nullable=False)
    condic1 = Column(Numeric(9, 4), nullable=False)
    oper7 = Column(String(1), nullable=False)
    condic2 = Column(Numeric(9, 4), nullable=False)
    oper8 = Column(String(1), nullable=False)
    oper9 = Column(String(1), nullable=False)
    oper10 = Column(String(1), nullable=False)
    oper11 = Column(String(1), nullable=False)
    condic3 = Column(Numeric(9, 4), nullable=False)
    oper12 = Column(String(1), nullable=False)
    condic4 = Column(Numeric(9, 4), nullable=False)
    oper13 = Column(String(1), nullable=False)
    oper14 = Column(String(1), nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    polpladeduc = Column(Integer, nullable=False)
    dpolpladeduc = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    diastrabajo = Column(Boolean, nullable=False)
    dias = Column(Numeric(5, 1), nullable=False)
    ndias = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Dpolpladeduc(dpolpladeduc={self.dpolpladeduc})>"