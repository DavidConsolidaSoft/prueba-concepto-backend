# Generado automáticamente
# Tabla: dbo.Naturaleza
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Naturaleza(Base):
    __tablename__ = "Naturaleza"
    __table_args__ = {"schema": "dbo"}

    Naturaleza = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nNaturaleza = Column(String(35))
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    Notas = Column(String(250))
    rubro = Column(Integer)
    grupo = Column(Integer)
    nrubro = Column(String(35))

    def __repr__(self):
        return "<Naturaleza(Naturaleza={self.Naturaleza})>"