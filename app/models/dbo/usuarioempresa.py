# Generado automáticamente
# Tabla: dbo.usuarioEmpresa
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Usuarioempresa(Base):
    __tablename__ = "usuarioEmpresa"
    __table_args__ = {"schema": "dbo"}

    usuario = Column(Integer)
    empresa = Column(Integer)
    usuarioEmpresa = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    rempresa = Column(Integer, nullable=False)
    rusuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Usuarioempresa(usuarioEmpresa={self.usuarioEmpresa})>"