# Generado automáticamente
# Tabla: dbo.tpfactura
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Tpfactura(Base):
    __tablename__ = "tpfactura"
    __table_args__ = {"schema": "dbo"}

    pfactura = Column(Integer, nullable=False)
    factura = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    tpfactura = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Tpfactura(tpfactura={self.tpfactura})>"