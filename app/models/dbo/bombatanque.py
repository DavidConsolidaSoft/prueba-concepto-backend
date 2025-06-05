# Generado automáticamente
# Tabla: dbo.bombatanque
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Bombatanque(Base):
    __tablename__ = "bombatanque"
    __table_args__ = {"schema": "dbo"}

    bomba = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    Bombatanque = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Bombatanque(Bombatanque={self.Bombatanque})>"