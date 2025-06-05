# Generado automáticamente
# Tabla: dbo.polpladeduc
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Polpladeduc(Base):
    __tablename__ = "polpladeduc"
    __table_args__ = {"schema": "dbo"}

    npolpladeduc = Column(String(100), nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    polpladeduc = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    deley = Column(Boolean, nullable=False)
    aguinaldo = Column(Boolean, nullable=False)
    indemnizacion = Column(Boolean, nullable=False)
    vacacion = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Polpladeduc(polpladeduc={self.polpladeduc})>"