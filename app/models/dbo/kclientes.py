# Generado automáticamente
# Tabla: dbo.kclientes
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, Float
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Kclientes(Base):
    __tablename__ = "kclientes"
    __table_args__ = {"schema": "dbo"}

    codigo = Column(String(50))
    nclientes = Column(String(150))
    email = Column(String(50))
    propietario = Column(String(150))
    ncondpago = Column(String(100))
    nprodprec = Column(String(100))
    contacto = Column(String(150))
    direccion = Column(String(250))
    razonsoc = Column(String(250))
    registro = Column(String(60))
    giro = Column(String(100))
    nit = Column(String(60))
    telefono1 = Column(String(60))
    telefono2 = Column(String(60))
    limitecredito = Column(Float)
    notas = Column(String(250))
    retencion = Column(Boolean)
    propio = Column(Integer)
    ExcluirCredito = Column(Integer)
    nvendedor = Column(String(60))
    condpago = Column(Integer)
    vendedor = Column(Integer)
    prodprec = Column(Integer,primary_key=True,)

    def __repr__(self):
        return "<Kclientes(codigo={self.codigo})>"