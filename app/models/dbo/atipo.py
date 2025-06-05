# Generado automáticamente
# Tabla: dbo.atipo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Atipo(Base):
    __tablename__ = "atipo"
    __table_args__ = {"schema": "dbo"}

    descripcion = Column(String(100), nullable=False)
    tasaresidual = Column(Numeric(18, 6), nullable=False)
    tasardepreciacion = Column(Numeric(18, 6), nullable=False)
    anios = Column(Integer, nullable=False)
    criterio = Column(Integer, nullable=False)
    cuenta = Column(Integer, nullable=False)
    ctrocosto = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    atipo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Atipo(atipo={self.atipo})>"