# Generado automáticamente
# Tabla: dbo.ctalong
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Ctalong(Base):
    __tablename__ = "ctalong"
    __table_args__ = {"schema": "dbo"}

    nctalong = Column(String(25), nullable=False)
    longitud = Column(Integer, nullable=False)
    mayor = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    ctalong = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    simctalong = Column(String(4), nullable=False)
    rubro = Column(Boolean, nullable=False)
    grupo = Column(Boolean, nullable=False)
    nivel1 = Column(Boolean, nullable=False)
    nivel2 = Column(Boolean, nullable=False)
    nivelGasto = Column(Boolean, nullable=False)
    sub01 = Column(Boolean, nullable=False)
    sub02 = Column(Boolean, nullable=False)
    longoriginal = Column(Integer, nullable=False)
    nwLong = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Ctalong(ctalong={self.ctalong})>"