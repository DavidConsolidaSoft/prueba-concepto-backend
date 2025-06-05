# Generado automáticamente
# Tabla: dbo.asignafull
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Asignafull(Base):
    __tablename__ = "asignafull"
    __table_args__ = {"schema": "dbo"}

    producto = Column(Integer, nullable=False)
    fecha1 = Column(DateTime)
    fecha2 = Column(DateTime)
    clientes = Column(String(25), nullable=False)
    factor = Column(Numeric(18, 6), nullable=False)
    asignaFull = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    prodprec = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Asignafull(asignaFull={self.asignaFull})>"