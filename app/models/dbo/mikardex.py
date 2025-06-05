# Generado automáticamente
# Tabla: dbo.mikardex
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Mikardex(Base):
    __tablename__ = "mikardex"
    __table_args__ = {"schema": "dbo"}

    kardex = Column(Integer, nullable=False)
    nproducto = Column(String(50), nullable=False)
    producto = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    ini = Column(Numeric(16, 6), nullable=False)
    compra = Column(Numeric(16, 6), nullable=False)
    ing = Column(Numeric(16, 6), nullable=False)
    vent = Column(Numeric(16, 6), nullable=False)
    bonif = Column(Numeric(16, 6), nullable=False)
    out = Column(Numeric(16, 6), nullable=False)
    devo = Column(Numeric(16, 6), nullable=False)
    exist = Column(Numeric(16, 6), nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    vexi = Column(Numeric(16, 6), nullable=False)
    ncasa = Column(String(35), nullable=False)
    npresenta = Column(String(40), nullable=False)
    ncategori = Column(String(40), nullable=False)
    nbodega = Column(String(50), nullable=False)
    ntipoprod = Column(String(40), nullable=False)
    codbarra = Column(String(25), nullable=False)
    icdbarra = Column(String(25), nullable=False)
    mikardex = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Mikardex(mikardex={self.mikardex})>"