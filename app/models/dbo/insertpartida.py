# Generado automáticamente
# Tabla: dbo.insertPartida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Insertpartida(Base):
    __tablename__ = "insertPartida"
    __table_args__ = {"schema": "dbo"}

    InsertPartida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    opartida = Column(Integer)
    dpartida = Column(Integer)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Insertpartida(InsertPartida={self.InsertPartida})>"