# Generado automáticamente
# Tabla: dbo.controlvence
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Controlvence(Base):
    __tablename__ = "controlvence"
    __table_args__ = {"schema": "dbo"}

    controlvence = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    miusuario = Column(Integer, nullable=False)
    notas1 = Column(String(250), nullable=False)
    notas2 = Column(String(250), nullable=False)
    fecha = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    clientes = Column(String(25), nullable=False)
    atendio = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Controlvence(controlvence={self.controlvence})>"