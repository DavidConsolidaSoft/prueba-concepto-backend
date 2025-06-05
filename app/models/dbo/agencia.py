# Generado automáticamente
# Tabla: dbo.agencia
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Agencia(Base):
    __tablename__ = "agencia"
    __table_args__ = {"schema": "dbo"}

    nagencia = Column(String(50), nullable=False)
    propietario = Column(String(50), nullable=False)
    moneda = Column(Integer, nullable=False)
    tipcli = Column(Integer, nullable=False)
    municip = Column(Integer, nullable=False)
    transpte = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    prodprec = Column(Integer, nullable=False)
    cliencatego = Column(Integer, nullable=False)
    contado = Column(Boolean, nullable=False)
    contacto = Column(String(50), nullable=False)
    direccion = Column(String(200), nullable=False)
    recomendado = Column(String(120), nullable=False)
    activo = Column(Boolean, nullable=False)
    razonsoc = Column(String(50), nullable=False)
    registro = Column(String(15), nullable=False)
    giro = Column(String(50), nullable=False)
    nit = Column(String(20))
    telefono1 = Column(String(25))
    telefono2 = Column(String(15), nullable=False)
    celular = Column(String(15), nullable=False)
    fax = Column(String(15), nullable=False)
    exento = Column(Boolean, nullable=False)
    descuento = Column(Integer, nullable=False)
    email = Column(String(50), nullable=False)
    promcomp = Column(Numeric(16, 6), nullable=False)
    prompago = Column(Numeric(16, 6), nullable=False)
    limitecredito = Column(Numeric(16, 6), nullable=False)
    saldo = Column(String(10), nullable=False)
    hora = Column(DateTime)
    notas = Column(String(250), nullable=False)
    agencia = Column(String(25), primary_key=True, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    retencion = Column(Boolean, nullable=False)
    contrato = Column(Boolean, nullable=False)
    nacimiento = Column(DateTime)
    ivacero = Column(Boolean, nullable=False)
    PROPIO = Column(Boolean, nullable=False)
    PDESC = Column(Numeric(5, 2), nullable=False)
    ZONA = Column(Integer, nullable=False)
    pApellido = Column(String(50))
    sApellido = Column(String(50))
    Nombres = Column(String(50))
    bodega = Column(Integer, nullable=False)
    MESA = Column(Boolean)
    NOPROPINA = Column(Boolean)
    referido = Column(String(25), nullable=False)
    direnvio = Column(String(250), nullable=False)
    agrupaagencia = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    preciovineta = Column(Integer)
    percepcion = Column(Boolean, nullable=False)
    nosujeto = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Agencia(agencia={self.agencia})>"