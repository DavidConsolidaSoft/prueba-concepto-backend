# Generado automáticamente
# Tabla: dbo.reffecha
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Reffecha(Base):
    __tablename__ = "reffecha"
    __table_args__ = {"schema": "dbo"}

    fechaini = Column(DateTime)
    fechafin = Column(DateTime)
    reffecha = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Reffecha(reffecha={self.reffecha})>"