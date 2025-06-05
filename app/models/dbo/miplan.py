# Generado automáticamente
# Tabla: dbo.miplan
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Miplan(Base):
    __tablename__ = "miplan"
    __table_args__ = {"schema": "dbo"}

    miplan = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    misfinanzas = Column(Integer)
    tipoPrograma = Column(Integer)
    dia = Column(Integer)
    mes = Column(Integer)
    vigente = Column(Boolean)
    nula = Column(Boolean)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    # Relaciones
    # misfinanzas_rel = relationship("Misfinanzas", back_populates="miplan_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Miplan(miplan={self.miplan})>"