# Generado automáticamente
# Tabla: dbo.dafp
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dafp(Base):
    __tablename__ = "dafp"
    __table_args__ = {"schema": "dbo"}

    minimo = Column(Numeric(18, 9))
    maximo = Column(Numeric(18, 9))
    totdev = Column(Numeric(18, 9))
    oper1 = Column(String(50))
    condicion1 = Column(Numeric(18, 6))
    oper2 = Column(String(50))
    patronal = Column(Numeric(18, 6))
    activo = Column(Boolean)
    pension = Column(Numeric(18, 6))
    comision = Column(Numeric(18, 6))
    afp = Column(Integer)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    minimoseg = Column(Numeric(18, 6), nullable=False)
    maximoseg = Column(Numeric(18, 6), nullable=False)
    dafp = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    CUOTAEMPLEADO = Column(Numeric(18, 6), nullable=False)
    CUOTAPATRONO = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Dafp(dafp={self.dafp})>"