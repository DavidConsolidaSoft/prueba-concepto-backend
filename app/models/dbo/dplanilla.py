# Generado automáticamente
# Tabla: dbo.dplanilla
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dplanilla(Base):
    __tablename__ = "dplanilla"
    __table_args__ = {"schema": "dbo"}

    empleado = Column(Integer)
    tipoprest = Column(Integer)
    poldesc = Column(Integer)
    afp = Column(Integer)
    afpcomision = Column(Numeric(18, 9))
    afppension = Column(Numeric(18, 9))
    totdedvp = Column(Numeric(18, 9))
    totdedv = Column(Numeric(18, 9))
    ingreso = Column(Integer)
    totded = Column(Numeric(18, 9))
    totdev = Column(Numeric(18, 9))
    totdedp = Column(Numeric(18, 9))
    activo = Column(Boolean)
    prestemp = Column(Integer)
    planilla = Column(Integer)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    totdevseg = Column(Numeric(18, 6))
    totdedseg = Column(Numeric(18, 6))
    dplanilla = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer)
    HEDiurnas = Column(Numeric(18, 9))
    HENocturna = Column(Numeric(18, 9))
    hedprecio = Column(Numeric(18, 9))
    henprecio = Column(Numeric(18, 9))
    viaticos = Column(Numeric(18, 9))
    tisss = Column(Numeric(18, 9))
    tafp = Column(Numeric(18, 9))
    trenta = Column(Numeric(18, 9))
    totros = Column(Numeric(18, 9))
    montoapagar = Column(Numeric(18, 9))
    dias = Column(Integer)
    comision = Column(Numeric(18, 6))
    suelmen = Column(Numeric(18, 6))
    otrosing = Column(Numeric(18, 6))
    prestamos = Column(Numeric(18, 6))
    despensa = Column(Numeric(18, 9))
    sueldiario = Column(Numeric(18, 8))
    FAGUIPAGADO = Column(DateTime)
    AGUINALDO = Column(Numeric(18, 9))
    vacacion = Column(Numeric(18, 6))
    AGUIPAGADO = Column(Numeric(18, 9))
    pisss = Column(Numeric(18, 9))
    pafp = Column(Numeric(18, 9))
    indemnizacion = Column(Numeric(16, 6), nullable=False)
    INCAPACIDAD = Column(Integer, nullable=False)
    VINCAPACIDAD = Column(Numeric(16, 6), nullable=False)
    TRABAJADOS = Column(Boolean, nullable=False)
    originaldias = Column(Integer, nullable=False)
    Alimentacion = Column(Numeric(18, 9))
    gratificacion = Column(Numeric(18, 9))
    HEF = Column(Numeric(18, 9))
    Segurov = Column(Numeric(18, 9))
    Transporte = Column(Numeric(18, 9))
    hevprecio = Column(Numeric(18, 9))
    hev = Column(Numeric(18, 9))
    hedomprecio = Column(Numeric(18, 9))
    hedom = Column(Numeric(18, 9))
    valHE = Column(Numeric(18, 6), nullable=False)
    seccion = Column(Integer, nullable=False)
    DTOTROS = Column(Numeric(18, 6), nullable=False)
    totalaguinaldo = Column(Numeric(18, 6), nullable=False)
    totalvacaciones = Column(Numeric(18, 6), nullable=False)
    totalindemnizacion = Column(Numeric(18, 6), nullable=False)
    cooperativa = Column(Numeric(18, 6), nullable=False)
    horasjornada = Column(Integer, nullable=False)
    COBISSS = Column(Integer, nullable=False)
    anios = Column(Integer)
    rentajunio = Column(Numeric(18, 6), nullable=False)
    rentadiciembre = Column(Numeric(18, 6), nullable=False)

    # Relaciones
    # planilla_rel = relationship("Planilla", back_populates="dplanilla_set")  # Comentado automáticamente
    # planilla_rel = relationship("Planilla", back_populates="dplanilla_set")  # Comentado automáticamente
    # seccion_rel = relationship("Seccion", back_populates="dplanilla_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dplanilla(dplanilla={self.dplanilla})>"