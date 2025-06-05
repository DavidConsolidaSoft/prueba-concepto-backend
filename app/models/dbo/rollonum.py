# Generado automáticamente
# Tabla: dbo.rollonum
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Rollonum(Base):
    __tablename__ = "rollonum"
    __table_args__ = {"schema": "dbo"}

    novinetas = Column(Integer, nullable=False)
    Noimpresas = Column(Integer, nullable=False)
    perdidas = Column(Integer, nullable=False)
    minimo = Column(Integer, nullable=False)
    maximo = Column(Integer, nullable=False)
    correlativo = Column(Integer, nullable=False)
    rollonum = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Rollonum(rollonum={self.rollonum})>"