# Generado automáticamente
# Tabla: dbo.kardex
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Kardex(Base):
    __tablename__ = "kardex"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    producto = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    lote = Column(Integer, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    reservado = Column(Numeric(16, 6), nullable=False)
    cuarentena = Column(Numeric(16, 6), nullable=False)
    fcantidad = Column(Numeric(16, 6), nullable=False)
    freservado = Column(Numeric(16, 6), nullable=False)
    fcuarentena = Column(Numeric(16, 6), nullable=False)
    ajuste = Column(Boolean, nullable=False)
    nota = Column(String(200), nullable=False)
    kardex = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    preparaJornada = Column(Integer, nullable=False)
    corridaA1 = Column(Integer, nullable=False)
    corridaA2 = Column(Integer, nullable=False)
    corridaA3 = Column(Integer, nullable=False)
    corridaA4 = Column(Integer, nullable=False)
    corridaA5 = Column(Integer, nullable=False)
    corridaA6 = Column(Integer, nullable=False)
    corridaA7 = Column(Integer, nullable=False)
    corridaA8 = Column(Integer, nullable=False)
    totalEscala = Column(Integer, nullable=False)
    ocCantidad = Column(Numeric(18, 6), nullable=False)
    docompra = Column(Integer, nullable=False)
    docompra1 = Column(Integer, nullable=False)

    # Relaciones
    # bodega_rel = relationship("Bodega", back_populates="kardex_set")  # Comentado automáticamente
    # lote_rel = relationship("Lote", back_populates="kardex_set")  # Comentado automáticamente
    # producto_rel = relationship("Producto", back_populates="kardex_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Kardex(kardex={self.kardex})>"