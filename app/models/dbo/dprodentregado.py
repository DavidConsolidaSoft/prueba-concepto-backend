# Generado automáticamente
# Tabla: dbo.dprodentregado
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dprodentregado(Base):
    __tablename__ = "dprodentregado"
    __table_args__ = {"schema": "dbo"}

    dprodentregado = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ProdEntregado = Column(Integer, nullable=False)
    Producto = Column(Integer, nullable=False)
    cantidad = Column(Numeric(18, 6), nullable=False)
    Serie = Column(String(50), nullable=False)
    fechagarantia = Column(DateTime)
    garantia = Column(Numeric(6, 2))
    Devolucion = Column(Boolean, nullable=False)
    Vencida = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)
    registrogarantia = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Dprodentregado(dprodentregado={self.dprodentregado})>"