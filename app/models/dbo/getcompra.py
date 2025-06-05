# Generado automáticamente
# Tabla: dbo.getcompra
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Getcompra(Base):
    __tablename__ = "getcompra"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    esRecinto = Column(Boolean, nullable=False)
    numedocu = Column(String(15), nullable=False)
    fecha = Column(DateTime, nullable=False)
    cnumedocu = Column(String(15), nullable=False)
    cfecha = Column(DateTime)
    ocompra = Column(Integer, nullable=False)
    compra = Column(Integer, nullable=False)
    caja = Column(Integer, nullable=False)
    recintofiscal = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    notas = Column(String(150), nullable=False)
    getcompra = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    encompra = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Getcompra(getcompra={self.getcompra})>"