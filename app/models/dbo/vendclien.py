# Generado automáticamente
# Tabla: dbo.vendclien
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Vendclien(Base):
    __tablename__ = "vendclien"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    preferido = Column(Boolean, nullable=False)
    vendedor = Column(Integer, nullable=False)
    clientes = Column(String(25), nullable=False)
    vendclien = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    pdesc = Column(Numeric(5, 2), nullable=False)

    # Relaciones
    # clientes_rel = relationship("Clientes", back_populates="vendclien_set")  # Comentado automáticamente
    # vendedor_rel = relationship("Vendedor", back_populates="vendclien_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Vendclien(vendclien={self.vendclien})>"