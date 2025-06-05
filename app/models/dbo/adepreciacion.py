# Generado automáticamente
# Tabla: dbo.adepreciacion
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Adepreciacion(Base):
    __tablename__ = "adepreciacion"
    __table_args__ = {"schema": "dbo"}

    mes = Column(Integer, nullable=False)
    montodepreciado = Column(Numeric(18, 6), nullable=False)
    aproducto = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    adepreciacion = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    anio = Column(Integer, nullable=False)
    fecha = Column(DateTime)

    def __repr__(self):
        return "<Adepreciacion(adepreciacion={self.adepreciacion})>"