# Generado automáticamente
# Tabla: dbo.RegistroGarantia
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Registrogarantia(Base):
    __tablename__ = "RegistroGarantia"
    __table_args__ = {"schema": "dbo"}

    Numedocu = Column(String(9), nullable=False)
    fecha = Column(DateTime)
    Clientes = Column(String(25), nullable=False)
    bodeguero = Column(Integer, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    registroGarantia = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)
    notas = Column(String(250))

    def __repr__(self):
        return "<Registrogarantia(registroGarantia={self.registroGarantia})>"