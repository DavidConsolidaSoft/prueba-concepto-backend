# Generado automáticamente
# Tabla: dbo.kardex_caja
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class KardexCaja(Base):
    __tablename__ = "kardex_caja"
    __table_args__ = {"schema": "dbo"}

    caja = Column(Integer, nullable=False)
    kardex = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    kardex_caja = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<KardexCaja(kardex_caja={self.kardex_caja})>"