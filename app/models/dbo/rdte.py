# Generado automáticamente
# Tabla: dbo.rdte
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer


class Rdte(Base):
    __tablename__ = "rdte"
    __table_args__ = {"schema": "dbo"}

    dte = Column(Integer, primary_key=True, nullable=False)
    dtabla = Column(Integer, primary_key=True, nullable=False)
    empresa = Column(Integer, primary_key=True, nullable=False)

    def __repr__(self):
        return "<Rdte(dte={self.dte}, dtabla={self.dtabla}, empresa={self.empresa})>"