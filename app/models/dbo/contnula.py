# Generado automáticamente
# Tabla: dbo.contnula
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Contnula(Base):
    __tablename__ = "contnula"
    __table_args__ = {"schema": "dbo"}

    motivo = Column(String(60), nullable=False)
    fecha = Column(DateTime, nullable=False)
    contrato = Column(Integer, nullable=False)
    contnula = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    # Relaciones
    # contrato_rel = relationship("Contrato", back_populates="contnula_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Contnula(contnula={self.contnula})>"