# Generado automáticamente
# Tabla: dbo.mifecha
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Mifecha(Base):
    __tablename__ = "mifecha"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime, nullable=False)
    mifecha = Column(Integer, primary_key=True, nullable=False)

    def __repr__(self):
        return "<Mifecha(mifecha={self.mifecha})>"