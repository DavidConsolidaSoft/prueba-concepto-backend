# Generado automáticamente
# Tabla: dbo.cambnula
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Cambnula(Base):
    __tablename__ = "cambnula"
    __table_args__ = {"schema": "dbo"}

    cambodega = Column(Integer, nullable=False)
    motivo = Column(String(60), nullable=False)
    fecha = Column(DateTime, nullable=False)
    cambnula = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    # Relaciones
    # cambodega_rel = relationship("Cambodega", back_populates="cambnula_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Cambnula(cambnula={self.cambnula})>"