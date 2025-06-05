# Generado automáticamente
# Tabla: dbo.prodprectipcli
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Prodprectipcli(Base):
    __tablename__ = "prodprectipcli"
    __table_args__ = {"schema": "dbo"}

    prodprec = Column(Integer, nullable=False)
    tipcli = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    prodprectipcli = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Relaciones
    # prodprec_rel = relationship("Prodprec", back_populates="prodprectipcli_set")  # Comentado automáticamente
    # tipcli_rel = relationship("Tipcli", back_populates="prodprectipcli_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Prodprectipcli(prodprectipcli={self.prodprectipcli})>"