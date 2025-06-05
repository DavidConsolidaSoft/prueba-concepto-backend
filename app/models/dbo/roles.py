# Generado automáticamente
# Tabla: dbo.roles
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Roles(Base):
    __tablename__ = "roles"
    __table_args__ = {"schema": "dbo"}

    roles = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nroles = Column(String(50), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Roles(roles={self.roles})>"