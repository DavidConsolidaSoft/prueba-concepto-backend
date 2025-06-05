# Generado automáticamente
# Tabla: dbo.facturapagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Facturapagos(Base):
    __tablename__ = "facturapagos"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    factura = Column(Integer, nullable=False)
    pagos = Column(Integer, nullable=False)
    pagosnula = Column(Boolean, nullable=False)
    facturapagos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Facturapagos(facturapagos={self.facturapagos})>"