# Generado automáticamente
# Tabla: dbo.dfliquida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dfliquida(Base):
    __tablename__ = "dfliquida"
    __table_args__ = {"schema": "dbo"}

    dfliquida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    factura = Column(Integer, nullable=False)
    clientes = Column(String(25), nullable=False)
    kardex = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    rliquida = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    numedocu = Column(String(25), nullable=False)
    montliquida = Column(Numeric(16, 6), nullable=False)
    prodprec = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Dfliquida(dfliquida={self.dfliquida})>"