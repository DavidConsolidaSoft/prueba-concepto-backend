# Generado automáticamente
# Tabla: dbo.factvehiculo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer


class Factvehiculo(Base):
    __tablename__ = "factvehiculo"
    __table_args__ = {"schema": "dbo"}

    factvehiculo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    factura = Column(Integer, nullable=False)
    clientedatos = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Factvehiculo(factvehiculo={self.factvehiculo})>"