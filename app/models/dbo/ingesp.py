# Generado automáticamente
# Tabla: dbo.ingesp
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Ingesp(Base):
    __tablename__ = "ingesp"
    __table_args__ = {"schema": "dbo"}

    ningesp = Column(String(50), nullable=False)
    porcentaje = Column(Numeric(8, 4), nullable=False)
    hed = Column(Boolean)
    hen = Column(Boolean)
    nocturnida = Column(Boolean)
    vacaciones = Column(Boolean)
    aguinaldo = Column(Boolean)
    indemnizac = Column(Boolean)
    activo = Column(Boolean)
    ingesp = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    tabla = Column(Boolean, nullable=False)
    hevacacion = Column(Numeric(16, 6), nullable=False)
    hev = Column(Boolean)
    hedom = Column(Boolean)
    factornocturna = Column(Numeric(18, 6))
    hnormal = Column(Numeric(18, 6), nullable=False)
    hextra = Column(Numeric(18, 6), nullable=False)
    notas = Column(String(200))
    notrabajo = Column(Boolean, nullable=False)
    politaller = Column(Boolean, nullable=False)
    horario = Column(String(25))
    factorhnormal = Column(Numeric(18, 6))
    fijo = Column(Numeric(12, 2))

    def __repr__(self):
        return "<Ingesp(ingesp={self.ingesp})>"