# Generado automáticamente
# Tabla: dbo.dprodDevolucion
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dproddevolucion(Base):
    __tablename__ = "dprodDevolucion"
    __table_args__ = {"schema": "dbo"}

    dprodDevolucion = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dProdEntregado = Column(Integer, nullable=False)
    Serie = Column(String(50), nullable=False)
    fechagarantia = Column(DateTime)
    garantia = Column(Numeric(6, 2))
    Vencida = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Dproddevolucion(dprodDevolucion={self.dprodDevolucion})>"