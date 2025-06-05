# Generado automáticamente
# Tabla: dbo.pedidoalmacen
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Pedidoalmacen(Base):
    __tablename__ = "pedidoalmacen"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    tipomov = Column(Integer, nullable=False)
    numedocu = Column(String(9), nullable=False)
    fecha = Column(DateTime, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    notas = Column(String(150), nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    pedidoalmacen = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    CAJA = Column(Integer)
    bodega = Column(Integer, nullable=False)
    cambodegaReferencia = Column(Integer, nullable=False)
    enviado = Column(Boolean, nullable=False)
    caja2 = Column(Integer, nullable=False)
    cambodega = Column(Integer, nullable=False)

    # Relaciones
    # tipomov_rel = relationship("Tipomov", back_populates="pedidoalmacen_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Pedidoalmacen(pedidoalmacen={self.pedidoalmacen})>"