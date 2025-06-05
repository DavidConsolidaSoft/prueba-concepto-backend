# Generado automáticamente
# Tabla: dbo.rutacobro
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Rutacobro(Base):
    __tablename__ = "rutacobro"
    __table_args__ = {"schema": "dbo"}

    vendedor = Column(Integer, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    liquidada = Column(Boolean, nullable=False)
    notas = Column(String(250), nullable=False)
    fecha = Column(DateTime, nullable=False)
    rutacobro = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    saldo = Column(Numeric(18, 6), nullable=False)
    numedocu = Column(Integer, nullable=False)
    entregada = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Rutacobro(rutacobro={self.rutacobro})>"