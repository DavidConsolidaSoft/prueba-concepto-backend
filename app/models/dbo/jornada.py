# Generado automáticamente
# Tabla: dbo.jornada
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Jornada(Base):
    __tablename__ = "jornada"
    __table_args__ = {"schema": "dbo"}

    diurna = Column(Boolean, nullable=False)
    njornada = Column(String(80), nullable=False)
    horasjornada = Column(Numeric(4, 2), nullable=False)
    activo = Column(Boolean, nullable=False)
    jornada = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    MEDIA = Column(Boolean, nullable=False)
    INICIAHE = Column(String(5))
    tiempo = Column(Integer)
    codreloj = Column(String(25))
    HELunes = Column(String(5), nullable=False)
    HSLunes = Column(String(5), nullable=False)
    TDLunes = Column(Integer, nullable=False)
    HEMartes = Column(String(5), nullable=False)
    HSMartes = Column(String(5), nullable=False)
    TDMartes = Column(Integer, nullable=False)
    HEMiercoles = Column(String(5), nullable=False)
    HSMiercoles = Column(String(5), nullable=False)
    TDMiercoles = Column(Integer, nullable=False)
    HEJueves = Column(String(5), nullable=False)
    HSJueves = Column(String(5), nullable=False)
    TDJueves = Column(Integer, nullable=False)
    HEViernes = Column(String(5), nullable=False)
    HSViernes = Column(String(5), nullable=False)
    TDViernes = Column(Integer, nullable=False)
    HESabado = Column(String(5), nullable=False)
    HSSabado = Column(String(5), nullable=False)
    TDSabado = Column(Integer, nullable=False)
    HEDomingo = Column(String(5), nullable=False)
    HSDomingo = Column(String(5), nullable=False)
    TDDomigno = Column(Integer, nullable=False)
    FactorHN = Column(Numeric(18, 6), nullable=False)
    FactorHE = Column(Numeric(18, 6), nullable=False)
    PeriodoGracia = Column(Numeric(18, 6), nullable=False)
    MinCalificaHE = Column(Numeric(18, 6), nullable=False)
    DuracionAlmuerzo = Column(Numeric(18, 6), nullable=False)
    ExcluirHoraAlmuerzo = Column(Boolean, nullable=False)
    TExtraAntesE = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Jornada(jornada={self.jornada})>"