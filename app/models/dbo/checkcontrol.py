# Generado automáticamente
# Tabla: dbo.checkcontrol
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Checkcontrol(Base):
    __tablename__ = "checkcontrol"
    __table_args__ = {"schema": "dbo"}

    checkcontrol = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    partida = Column(Integer)
    nocheque_o = Column(Integer)
    nocheque_f = Column(Integer, nullable=False)
    usuario_r = Column(Integer)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fecha_o = Column(DateTime)
    fecha_f = Column(DateTime)

    def __repr__(self):
        return "<Checkcontrol(checkcontrol={self.checkcontrol})>"