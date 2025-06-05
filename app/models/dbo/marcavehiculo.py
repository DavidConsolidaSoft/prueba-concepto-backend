# Generado automáticamente
# Tabla: dbo.marcavehiculo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Marcavehiculo(Base):
    __tablename__ = "marcavehiculo"
    __table_args__ = {"schema": "dbo"}

    nmarcavehiculo = Column(String(200), nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    marcavehiculo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Marcavehiculo(marcavehiculo={self.marcavehiculo})>"