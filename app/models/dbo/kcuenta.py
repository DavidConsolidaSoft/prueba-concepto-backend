# Generado automáticamente
# Tabla: dbo.kcuenta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, Float
from sqlalchemy import Column, Integer
from sqlalchemy import Column, SmallInteger
from sqlalchemy import Column, String


class Kcuenta(Base):
    __tablename__ = "kcuenta"
    __table_args__ = {"schema": "dbo"}

    nocuenta = Column(Integer,primary_key=True, nullable=False)
    nocheque = Column(Integer)
    miformato = Column(String(50))
    banco = Column(Boolean, nullable=False)
    proveedor = Column(Boolean, nullable=False)
    provbol = Column(Boolean, nullable=False)
    iva = Column(Boolean, nullable=False)
    ret = Column(SmallInteger, nullable=False)
    Excl = Column(SmallInteger, nullable=False)
    Fovial = Column(SmallInteger, nullable=False)
    Renta = Column(SmallInteger, nullable=False)
    factor = Column(Float, nullable=False)
    debe = Column(Boolean, nullable=False)
    micheque = Column(String(1))
    AplicaRete = Column(SmallInteger, nullable=False)
    REGISTRO = Column(String(50))
    IMPORTACION = Column(SmallInteger, nullable=False)
    misformato = Column(String(50))
    cotrans = Column(String(50), nullable=False)
    lineascheque = Column(SmallInteger, nullable=False)
    nit = Column(String(1))
    giro = Column(String(1))
    razonsoc = Column(String(1))
    email = Column(String(1))
    sitioweb = Column(String(1))
    notas = Column(String(1))
    direccion = Column(String(1))
    PERCEPCION = Column(Boolean, nullable=False)
    CxCProveedor = Column(SmallInteger, nullable=False)
    cuentaCxC = Column(SmallInteger, nullable=False)
    deduccion1 = Column(SmallInteger, nullable=False)
    deduccion1_2 = Column(SmallInteger, nullable=False)
    deduccion2 = Column(SmallInteger, nullable=False)
    AplicaPercepcion = Column(SmallInteger, nullable=False)

    def __repr__(self):
        return "<Kcuenta(nocuenta={self.nocuenta})>"