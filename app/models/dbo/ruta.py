# Generado automáticamente
# Tabla: dbo.ruta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer
from sqlalchemy import Column, LargeBinary


class Ruta(Base):
    __tablename__ = "ruta"
    __table_args__ = {"schema": "dbo"}

    unidad = Column(LargeBinary, nullable=False)
    ruta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Ruta(ruta={self.ruta})>"