# Generado automáticamente
# Tabla: dbo.profesion
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Profesion(Base):
    __tablename__ = "profesion"
    __table_args__ = {"schema": "dbo"}

    nprofesion = Column(String(80), nullable=False)
    activo = Column(Boolean, nullable=False)
    profesion = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Profesion(profesion={self.profesion})>"