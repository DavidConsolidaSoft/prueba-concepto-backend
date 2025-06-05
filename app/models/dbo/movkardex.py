# Generado automáticamente
# Tabla: dbo.movkardex
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Movkardex(Base):
    __tablename__ = "movkardex"
    __table_args__ = {"schema": "dbo"}

    kardex = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    nproducto = Column(String(50), nullable=False)
    icdbarra = Column(String(15), nullable=False)
    sgn = Column(String(1), nullable=False)
    fecha = Column(DateTime, nullable=False)
    ntipomov = Column(String(40), nullable=False)
    nbodega = Column(String(50), nullable=False)
    lote = Column(Integer, nullable=False)
    nolote = Column(String(20), nullable=False)
    bodega = Column(Integer, nullable=False)
    doc = Column(String(15), nullable=False)
    aus = Column(Numeric(16, 6), nullable=False)
    avs = Column(Numeric(16, 6), nullable=False)
    ui = Column(Numeric(16, 6), nullable=False)
    uo = Column(Numeric(16, 6), nullable=False)
    us = Column(Numeric(16, 6), nullable=False)
    vi = Column(Numeric(16, 6), nullable=False)
    vo = Column(Numeric(16, 6), nullable=False)
    vs = Column(Numeric(16, 6), nullable=False)
    vc = Column(Numeric(16, 6), nullable=False)
    vcp = Column(Numeric(16, 6), nullable=False)
    cpra = Column(Boolean, nullable=False)
    cod = Column(Integer, nullable=False)
    movkardex = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Movkardex(movkardex={self.movkardex})>"