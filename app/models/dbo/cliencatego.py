# Generado automáticamente
# Tabla: dbo.cliencatego
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Cliencatego(Base):
    __tablename__ = "cliencatego"
    __table_args__ = {"schema": "dbo"}

    ncliencatego = Column(String(40))
    activo = Column(Boolean, nullable=False)
    preferido = Column(Boolean, nullable=False)
    cliencatego = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Cliencatego(cliencatego={self.cliencatego})>"