# Generado automáticamente
# Tabla: dbo.tipoincapacidad
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Tipoincapacidad(Base):
    __tablename__ = "tipoincapacidad"
    __table_args__ = {"schema": "dbo"}

    tipoincapacidad = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ntipoincapacidad = Column(String(80))
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)
    vacacion = Column(Boolean, nullable=False)
    incapacidad = Column(Boolean, nullable=False)
    nolaborado = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    factor = Column(Numeric(5, 2), nullable=False)
    factor1 = Column(Numeric(5, 2), nullable=False)
    dias = Column(Integer, nullable=False)
    cobisss = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Tipoincapacidad(tipoincapacidad={self.tipoincapacidad})>"