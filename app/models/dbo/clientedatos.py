# Generado automáticamente
# Tabla: dbo.clientedatos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Clientedatos(Base):
    __tablename__ = "clientedatos"
    __table_args__ = {"schema": "dbo"}

    clientedatos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    clientes = Column(String(25), nullable=False)
    nclientedatos = Column(String(150), nullable=False)
    placa = Column(String(8), nullable=False)
    chasis = Column(String(25), nullable=False)
    fechamatricula = Column(DateTime)
    nolicencia = Column(String(25), nullable=False)
    motor = Column(String(25), nullable=False)
    color = Column(String(25), nullable=False)
    ano = Column(DateTime)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Clientedatos(clientedatos={self.clientedatos})>"