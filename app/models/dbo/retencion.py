# Generado automáticamente
# Tabla: dbo.retencion
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Retencion(Base):
    __tablename__ = "retencion"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    proveedor = Column(Integer, nullable=False)
    numedocu = Column(String(9), nullable=False)
    numedocux = Column(String(9), nullable=False)
    compra = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    nula = Column(Boolean, nullable=False)
    notas = Column(String(150), nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    montfact = Column(Numeric(16, 6), nullable=False)
    retencion = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    nosujeto = Column(Numeric(18, 6), nullable=False)
    percepcion = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Retencion(retencion={self.retencion})>"