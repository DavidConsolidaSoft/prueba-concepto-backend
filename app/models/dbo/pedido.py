# Generado automáticamente
# Tabla: dbo.pedido
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
from sqlalchemy import Column, Text


class Pedido(Base):
    __tablename__ = "pedido"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    fecha = Column(DateTime, nullable=False)
    documento = Column(String(15), nullable=False)
    clientes = Column(String(25), nullable=False)
    nentregas = Column(Numeric(2, 0), nullable=False)
    terminado = Column(Boolean, nullable=False)
    cancelado = Column(Boolean, nullable=False)
    fecharecib = Column(DateTime)
    fechalimite = Column(DateTime)
    fechadesp = Column(DateTime)
    tipovta = Column(Integer, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nota = Column(Text, nullable=False)
    pedido = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    timestamp = Column(DateTime)

    def __repr__(self):
        return "<Pedido(pedido={self.pedido})>"