# Generado automáticamente
# Tabla: dbo.horario
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Horario(Base):
    __tablename__ = "horario"
    __table_args__ = {"schema": "dbo"}

    anio = Column(Integer, nullable=False)
    mes = Column(Integer, nullable=False)
    semana = Column(Integer, nullable=False)
    seccion = Column(Integer, nullable=False)
    jornada = Column(Integer, nullable=False)
    horario = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    midia = Column(Integer, nullable=False)
    grupo = Column(Integer, nullable=False)
    mesint = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Horario(horario={self.horario})>"