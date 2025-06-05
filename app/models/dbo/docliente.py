# Generado automáticamente
# Tabla: dbo.docliente
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Docliente(Base):
    __tablename__ = "docliente"
    __table_args__ = {"schema": "dbo"}

    docompra = Column(Integer)
    clientes = Column(String(25))
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    docliente = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Docliente(docliente={self.docliente})>"