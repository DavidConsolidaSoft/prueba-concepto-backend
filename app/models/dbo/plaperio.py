# Generado automáticamente
# Tabla: dbo.plaperio
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Plaperio(Base):
    __tablename__ = "plaperio"
    __table_args__ = {"schema": "dbo"}

    nplaperio = Column(String(80))
    meses = Column(Integer)
    año = Column(Integer)
    aguinaldo = Column(Boolean)
    vacacion = Column(Boolean)
    activo = Column(Boolean)
    plaperio = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    FINICIO = Column(DateTime)
    FFIN = Column(DateTime)
    f1 = Column(DateTime)
    f2 = Column(DateTime)
    f3 = Column(DateTime)
    f4 = Column(DateTime)
    ndias = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Plaperio(plaperio={self.plaperio})>"