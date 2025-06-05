# Generado automáticamente
# Tabla: dbo.tipopla
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Tipopla(Base):
    __tablename__ = "tipopla"
    __table_args__ = {"schema": "dbo"}

    ntipopla = Column(String(50))
    activo = Column(Boolean, nullable=False)
    afp = Column(Boolean, nullable=False)
    prestamos = Column(Boolean)
    patrono = Column(Integer)
    pais = Column(Integer)
    tipopla = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    pla1 = Column(Boolean)
    pla4 = Column(Boolean)
    pla3 = Column(Boolean)
    pla2 = Column(Boolean)
    enproceso = Column(Boolean)
    ndias = Column(Integer)
    vacacion = Column(Boolean)
    INDEMNIZACION = Column(Boolean)
    granja = Column(Boolean)
    aguinaldo = Column(Boolean)
    Noplanilla = Column(Integer, nullable=False)
    reporte = Column(String(40), nullable=False)
    SALMAX = Column(Numeric(18, 6), nullable=False)
    diasminimos = Column(Integer, nullable=False)
    diasaplicados = Column(Integer, nullable=False)
    porcentaje = Column(Integer, nullable=False)
    plazomeses = Column(Integer, nullable=False)
    maxaguinaldo = Column(Numeric(18, 6), nullable=False)
    reloj = Column(Integer, nullable=False)
    noplaisss = Column(Boolean, nullable=False)
    noplaafp = Column(Boolean, nullable=False)
    hfijo = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Tipopla(tipopla={self.tipopla})>"