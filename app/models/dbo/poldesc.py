# Generado automáticamente
# Tabla: dbo.poldesc
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Poldesc(Base):
    __tablename__ = "poldesc"
    __table_args__ = {"schema": "dbo"}

    npoldesc = Column(String(60), nullable=False)
    pais = Column(Integer)
    aplpat = Column(Boolean, nullable=False)
    procura = Column(Boolean, nullable=False)
    segsoc = Column(Boolean, nullable=False)
    renta = Column(Boolean, nullable=False)
    educa = Column(Boolean, nullable=False)
    otros = Column(Boolean, nullable=False)
    con1 = Column(Boolean, nullable=False)
    con2 = Column(Boolean, nullable=False)
    con3 = Column(Boolean, nullable=False)
    con4 = Column(Boolean, nullable=False)
    con5 = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    perpla = Column(Integer)
    poldesc = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    despensa = Column(Boolean, nullable=False)
    facturacion = Column(Boolean, nullable=False)
    personal = Column(Boolean, nullable=False)
    transporte = Column(Boolean, nullable=False)
    optica = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    tipdeduccion = Column(Integer, nullable=False)
    segurov = Column(Boolean)
    deley = Column(Boolean)
    manual = Column(Boolean)
    segurovida = Column(Boolean, nullable=False)
    banco = Column(Boolean, nullable=False)
    cooperativa = Column(Boolean, nullable=False)
    ORDEN = Column(Integer, nullable=False)
    Aguinaldo = Column(Boolean)
    Indemnizacion = Column(Boolean)
    Vacacion = Column(Boolean)
    Anticipo = Column(Boolean, nullable=False)
    recalculojunio = Column(Boolean, nullable=False)
    recalculodiciembre = Column(Boolean, nullable=False)
    topemax = Column(Numeric(8, 2))

    def __repr__(self):
        return "<Poldesc(poldesc={self.poldesc})>"