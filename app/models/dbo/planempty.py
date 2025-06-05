# Generado automáticamente
# Tabla: dbo.planempty
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Planempty(Base):
    __tablename__ = "planempty"
    __table_args__ = {"schema": "dbo"}

    hora = Column(String(6))
    jornada = Column(Boolean)
    content1 = Column(String(255))
    content2 = Column(String(255))
    content3 = Column(String(255))
    content4 = Column(String(255))
    content5 = Column(String(255))
    content6 = Column(String(255))
    content7 = Column(String(255))
    planempty = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Planempty(planempty={self.planempty})>"