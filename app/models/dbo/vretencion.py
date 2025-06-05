# Generado automáticamente
# Tabla: dbo.vretencion
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Vretencion(Base):
    __tablename__ = "vretencion"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    clientes = Column(String(25), nullable=False)
    numedocu = Column(String(9), nullable=False)
    numedocux = Column(String(9), nullable=False)
    factura = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    nula = Column(Boolean, nullable=False)
    notas = Column(String(150), nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    montfact = Column(Numeric(16, 6), nullable=False)
    vretencion = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Vretencion(vretencion={self.vretencion})>"