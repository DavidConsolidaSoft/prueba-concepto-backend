# Generado automáticamente
# Tabla: dbo.diasLaborados
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Diaslaborados(Base):
    __tablename__ = "diasLaborados"
    __table_args__ = {"schema": "dbo"}

    dia = Column(DateTime, nullable=False)
    esdomingo = Column(Boolean, nullable=False)
    esasueto = Column(Boolean, nullable=False)
    espermanente = Column(Boolean, nullable=False)
    diaslaborados = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Diaslaborados(diaslaborados={self.diaslaborados})>"