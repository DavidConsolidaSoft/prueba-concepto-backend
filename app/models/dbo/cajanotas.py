# Generado automáticamente
# Tabla: dbo.cajaNotas
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Cajanotas(Base):
    __tablename__ = "cajaNotas"
    __table_args__ = {"schema": "dbo"}

    caja = Column(Integer, primary_key=True)
    Notas = Column(String(250))
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Cajanotas(caja={self.caja})>"