# Generado automáticamente
# Tabla: dbo.adistr
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Adistr(Base):
    __tablename__ = "adistr"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    clientes = Column(String(25), nullable=False)
    miembro = Column(String(25), nullable=False)
    anivel = Column(Integer, nullable=False)
    topacio = Column(Boolean, nullable=False)
    zafiro = Column(Boolean, nullable=False)
    esmeralda = Column(Boolean, nullable=False)
    adistr = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    membresia = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fingreso = Column(DateTime)
    bonopag = Column(Boolean)
    bono = Column(Numeric(7, 3), nullable=False)

    def __repr__(self):
        return "<Adistr(adistr={self.adistr})>"