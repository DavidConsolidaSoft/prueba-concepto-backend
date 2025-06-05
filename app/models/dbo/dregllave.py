# Generado automáticamente
# Tabla: dbo.dregllave
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Dregllave(Base):
    __tablename__ = "dregllave"
    __table_args__ = {"schema": "dbo"}

    dregllave = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    pais = Column(Integer, nullable=False)
    Producto = Column(Integer, nullable=False)
    clientes = Column(String(25), nullable=False)
    dclientes = Column(String(25), nullable=False)
    fecha = Column(DateTime, nullable=False)
    moneda = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    equipo = Column(String(55), nullable=False)
    registro = Column(String(65), nullable=False)
    reinstall = Column(Integer, nullable=False)
    sucursal = Column(String(25), nullable=False)
    email = Column(String(65), nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    notas = Column(String(250), nullable=False)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    noProducto = Column(String(65), nullable=False)
    Llave = Column(String(65), nullable=False)
    IFORMATO = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Dregllave(dregllave={self.dregllave})>"