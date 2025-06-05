# Generado automáticamente
# Tabla: dbo.Candidato
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, LargeBinary
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Candidato(Base):
    __tablename__ = "Candidato"
    __table_args__ = {"schema": "dbo"}

    codisss = Column(String(50))
    nempleado = Column(String(50))
    aempleado = Column(String(50))
    nombisss = Column(String(50))
    foto = Column(LargeBinary)
    sexo = Column(Integer)
    nacional = Column(Integer)
    pais = Column(Integer)
    depto = Column(Integer)
    municip = Column(Integer)
    fechnac = Column(DateTime)
    lugarnac = Column(String(50))
    estcivil = Column(Integer)
    profesion = Column(Integer)
    direccemp = Column(String(250))
    telefon1 = Column(String(15))
    telefon2 = Column(String(15))
    tiposan = Column(Integer)
    fechacont = Column(DateTime)
    vencontra = Column(DateTime)
    fecharet = Column(DateTime)
    seccion = Column(Integer)
    cargo = Column(Integer)
    ntarjeta = Column(String(25))
    jornada = Column(Integer)
    sueldiario = Column(Numeric(18, 6))
    suelmen = Column(Numeric(18, 6))
    formpago = Column(Integer)
    nit = Column(String(50))
    cip = Column(String(50))
    carelect = Column(String(50))
    carmino = Column(String(50))
    permintr = Column(String(50))
    liccond = Column(String(50))
    pasaport = Column(String(50))
    numisss = Column(String(50))
    nup = Column(String(50))
    cuentab = Column(String(50))
    tipocta = Column(Integer)
    banco = Column(Integer)
    afp = Column(Integer)
    procurad = Column(Boolean)
    horasext = Column(Boolean)
    notas = Column(String(250))
    activo = Column(Boolean)
    cuenta = Column(Integer)
    ctrocosto = Column(Integer)
    afpv = Column(Numeric(18, 6))
    afpvp = Column(Numeric(18, 6))
    Empleado = Column(Integer)
    Candidato = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    empcubanco = Column(Integer)
    sueldiarioseg = Column(Numeric(18, 6))
    suelmenseg = Column(Numeric(18, 6))
    afpvseg = Column(Numeric(18, 6))
    afpvpseg = Column(Numeric(18, 6))
    empresa = Column(Integer)
    tipoplaza = Column(Integer)
    jubilado = Column(Boolean)
    codreloj = Column(String(25))
    contrato = Column(Boolean)
    gerente = Column(Boolean)
    jefe = Column(Boolean)
    supervisor = Column(Boolean)
    autoriza = Column(Boolean)
    miImagen = Column(String(250))
    aprobadorrhh = Column(Boolean, nullable=False)
    aprobadojefe = Column(Boolean, nullable=False)
    faprobadorrhh = Column(DateTime)
    faprobadojefe = Column(DateTime)

    def __repr__(self):
        return "<Candidato(Candidato={self.Candidato})>"