# Generado automáticamente
# Tabla: dbo.prodplanta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Prodplanta(Base):
    __tablename__ = "prodplanta"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime)
    bodega = Column(Integer)
    empleado = Column(Integer)
    producto = Column(Integer)
    precio = Column(Numeric(12, 6))
    pextra = Column(Numeric(12, 6))
    pagado = Column(Boolean, nullable=False)
    cantidad = Column(Numeric(12, 2))
    extra = Column(Numeric(12, 2))
    empresa = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    prodplanta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    notas = Column(String(250))
    dplanilla = Column(Integer)
    bextra = Column(Boolean)
    almacen = Column(Integer)

    def __repr__(self):
        return "<Prodplanta(prodplanta={self.prodplanta})>"