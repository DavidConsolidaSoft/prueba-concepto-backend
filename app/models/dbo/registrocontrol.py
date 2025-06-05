# Generado automáticamente
# Tabla: dbo.registroControl
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Registrocontrol(Base):
    __tablename__ = "registroControl"
    __table_args__ = {"schema": "dbo"}

    RegistroControl = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    idUsuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    modulo = Column(Integer, nullable=False)
    FinSesion = Column(DateTime)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    equipo = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Registrocontrol(RegistroControl={self.RegistroControl})>"