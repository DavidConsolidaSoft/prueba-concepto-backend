# Generado automáticamente
# Tabla: dbo.clase
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Clase(Base):
    __tablename__ = "clase"
    __table_args__ = {"schema": "dbo"}

    clase = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nClase = Column(String(15), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Clase(clase={self.clase})>"