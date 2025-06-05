# Generado automáticamente
# Tabla: dbo.controles
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Controles(Base):
    __tablename__ = "controles"
    __table_args__ = {"schema": "dbo"}

    controles = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ncontroles = Column(String(50), nullable=False)
    duracion = Column(Numeric(18, 2), nullable=False)
    clasificacion = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Controles(controles={self.controles})>"