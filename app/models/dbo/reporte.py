# Generado automáticamente
# Tabla: dbo.reporte
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Reporte(Base):
    __tablename__ = "reporte"
    __table_args__ = {"schema": "dbo"}

    nreporte = Column(String(40), nullable=False)
    encab1 = Column(String(30), nullable=False)
    encab2 = Column(String(30), nullable=False)
    encab3 = Column(String(30), nullable=False)
    columna = Column(Numeric(16, 6), nullable=False)
    encolum1 = Column(String(15), nullable=False)
    encolum2 = Column(String(15), nullable=False)
    encolum3 = Column(String(15), nullable=False)
    encolum4 = Column(String(15), nullable=False)
    encolum5 = Column(String(15), nullable=False)
    encolum6 = Column(String(15), nullable=False)
    tot1 = Column(Boolean, nullable=False)
    tot2 = Column(Boolean, nullable=False)
    tot3 = Column(Boolean, nullable=False)
    tot4 = Column(Boolean, nullable=False)
    tot5 = Column(Boolean, nullable=False)
    repftot = Column(Numeric(16, 6), nullable=False)
    firma1 = Column(String(32), nullable=False)
    firma2 = Column(String(32), nullable=False)
    firma3 = Column(String(32), nullable=False)
    titulo1 = Column(String(32), nullable=False)
    titulo2 = Column(String(32), nullable=False)
    titulo3 = Column(String(32), nullable=False)
    activo = Column(Boolean, nullable=False)
    reporte = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    auto = Column(Integer, nullable=False)
    cTotal1 = Column(String(70), nullable=False)
    cTotal2 = Column(String(70), nullable=False)

    def __repr__(self):
        return "<Reporte(reporte={self.reporte})>"