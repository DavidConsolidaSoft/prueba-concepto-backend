# Generado automáticamente
# Tabla: dbo.ComisionAgencia
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Comisionagencia(Base):
    __tablename__ = "ComisionAgencia"
    __table_args__ = {"schema": "dbo"}

    clientes = Column(String(25), nullable=False)
    fecha1 = Column(DateTime)
    fecha2 = Column(DateTime)
    pDesc = Column(Numeric(5, 2), nullable=False)
    Encomienda = Column(Numeric(16, 6), nullable=False)
    Comision = Column(Numeric(16, 6), nullable=False)
    Retencion = Column(Numeric(16, 6), nullable=False)
    contabilidad = Column(Boolean, nullable=False)
    ComisionAgencia = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    umail = Column(Integer, nullable=False)
    vmail = Column(Numeric(18, 6), nullable=False)
    viatico = Column(Numeric(18, 6), nullable=False)
    otros = Column(Numeric(18, 6), nullable=False)
    noremesado = Column(Numeric(18, 6), nullable=False)
    unulas = Column(Integer, nullable=False)
    nulas = Column(Numeric(18, 6), nullable=False)
    otrosdesc = Column(Numeric(18, 6), nullable=False)
    banco = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    mes = Column(DateTime, nullable=False)
    minimo = Column(String(15), nullable=False)
    Maximo = Column(String(15), nullable=False)
    remesado = Column(Numeric(18, 6), nullable=False)
    renta = Column(Numeric(18, 6), nullable=False)
    viva = Column(Numeric(18, 6), nullable=False)
    impresa = Column(Boolean, nullable=False)
    noitems = Column(Integer, nullable=False)
    montfact = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Comisionagencia(ComisionAgencia={self.ComisionAgencia})>"