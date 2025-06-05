# Generado automáticamente
# Tabla: dbo.almtaller
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Almtaller(Base):
    __tablename__ = "almtaller"
    __table_args__ = {"schema": "dbo"}

    fechaentrega = Column(DateTime)
    almacen = Column(Integer)
    empresa = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    almtaller = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Almtaller(almtaller={self.almtaller})>"