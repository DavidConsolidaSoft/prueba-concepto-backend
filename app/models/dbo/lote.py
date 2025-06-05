# Generado automáticamente
# Tabla: dbo.lote
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Lote(Base):
    __tablename__ = "lote"
    __table_args__ = {"schema": "dbo"}

    nolote = Column(String(20), nullable=False)
    activo = Column(Boolean, nullable=False)
    fecvence = Column(DateTime)
    fecingreso = Column(DateTime)
    lote = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    pureza = Column(Numeric(18, 6), nullable=False)
    TipoEscala = Column(Integer, nullable=False)
    TotalEscala = Column(Integer, nullable=False)
    resolucion = Column(String(15), nullable=False)
    corridaA1 = Column(Integer, nullable=False)
    corridaA2 = Column(Integer, nullable=False)
    corridaA3 = Column(Integer, nullable=False)
    corridaA4 = Column(Integer, nullable=False)
    corridaA5 = Column(Integer, nullable=False)
    corridaA6 = Column(Integer, nullable=False)
    corridaA7 = Column(Integer, nullable=False)
    corridaA8 = Column(Integer, nullable=False)
    z1 = Column(Numeric(5, 1))
    z2 = Column(Numeric(5, 1))
    z3 = Column(Numeric(5, 1))
    z4 = Column(Numeric(5, 1))
    z5 = Column(Numeric(5, 1))
    z6 = Column(Numeric(5, 1))
    z7 = Column(Numeric(5, 1))
    z8 = Column(Numeric(5, 1))

    def __repr__(self):
        return "<Lote(lote={self.lote})>"