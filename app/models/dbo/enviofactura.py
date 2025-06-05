# Generado automáticamente
# Tabla: dbo.envioFactura
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Enviofactura(Base):
    __tablename__ = "envioFactura"
    __table_args__ = {"schema": "dbo"}

    factura = Column(Integer, nullable=False)
    cambodega = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    envioFactura = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    dfactura = Column(Integer)
    dcambodega = Column(Integer)

    def __repr__(self):
        return "<Enviofactura(envioFactura={self.envioFactura})>"