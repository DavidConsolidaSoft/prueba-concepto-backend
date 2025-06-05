# Generado automáticamente
# Tabla: dbo.caccesos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Caccesos(Base):
    __tablename__ = "caccesos"
    __table_args__ = {"schema": "dbo"}

    ncaccesos = Column(String(250), nullable=False)
    activo = Column(Boolean, nullable=False)
    proceso = Column(Integer, nullable=False)
    micolor = Column(Integer, nullable=False)
    nivel0 = Column(Numeric(18, 6), nullable=False)
    nivel1 = Column(Numeric(18, 6), nullable=False)
    nivel2 = Column(Numeric(18, 6), nullable=False)
    nivel3 = Column(Numeric(18, 6), nullable=False)
    nivel4 = Column(Numeric(18, 6), nullable=False)
    tipoNivel = Column(Integer, nullable=False)
    diasgracia = Column(Integer, nullable=False)
    caccesos = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    nproceso = Column(String(25), nullable=False)
    acceso = Column(Boolean, nullable=False)
    descrip = Column(String(100), nullable=False)
    puedecambiar = Column(Boolean, nullable=False)
    minimo = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Caccesos(ncaccesos={self.ncaccesos})>"