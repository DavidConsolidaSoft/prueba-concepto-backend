# Generado automáticamente
# Tabla: dbo.Bodeguero
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Bodeguero(Base):
    __tablename__ = "Bodeguero"
    __table_args__ = {"schema": "dbo"}

    nBodeguero = Column(String(25), nullable=False)
    Bodeguero = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Bodeguero(Bodeguero={self.Bodeguero})>"