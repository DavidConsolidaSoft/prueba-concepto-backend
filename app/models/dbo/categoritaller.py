# Generado automáticamente
# Tabla: dbo.categoritaller
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Categoritaller(Base):
    __tablename__ = "categoritaller"
    __table_args__ = {"schema": "dbo"}

    ncategoritaller = Column(String(40), nullable=False)
    preferido = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    categoritaller = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    margenminimo = Column(Numeric(16, 6), nullable=False)
    margen = Column(Numeric(16, 6), nullable=False)
    Preventivo = Column(Boolean, nullable=False)
    Correctivo = Column(Boolean, nullable=False)
    diesel = Column(Boolean, nullable=False)
    Recepcion = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Categoritaller(categoritaller={self.categoritaller})>"