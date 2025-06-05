# Generado automáticamente
# Tabla: dbo.partidavta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Partidavta(Base):
    __tablename__ = "partidavta"
    __table_args__ = {"schema": "dbo"}

    partidavta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    factura = Column(Integer)
    partida = Column(Integer)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Partidavta(partidavta={self.partidavta})>"