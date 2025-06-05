# Generado automáticamente
# Tabla: dbo.dgetcompra
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dgetcompra(Base):
    __tablename__ = "dgetcompra"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    docompra = Column(Integer, nullable=False)
    precio = Column(Numeric(18, 6), nullable=False)
    cantidad = Column(Numeric(18, 6), nullable=False)
    bonificado = Column(Numeric(18, 6), nullable=False)
    montcomp = Column(Numeric(18, 6), nullable=False)
    hcantidad = Column(Numeric(18, 6), nullable=False)
    hbonificado = Column(Numeric(18, 6), nullable=False)
    hprecio = Column(Numeric(18, 6), nullable=False)
    vcantidad = Column(Numeric(18, 6), nullable=False)
    hmontcomp = Column(Numeric(18, 6), nullable=False)
    pdesc = Column(Numeric(5, 2), nullable=False)
    producto = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    lote = Column(Integer, nullable=False)
    kardex = Column(Integer, nullable=False)
    dgetcompra = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    getcompra = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Dgetcompra(dgetcompra={self.dgetcompra})>"