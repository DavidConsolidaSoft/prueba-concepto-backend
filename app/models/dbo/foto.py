# Generado automáticamente
# Tabla: dbo.foto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer
from sqlalchemy import Column, LargeBinary
from sqlalchemy import Column, String


class Foto(Base):
    __tablename__ = "foto"
    __table_args__ = {"schema": "dbo"}

    idfoto = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    foto = Column(LargeBinary)
    nombre = Column(String(50))

    def __repr__(self):
        return "<Foto(idfoto={self.idfoto})>"