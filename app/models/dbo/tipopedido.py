# Generado automáticamente
# Tabla: dbo.tipopedido
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipopedido(Base):
    __tablename__ = "tipopedido"
    __table_args__ = {"schema": "dbo"}

    ntipopedido = Column(String(40), nullable=False)
    activo = Column(Boolean, nullable=False)
    sinExistencias = Column(Boolean, nullable=False)
    tipoPedido = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Tipopedido(tipoPedido={self.tipoPedido})>"