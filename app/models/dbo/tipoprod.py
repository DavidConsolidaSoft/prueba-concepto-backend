# Generado automáticamente
# Tabla: dbo.tipoprod
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class TipoProd(Base):
    __tablename__ = "tipoprod"
    __table_args__ = {"schema": "dbo"}

    ntipoprod = Column(String(40), nullable=False)
    preferido = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    tipoprod = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    margenminimo = Column(Numeric(16, 6), nullable=False)
    margen = Column(Numeric(16, 6), nullable=False)
    Llanta = Column(Boolean, nullable=False)
    Bateria = Column(Boolean, nullable=False)
    gasolina = Column(Boolean, nullable=False)
    diesel = Column(Boolean, nullable=False)
    implante = Column(Boolean, nullable=False)
    bebidas = Column(Boolean, nullable=False)
    postres = Column(Boolean, nullable=False)
    ensaladas = Column(Boolean, nullable=False)
    principal = Column(Boolean, nullable=False)
    orden = Column(String(6), nullable=False)
    incluir = Column(Boolean, nullable=False)
    adescp = Column(Boolean, nullable=False)
    promosion = Column(Boolean, nullable=False)
    cocina = Column(Boolean, nullable=False)
    mibar = Column(Boolean, nullable=False)
    venta = Column(Boolean, nullable=False)
    otroiva = Column(Boolean, nullable=False)
    desc1 = Column(Integer)
    desc2 = Column(Integer)
    desc3 = Column(Integer)
    desc4 = Column(Integer)
    desc5 = Column(Integer)
    parancel = Column(Numeric(18, 6), nullable=False)
    Margen2 = Column(Numeric(6, 2), nullable=False)
    Margen3 = Column(Numeric(6, 2), nullable=False)
    Margen4 = Column(Numeric(6, 2), nullable=False)
    Margen5 = Column(Numeric(6, 2), nullable=False)
    miimagen = Column(String(150))
    puno = Column(Integer, nullable=False)
    pdos = Column(Integer, nullable=False)
    ptres = Column(Integer, nullable=False)
    pcuatro = Column(Integer, nullable=False)
    pcinco = Column(Integer, nullable=False)
    vol1 = Column(Integer, nullable=False)
    vol2 = Column(Integer, nullable=False)
    vol3 = Column(Integer, nullable=False)
    vol4 = Column(Integer, nullable=False)
    vol5 = Column(Integer, nullable=False)
    fecha1 = Column(DateTime)
    fecha2 = Column(DateTime)
    factor1 = Column(Integer, nullable=False)
    factor2 = Column(Integer, nullable=False)
    factor3 = Column(Integer, nullable=False)
    factor4 = Column(Integer, nullable=False)
    factor5 = Column(Integer, nullable=False)
    image = Column(String(250))

    def __repr__(self):
        return "<Tipoprod(tipoprod={self.tipoprod})>"