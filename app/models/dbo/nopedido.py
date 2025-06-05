# Generado automáticamente
# Tabla: dbo.nopedido
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Nopedido(Base):
    __tablename__ = "nopedido"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    pedido = Column(Integer, nullable=False)
    nopedido = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    lotengo = Column(Boolean, nullable=False)
    caja = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Nopedido(nopedido={self.nopedido})>"