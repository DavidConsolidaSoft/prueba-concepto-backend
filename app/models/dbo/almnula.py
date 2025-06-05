# Generado automáticamente
# Tabla: dbo.almnula
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String
# # from sqlalchemy.orm import relationship  # Comentado temporalmente  # Comentado temporalmente


class Almnula(Base):
    __tablename__ = "almnula"
    __table_args__ = {"schema": "dbo"}

    almacen = Column(Integer, nullable=False)
    motivo = Column(String(60), nullable=False)
    fecha = Column(DateTime, nullable=False)
    almnula = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    # Relaciones
    # # almacen_rel = relationship(...)  # Comentado automáticamente  # Comentado temporalmente

    def __repr__(self):
        return "<Almnula(almnula={self.almnula})>"