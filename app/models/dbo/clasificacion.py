# Generado automáticamente
# Tabla: dbo.clasificacion
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Clasificacion(Base):
    __tablename__ = "clasificacion"
    __table_args__ = {"schema": "dbo"}

    Clasificacion = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nclasificacion = Column(String(50), nullable=False)
    riesgoA = Column(Boolean, nullable=False)
    riesgoB = Column(Boolean, nullable=False)
    riesgoC = Column(Boolean, nullable=False)
    duracion = Column(Numeric(18, 2), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Clasificacion(Clasificacion={self.Clasificacion})>"