# Generado automáticamente
# Tabla: dbo.micolor
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Micolor(Base):
    __tablename__ = "micolor"
    __table_args__ = {"schema": "dbo"}

    micolor = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nmicolor = Column(String(15), nullable=False)
    Descripcion = Column(String(25), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    codigocolor = Column(Integer, nullable=False)
    codigoRGB = Column(String(20), nullable=False)
    codR = Column(String(3), nullable=False)
    codG = Column(String(3), nullable=False)
    codB = Column(String(3), nullable=False)

    def __repr__(self):
        return "<Micolor(micolor={self.micolor})>"