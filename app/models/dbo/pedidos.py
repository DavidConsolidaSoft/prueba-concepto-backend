# Generado automáticamente
# Tabla: dbo.pedidos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Pedidos(Base):
    __tablename__ = "pedidos"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    clientes = Column(String(25), nullable=False)
    nclientes = Column(String(50), nullable=False)
    condpago = Column(Integer, nullable=False)
    ncondpago = Column(String(50), nullable=False)
    nvendedor = Column(String(50), nullable=False)
    vendedor = Column(Integer, nullable=False)
    direccion = Column(String(200), nullable=False)
    registro = Column(String(15), nullable=False)
    telefono1 = Column(String(15), nullable=False)
    limitecred = Column(Numeric(19, 4), nullable=False)

    def __repr__(self):
        return "<Pedidos(clientes={self.clientes})>"