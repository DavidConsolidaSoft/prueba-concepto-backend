# Generado automáticamente
# Tabla: dbo.nocpedido
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Nocpedido(Base):
    __tablename__ = "nocpedido"
    __table_args__ = {"schema": "dbo"}

    concepto = Column(String(75), nullable=False)
    activo = Column(Boolean, nullable=False)
    pedido = Column(Integer, nullable=False)
    nocpedido = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Nocpedido(nocpedido={self.nocpedido})>"