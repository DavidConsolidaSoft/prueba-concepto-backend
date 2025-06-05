# Generado automáticamente
# Tabla: dbo.emptipla
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Emptipla(Base):
    __tablename__ = "emptipla"
    __table_args__ = {"schema": "dbo"}

    empleado = Column(Integer, nullable=False)
    tipopla = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    emptipla = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer)

    # Relaciones
    # tipopla_rel = relationship("Tipopla", back_populates="emptipla_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Emptipla(emptipla={self.emptipla})>"