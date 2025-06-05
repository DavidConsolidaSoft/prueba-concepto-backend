# Generado automáticamente
# Tabla: dbo.impresor
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Impresor(Base):
    __tablename__ = "impresor"
    __table_args__ = {"schema": "dbo"}

    impresor = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nimpresor = Column(String(100), nullable=False)
    factura = Column(Boolean, nullable=False)
    recibo = Column(Boolean, nullable=False)
    bodega = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Impresor(impresor={self.impresor})>"