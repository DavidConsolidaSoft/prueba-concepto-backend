# Generado automáticamente
# Tabla: dbo.admoncaja
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Admoncaja(Base):
    __tablename__ = "admoncaja"
    __table_args__ = {"schema": "dbo"}

    admoncaja = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tipoEscala = Column(Integer)
    nocaja = Column(String(20))
    fecha = Column(DateTime)
    fcheck = Column(DateTime)
    fseall = Column(DateTime)
    q1 = Column(Integer)
    q2 = Column(Integer)
    q3 = Column(Integer)
    q4 = Column(Integer)
    q5 = Column(Integer)
    q6 = Column(Integer)
    q7 = Column(Integer)
    q8 = Column(Integer)
    t1 = Column(Numeric(3, 1))
    t2 = Column(Numeric(3, 1))
    t3 = Column(Numeric(3, 1))
    t4 = Column(Numeric(3, 1))
    t5 = Column(Numeric(3, 1))
    t6 = Column(Numeric(3, 1))
    t7 = Column(Numeric(3, 1))
    t8 = Column(Numeric(3, 1))
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    bodega = Column(Numeric(6, 2))
    producto = Column(Numeric(6, 2))
    docompra = Column(Integer)
    enfirme = Column(Numeric(9, 2))
    Tenfirme = Column(DateTime)

    def __repr__(self):
        return "<Admoncaja(admoncaja={self.admoncaja})>"