# Generado automáticamente
# Tabla: dbo.polingpla
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Polingpla(Base):
    __tablename__ = "polingpla"
    __table_args__ = {"schema": "dbo"}

    npolingpla = Column(String(60), nullable=False)
    pais = Column(Integer)
    aplpat = Column(Boolean, nullable=False)
    aguinaldo = Column(Boolean, nullable=False)
    vacacion = Column(Boolean, nullable=False)
    indemnizacion = Column(Boolean, nullable=False)
    otros = Column(Boolean, nullable=False)
    con1 = Column(Boolean, nullable=False)
    con2 = Column(Boolean, nullable=False)
    con3 = Column(Boolean, nullable=False)
    con4 = Column(Boolean, nullable=False)
    con5 = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    polingpla = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    tipingpla = Column(Integer, nullable=False)
    salMinimo = Column(Numeric(18, 6))
    SalMaximo = Column(Numeric(18, 6))
    devengado = Column(Boolean)
    manual = Column(Boolean)
    isss = Column(Boolean, nullable=False)
    afp = Column(Boolean, nullable=False)
    renta = Column(Boolean, nullable=False)
    gratificacion = Column(Boolean, nullable=False)
    viaticos = Column(Boolean, nullable=False)
    agricola = Column(Boolean, nullable=False)
    depreciacion = Column(Boolean, nullable=False)
    comision = Column(Boolean, nullable=False)
    ORDEN = Column(Integer, nullable=False)
    ingresofijo = Column(Boolean, nullable=False)
    automatico = Column(Boolean)
    bonodia = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Polingpla(polingpla={self.polingpla})>"