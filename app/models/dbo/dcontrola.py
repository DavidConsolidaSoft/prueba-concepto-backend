# Generado automáticamente
# Tabla: dbo.dcontrola
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Dcontrola(Base):
    __tablename__ = "dcontrola"
    __table_args__ = {"schema": "dbo"}

    tabla = Column(String(50), nullable=False)
    equipo = Column(String(50), nullable=False)
    Nuevo = Column(Boolean, nullable=False)
    modificar = Column(Boolean, nullable=False)
    eliminar = Column(Boolean, nullable=False)
    dcontrola = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    aplicacion = Column(String(50))

    def __repr__(self):
        return "<Dcontrola(dcontrola={self.dcontrola})>"