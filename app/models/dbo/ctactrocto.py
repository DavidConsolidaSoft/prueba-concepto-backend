# Generado automáticamente
# Tabla: dbo.ctactrocto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Ctactrocto(Base):
    __tablename__ = "ctactrocto"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    cuenta = Column(Integer, nullable=False)
    ctrocosto = Column(Integer, nullable=False)
    ctactrocto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    # Relaciones
    # ctrocosto_rel = relationship("Ctrocosto", back_populates="ctactrocto_set")  # Comentado automáticamente
    # cuenta_rel = relationship("Cuenta", back_populates="ctactrocto_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Ctactrocto(ctactrocto={self.ctactrocto})>"