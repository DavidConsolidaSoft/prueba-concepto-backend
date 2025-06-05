# Generado automáticamente
# Tabla: dbo.prodentregado
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Prodentregado(Base):
    __tablename__ = "prodentregado"
    __table_args__ = {"schema": "dbo"}

    prodentregado = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    factura = Column(Integer, nullable=False)
    registroproducto = Column(Integer, nullable=False)
    cantidad = Column(Numeric(18, 6), nullable=False)
    garantia = Column(DateTime)
    garantiaprov = Column(DateTime)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)
    dFactura = Column(Integer, nullable=False)
    entregado = Column(Boolean, nullable=False)
    registrogarantia = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Prodentregado(prodentregado={self.prodentregado})>"