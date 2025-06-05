# Generado automáticamente
# Tabla: dbo.TipoPago
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipopago(Base):
    __tablename__ = "TipoPago"
    __table_args__ = {"schema": "dbo"}

    ntipopago = Column(String(35), nullable=False)
    TipoPago = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Tipopago(TipoPago={self.TipoPago})>"