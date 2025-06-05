# Generado automáticamente
# Tabla: dbo.JornadaRuta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Jornadaruta(Base):
    __tablename__ = "JornadaRuta"
    __table_args__ = {"schema": "dbo"}

    JornadaRuta = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    nJornadaRuta = Column(String(35))
    activo = Column(Boolean)
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)
    residuos = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Jornadaruta(JornadaRuta={self.JornadaRuta})>"