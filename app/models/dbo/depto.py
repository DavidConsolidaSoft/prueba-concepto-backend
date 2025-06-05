# Generado automáticamente
# Tabla: dbo.depto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Depto(Base):
    __tablename__ = "depto"
    __table_args__ = {"schema": "dbo"}

    ndepto = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
    preferido = Column(Boolean, nullable=False)
    pais = Column(Integer, nullable=False)
    depto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    codpostal = Column(String(7))
    codigo = Column(String(4))
    cod_postal = Column(String(15))

    # Relaciones
    # pais_rel = relationship("Pais", back_populates="depto_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Depto(depto={self.depto})>"