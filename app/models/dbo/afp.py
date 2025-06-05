# Generado automáticamente
# Tabla: dbo.afp
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Afp(Base):
    __tablename__ = "afp"
    __table_args__ = {"schema": "dbo"}

    nafp = Column(String(50), nullable=False)
    simafp = Column(String(50), nullable=False)
    pais = Column(Integer)
    activo = Column(Boolean, nullable=False)
    afp = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)
    tipo = Column(String(1), nullable=False)

    def __repr__(self):
        return "<Afp(afp={self.afp})>"