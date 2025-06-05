# Generado automáticamente
# Tabla: dbo.empleado
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, LargeBinary
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Empleado(Base):
    __tablename__ = "empleado"
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
    telefon1 = Column(String(25))
    telefon2 = Column(String(25))
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
    empleado = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    empcubanco = Column(Integer)
    sueldiarioseg = Column(Numeric(18, 6))
    suelmenseg = Column(Numeric(18, 6))
    afpvseg = Column(Numeric(18, 6))
    afpvpseg = Column(Numeric(18, 6))
    empresa = Column(Integer)
    tipoplaza = Column(Integer)
    jubilado = Column(Boolean)
    codreloj = Column(String(25))
    contrato = Column(Boolean, nullable=False)
    gerente = Column(Boolean, nullable=False)
    jefe = Column(Boolean, nullable=False)
    supervisor = Column(Boolean, nullable=False)
    autoriza = Column(Boolean, nullable=False)
    miImagen = Column(String(250))
    ingesp = Column(Integer, nullable=False)
    asegurad = Column(Integer, nullable=False)
    tiposeg = Column(Integer, nullable=False)
    camion = Column(Integer, nullable=False)
    rutacamion = Column(Integer)
    sectorlaboral = Column(Integer, nullable=False)
    tiempo = Column(Integer)
    licNRemu = Column(Boolean)
    IBC = Column(Boolean)
    pensionvejezanti = Column(Boolean)
    pensionadosinobli = Column(Boolean)
    penriesgospro = Column(Boolean)
    docentepub = Column(Boolean)
    cotivoluntariaafi = Column(Numeric(16, 8))
    cotivoluntariaemp = Column(Integer)
    codigobpen = Column(Integer)
    citrab = Column(String(5))
    codigocentrabajo = Column(Numeric(16, 8))
    ingesp1 = Column(Integer)
    ingesp2 = Column(Integer)
    ingesp3 = Column(Integer)
    ingesp4 = Column(Integer)
    ingesp5 = Column(Integer)
    ingesp6 = Column(Integer)
    ingesp7 = Column(Integer)
    nempleado1 = Column(String(100))
    napellido1 = Column(String(100))
    napellido2 = Column(String(100))
    clave = Column(Integer, nullable=False)
    sprofesional = Column(Boolean, nullable=False)
    email = Column(String(50))

    # Relaciones
    # seccion_rel = relationship("Seccion", back_populates="empleado_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Empleado(codisss={self.codisss})>"