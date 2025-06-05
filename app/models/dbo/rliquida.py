# Generado automáticamente
# Tabla: dbo.rliquida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Rliquida(Base):
    __tablename__ = "rliquida"
    __table_args__ = {"schema": "dbo"}

    rliquida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    impresa = Column(Boolean, nullable=False)
    enfirme = Column(Boolean, nullable=False)
    vendedor = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    prodprec = Column(Integer, nullable=False)
    montliquida = Column(Numeric(16, 6), nullable=False)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    vdevolucion = Column(Numeric(16, 6), nullable=False)
    vtventa = Column(Numeric(16, 6), nullable=False)
    efectivo = Column(Numeric(18, 6), nullable=False)
    cheque = Column(Numeric(18, 6), nullable=False)
    remesa = Column(Numeric(18, 6), nullable=False)
    tarjeta = Column(Numeric(18, 6), nullable=False)
    ventacredito = Column(Numeric(18, 6), nullable=False)
    ventaefectivo = Column(Numeric(18, 6), nullable=False)
    horasJornada = Column(Integer, nullable=False)
    horaSalida = Column(String(5), nullable=False)
    motorista = Column(Integer, nullable=False)
    camion = Column(Integer, nullable=False)
    horasExtras = Column(Integer, nullable=False)
    motorista1 = Column(Integer, nullable=False)
    horaSalida1 = Column(String(5), nullable=False)
    horasJornada1 = Column(Integer, nullable=False)
    horasExtras1 = Column(Integer, nullable=False)
    camion1 = Column(Integer, nullable=False)
    notas = Column(String(250), nullable=False)
    horas = Column(Integer, nullable=False)
    horas1 = Column(Integer, nullable=False)
    cienll = Column(Integer, nullable=False)
    cincuentadoll = Column(Integer, nullable=False)
    veintell = Column(Integer, nullable=False)
    diezll = Column(Integer, nullable=False)
    cincoll = Column(Integer, nullable=False)
    unoll = Column(Integer, nullable=False)
    cincuentavos = Column(Integer, nullable=False)
    veintecincovos = Column(Integer, nullable=False)
    diezvos = Column(Integer, nullable=False)
    cincovos = Column(Integer, nullable=False)
    unvos = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Rliquida(rliquida={self.rliquida})>"