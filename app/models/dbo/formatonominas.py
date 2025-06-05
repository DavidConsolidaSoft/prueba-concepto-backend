# Generado automáticamente
# Tabla: dbo.FormatoNominas
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Formatonominas(Base):
    __tablename__ = "FormatoNominas"
    __table_args__ = {"schema": "dbo"}

    FormatoNomina = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    nFormatoNomina = Column(String(150))
    fFormatoNomina = Column(String(250))
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Formatonominas(FormatoNomina={self.FormatoNomina})>"