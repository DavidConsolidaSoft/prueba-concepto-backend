# Generado automáticamente
# Tabla: dbo.midia
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Midia(Base):
    __tablename__ = "midia"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime, nullable=False)
    mes = Column(String(50), nullable=False)
    dia = Column(String(50), nullable=False)
    semana = Column(Integer, nullable=False)
    midia = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Midia(midia={self.midia})>"