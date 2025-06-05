# Generado automáticamente
# Tabla: dbo.tomafisica
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Tomafisica(Base):
    __tablename__ = "tomafisica"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    tipomov = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    notas = Column(String(150), nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    tomafisica = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    # Relaciones
    # tipomov_rel = relationship("Tipomov", back_populates="tomafisica_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Tomafisica(tomafisica={self.tomafisica})>"