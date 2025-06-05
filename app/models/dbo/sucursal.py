# Generado automáticamente
# Tabla: dbo.sucursal
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Sucursal(Base):
    __tablename__ = "sucursal"
    __table_args__ = {"schema": "dbo"}

    ntipoBodega = Column(String(35), nullable=False)
    activo = Column(Boolean)
    tipoBodega = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    principal = Column(Boolean, nullable=False)
    tercero = Column(Boolean, nullable=False)
    quedan = Column(Integer, nullable=False)
    calculosiniva = Column(Boolean, nullable=False)
    direccion = Column(String(250))
    prefijo = Column(String(20))
    prefijo1 = Column(String(20))
    prefijo2 = Column(String(20))
    prefijo3 = Column(String(20))
    prefijo4 = Column(String(20))
    cod_postal = Column(String(15))
    correo = Column(String(50), nullable=False)
    nit = Column(String(20), nullable=False)
    razon_soc = Column(String(60), nullable=False)
    nomb_comercial = Column(String(60), nullable=False)
    nombre_complemento = Column(String(15), nullable=False)
    serie_ini = Column(String(60), nullable=False)
    serie_fin = Column(String(60), nullable=False)
    _correo = Column(String(35))
    _clave = Column(String(35))
    nosucursal = Column(String(4))
    otrodato = Column(String(35))
    puerto = Column(String(5))
    Establecimiento = Column(String(10))
    PuntoVenta = Column(String(10))

    def __repr__(self):
        return "<Sucursal(ntipoBodega={self.ntipoBodega})>"