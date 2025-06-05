# Generado automáticamente
# Tabla: dbo.cuentatipomov
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Cuentatipomov(Base):
    __tablename__ = "cuentatipomov"
    __table_args__ = {"schema": "dbo"}

    Activo = Column(Boolean, nullable=False)
    tipomov = Column(Integer, nullable=False)
    sucursal = Column(Integer, nullable=False)
    cuenta = Column(Integer, nullable=False)
    cuentatipomov = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    cuentaiva = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Cuentatipomov(cuentatipomov={self.cuentatipomov})>"