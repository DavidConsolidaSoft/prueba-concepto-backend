# Generado automáticamente
# Tabla: dbo.PreparaJornada
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Preparajornada(Base):
    __tablename__ = "PreparaJornada"
    __table_args__ = {"schema": "dbo"}

    PreparaJornada = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    JornadaRuta = Column(Integer)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    fecha = Column(DateTime, nullable=False)
    notas = Column(String(255))
    Precio = Column(Numeric(18, 6))
    numtiquet = Column(Integer)
    fnumtiquet = Column(Integer)
    producto = Column(Integer)
    bodega = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Preparajornada(PreparaJornada={self.PreparaJornada})>"