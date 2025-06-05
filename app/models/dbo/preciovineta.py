# Generado automáticamente
# Tabla: dbo.preciovineta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Preciovineta(Base):
    __tablename__ = "preciovineta"
    __table_args__ = {"schema": "dbo"}

    npreciovineta = Column(String(50), nullable=False)
    preferido = Column(Boolean, nullable=False)
    preciovineta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Preciovineta(preciovineta={self.preciovineta})>"