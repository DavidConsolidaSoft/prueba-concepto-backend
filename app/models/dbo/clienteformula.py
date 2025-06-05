# Generado automáticamente
# Tabla: dbo.clienteformula
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Clienteformula(Base):
    __tablename__ = "clienteformula"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    preferido = Column(Boolean, nullable=False)
    mformula = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    clientes = Column(String(25), nullable=False)
    clienteformula = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Clienteformula(clienteformula={self.clienteformula})>"