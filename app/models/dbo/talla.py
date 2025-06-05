# Generado automáticamente
# Tabla: dbo.Talla
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Talla(Base):
    __tablename__ = "Talla"
    __table_args__ = {"schema": "dbo"}

    talla = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    talla1 = Column(Numeric(5, 2), nullable=False)
    talla2 = Column(Numeric(5, 2), nullable=False)
    talla3 = Column(Numeric(5, 2), nullable=False)
    tallatipo = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Talla(talla={self.talla})>"