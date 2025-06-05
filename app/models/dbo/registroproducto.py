# Generado automáticamente
# Tabla: dbo.RegistroProducto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Registroproducto(Base):
    __tablename__ = "RegistroProducto"
    __table_args__ = {"schema": "dbo"}

    compra = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    serie = Column(String(25), nullable=False)
    cantidad = Column(Numeric(18, 6), nullable=False)
    fechaVence = Column(DateTime)
    bodega = Column(Integer, nullable=False)
    registoProducto = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)

    # Relaciones
    # producto_rel = relationship("Producto", back_populates="registroproducto_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Registroproducto(compra={self.compra})>"