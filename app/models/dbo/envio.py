# Generado automáticamente
# Tabla: dbo.envio
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Envio(Base):
    __tablename__ = "envio"
    __table_args__ = {"schema": "dbo"}

    envio = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nEnvio = Column(String(15), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Envio(envio={self.envio})>"