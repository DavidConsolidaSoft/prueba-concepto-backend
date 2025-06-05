# Generado automáticamente
# Tabla: dbo.corrDiezmo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Corrdiezmo(Base):
    __tablename__ = "corrDiezmo"
    __table_args__ = {"schema": "dbo"}

    Corrdiezmo = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    nopedido = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Corrdiezmo(Corrdiezmo={self.Corrdiezmo})>"