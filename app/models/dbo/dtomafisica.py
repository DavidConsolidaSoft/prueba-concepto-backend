# Generado automáticamente
# Tabla: dbo.dtomafisica
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dtomafisica(Base):
    __tablename__ = "dtomafisica"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    kardex = Column(Integer, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    reservado = Column(Numeric(16, 6), nullable=False)
    cuarentena = Column(Numeric(16, 6), nullable=False)
    fcantidad = Column(Numeric(16, 6), nullable=False)
    freservado = Column(Numeric(16, 6), nullable=False)
    fcuarentena = Column(Numeric(16, 6), nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    fcosto = Column(Numeric(16, 6), nullable=False)
    ajustar = Column(Boolean, nullable=False)
    tomafisica = Column(Integer, nullable=False)
    dtomafisica = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    # Relaciones
    # kardex_rel = relationship("Kardex", back_populates="dtomafisica_set")  # Comentado automáticamente
    # tomafisica_rel = relationship("Tomafisica", back_populates="dtomafisica_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dtomafisica(dtomafisica={self.dtomafisica})>"