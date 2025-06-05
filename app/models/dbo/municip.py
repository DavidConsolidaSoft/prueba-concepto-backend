# Generado automáticamente
# Tabla: dbo.municip
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Municip(Base):
    __tablename__ = "municip"
    __table_args__ = {"schema": "dbo"}

    nmunicip = Column(String(50), nullable=False)
    preferido = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    depto = Column(Integer, nullable=False)
    municip = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    codigo = Column(String(4))

    # Relaciones
    # depto_rel = relationship("Depto", back_populates="municip_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Municip(municip={self.municip})>"