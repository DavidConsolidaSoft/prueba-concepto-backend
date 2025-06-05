# Generado automáticamente
# Tabla: dbo.estatus
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Estatus(Base):
    __tablename__ = "estatus"
    __table_args__ = {"schema": "dbo"}

    estatus = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nestatus = Column(String(50), nullable=False)
    noiniciado = Column(Boolean, nullable=False)
    proceso = Column(Boolean, nullable=False)
    terminado = Column(Boolean, nullable=False)
    cancela = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    cimport = Column(Boolean, nullable=False)
    cexport = Column(Boolean, nullable=False)
    portimport = Column(Boolean, nullable=False)
    portexport = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Estatus(estatus={self.estatus})>"