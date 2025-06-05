# Generado automáticamente
# Tabla: dbo.nochpedido
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Nochpedido(Base):
    __tablename__ = "nochpedido"
    __table_args__ = {"schema": "dbo"}

    pedido = Column(Integer, nullable=False)
    nochpedido = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Nochpedido(nochpedido={self.nochpedido})>"