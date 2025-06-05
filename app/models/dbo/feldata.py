# Generado automáticamente
# Tabla: dbo.feldata
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, SmallInteger
from sqlalchemy import Column, String


class Feldata(Base):
    __tablename__ = "feldata"
    __table_args__ = {"schema": "dbo"}

    dte = Column(SmallInteger,primary_key=True)
    ncatalogo = Column(String(50))
    catalogo = Column(String(50))
    scatalogo = Column(String(50))
    descripcion = Column(String(250))
    zcatalogo = Column(String(20))
    tabla = Column(String(50))
    depto = Column(SmallInteger)
    municip = Column(SmallInteger)

    def __repr__(self):
        return "<Feldata(dte={self.dte})>"