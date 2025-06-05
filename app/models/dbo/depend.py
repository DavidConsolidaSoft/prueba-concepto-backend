# Generado automáticamente
# Tabla: dbo.depend
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Depend(Base):
    __tablename__ = "depend"
    __table_args__ = {"schema": "dbo"}

    ndepend = Column(String(80), nullable=False)
    edad = Column(Integer, nullable=False)
    parentes = Column(Integer)
    activo = Column(Boolean, nullable=False)
    empleado = Column(Integer)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer)
    depend = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Depend(depend={self.depend})>"