# Generado automáticamente
# Tabla: dbo.cprodprec
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Cprodprec(Base):
    __tablename__ = "cprodprec"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    ncprodprec = Column(String(50), nullable=False)
    fechainicial = Column(DateTime)
    fechafinal = Column(DateTime)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    cprodprec = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Cprodprec(cprodprec={self.cprodprec})>"