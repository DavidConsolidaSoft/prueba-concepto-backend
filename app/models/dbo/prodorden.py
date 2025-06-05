# Generado automáticamente
# Tabla: dbo.prodorden
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Prodorden(Base):
    __tablename__ = "prodorden"
    __table_args__ = {"schema": "dbo"}

    producto = Column(Integer)
    almacen = Column(Integer)
    fecha = Column(DateTime)
    fechainicio = Column(DateTime)
    fechafin = Column(DateTime)
    estatus = Column(Integer)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    prodorden = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Prodorden(prodorden={self.prodorden})>"