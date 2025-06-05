# Generado automáticamente
# Tabla: dbo.ctrolong
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Ctrolong(Base):
    __tablename__ = "ctrolong"
    __table_args__ = {"schema": "dbo"}

    nctrolong = Column(String(25), nullable=False)
    longitud = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    ctrolong = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    rubro = Column(Boolean, nullable=False)
    grupo = Column(Boolean, nullable=False)
    nivel1 = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Ctrolong(ctrolong={self.ctrolong})>"