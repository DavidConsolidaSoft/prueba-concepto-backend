# Generado automáticamente
# Tabla: dbo.ControlRegistro
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Controlregistro(Base):
    __tablename__ = "ControlRegistro"
    __table_args__ = {"schema": "dbo"}

    ControlRegistro = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    modulo = Column(Integer, nullable=False)
    netdata = Column(String(45), nullable=False)
    Activo = Column(Boolean, nullable=False)
    Empresa = Column(Integer, nullable=False)
    Usuario = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Controlregistro(ControlRegistro={self.ControlRegistro})>"