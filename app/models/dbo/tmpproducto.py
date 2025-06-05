# Generado automáticamente
# Tabla: dbo.tmpProducto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Tmpproducto(Base):
    __tablename__ = "tmpProducto"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    producto = Column(Integer)
    qinvfin = Column(Numeric(18, 6), nullable=False)
    invfin = Column(Numeric(18, 6), nullable=False)
    costoprom = Column(Numeric(18, 6), nullable=False)
    qcompra = Column(Numeric(18, 6), nullable=False)
    qotrosing = Column(Numeric(18, 6), nullable=False)
    qingreso = Column(Numeric(18, 6), nullable=False)
    qsalida = Column(Numeric(18, 6), nullable=False)
    qventa = Column(Numeric(18, 6), nullable=False)
    qdevol = Column(Numeric(18, 6), nullable=False)
    qbonif = Column(Numeric(18, 6), nullable=False)
    compra = Column(Numeric(18, 6), nullable=False)
    otrosing = Column(Numeric(18, 6), nullable=False)
    ingreso = Column(Numeric(18, 6), nullable=False)
    salida = Column(Numeric(18, 6), nullable=False)
    venta = Column(Numeric(18, 6), nullable=False)
    devol = Column(Numeric(18, 6), nullable=False)
    bonif = Column(Numeric(18, 6), nullable=False)
    invini = Column(Numeric(18, 6), nullable=False)
    qinvini = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Tmpproducto(producto={self.producto})>"