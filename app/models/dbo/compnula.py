# Generado automáticamente
# Tabla: dbo.compnula
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Compnula(Base):
    __tablename__ = "compnula"
    __table_args__ = {"schema": "dbo"}

    motivo = Column(String(60), nullable=False)
    fecha = Column(DateTime, nullable=False)
    compra = Column(Integer, nullable=False)
    compnula = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    # Relaciones
    # compra_rel = relationship("Compra", back_populates="compnula_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Compnula(compnula={self.compnula})>"