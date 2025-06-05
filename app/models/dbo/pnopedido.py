# Generado automáticamente
# Tabla: dbo.pnopedido
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Pnopedido(Base):
    __tablename__ = "pnopedido"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    pedido = Column(Integer, nullable=False)
    nopedido = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    pnopedido = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Pnopedido(pnopedido={self.pnopedido})>"