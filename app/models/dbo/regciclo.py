# Generado automáticamente
# Tabla: dbo.regciclo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Regciclo(Base):
    __tablename__ = "regciclo"
    __table_args__ = {"schema": "dbo"}

    regciclo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ciclo = Column(String(7), nullable=False)
    activo = Column(Boolean, nullable=False)
    fechaini = Column(DateTime)
    fechafin = Column(DateTime)
    nocuotas = Column(Integer, nullable=False)
    prodprec = Column(Integer, nullable=False)
    impresa = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Regciclo(regciclo={self.regciclo})>"