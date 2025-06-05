# Generado automáticamente
# Tabla: dbo.ncpedido
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Ncpedido(Base):
    __tablename__ = "ncpedido"
    __table_args__ = {"schema": "dbo"}

    pedido = Column(Integer, nullable=False)
    ncpedido = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Ncpedido(ncpedido={self.ncpedido})>"