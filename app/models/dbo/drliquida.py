# Generado automáticamente
# Tabla: dbo.drliquida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Drliquida(Base):
    __tablename__ = "drliquida"
    __table_args__ = {"schema": "dbo"}

    drliquida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    rliquida = Column(Integer, nullable=False)
    precio = Column(Numeric(16, 6), nullable=False)
    kardex = Column(Integer, nullable=False)
    almacen = Column(Integer, nullable=False)
    pagos = Column(Integer, nullable=False)
    devolucion = Column(Numeric(16, 6), nullable=False)
    venta = Column(Numeric(16, 6), nullable=False)
    vfaltante = Column(Numeric(16, 6), nullable=False)
    saldoliquida = Column(Numeric(16, 6), nullable=False)
    montliquida = Column(Numeric(16, 6), nullable=False)
    recarga = Column(Numeric(16, 6), nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    vefectivo = Column(Numeric(16, 6), nullable=False)
    tvventa = Column(Numeric(16, 6), nullable=False)
    inicial = Column(Numeric(18, 6), nullable=False)
    fisico = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Drliquida(drliquida={self.drliquida})>"