# Generado automáticamente
# Tabla: dbo.usuarioseccion
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Usuarioseccion(Base):
    __tablename__ = "usuarioseccion"
    __table_args__ = {"schema": "dbo"}

    usuario = Column(Integer, nullable=False)
    seccion = Column(Integer)
    usuarioseccion = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Usuarioseccion(usuarioseccion={self.usuarioseccion})>"