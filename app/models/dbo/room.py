# Generado automáticamente
# Tabla: dbo.room
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Room(Base):
    __tablename__ = "room"
    __table_args__ = {"schema": "dbo"}

    nroom = Column(String(5), nullable=False)
    activo = Column(Boolean, nullable=False)
    room = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Room(room={self.room})>"