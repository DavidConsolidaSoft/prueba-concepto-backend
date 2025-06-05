# Generado automáticamente
# Tabla: dbo.factnula
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Factnula(Base):
    __tablename__ = "factnula"
    __table_args__ = {"schema": "dbo"}

    motivo = Column(String(60), nullable=False)
    fecha = Column(DateTime, nullable=False)
    factura = Column(Integer, nullable=False)
    factnula = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    impresa = Column(Boolean, nullable=False)
    facturareferencia = Column(Integer)

    # Relaciones
    # factura_rel = relationship("Factura", back_populates="factnula_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Factnula(factnula={self.factnula})>"