# Generado automáticamente
# Tabla: dbo.seccion
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Seccion(Base):
    __tablename__ = "seccion"
    __table_args__ = {"schema": "dbo"}

    nseccion = Column(String(80), nullable=False)
    produccion = Column(Boolean, nullable=False)
    administracion = Column(Boolean, nullable=False)
    gerencia = Column(Boolean, nullable=False)
    otros = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    seccion = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    correlisss = Column(String(10), nullable=False)
    taller = Column(Boolean, nullable=False)
    reloj = Column(Boolean, nullable=False)
    sabsinhorario = Column(Boolean, nullable=False)
    nhorassab = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Seccion(seccion={self.seccion})>"