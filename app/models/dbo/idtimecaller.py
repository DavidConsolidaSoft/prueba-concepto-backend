# Generado automáticamente
# Tabla: dbo.idtimecaller
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Idtimecaller(Base):
    __tablename__ = "idtimecaller"
    __table_args__ = {"schema": "dbo"}

    idtimeCaller = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    fecha = Column(DateTime)
    registro = Column(String(250))
    activo = Column(Boolean)
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Idtimecaller(idtimeCaller={self.idtimeCaller})>"