# Generado automáticamente
# Tabla: dbo.dcompranc
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dcompranc(Base):
    __tablename__ = "dcompranc"
    __table_args__ = {"schema": "dbo"}

    dcompra = Column(Integer)
    descuento = Column(Numeric(9, 2))
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    dcompranc = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    difcambio = Column(Numeric(5, 2))

    def __repr__(self):
        return "<Dcompranc(dcompranc={self.dcompranc})>"