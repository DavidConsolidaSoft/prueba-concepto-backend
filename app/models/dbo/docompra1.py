# Generado automáticamente
# Tabla: dbo.docompra1
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Docompra1(Base):
    __tablename__ = "docompra1"
    __table_args__ = {"schema": "dbo"}

    producto = Column(Integer, nullable=False)
    docompra = Column(Integer, nullable=False)
    ocompra = Column(Integer, nullable=False)
    recibido = Column(Numeric(18, 6), nullable=False)
    pendiente = Column(Numeric(18, 6), nullable=False)
    nuevoingreso = Column(Numeric(18, 6), nullable=False)
    lote = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    docompra1 = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    dcompra = Column(Integer, nullable=False)
    recibidorecinto = Column(Numeric(18, 6), nullable=False)
    pendienterecinto = Column(Numeric(18, 6), nullable=False)
    nuevoingresorecinto = Column(Numeric(18, 6), nullable=False)
    compra = Column(Integer, nullable=False)
    kardex = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Docompra1(docompra1={self.docompra1})>"