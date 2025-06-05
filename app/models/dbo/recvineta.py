# Generado automáticamente
# Tabla: dbo.recvineta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Recvineta(Base):
    __tablename__ = "recvineta"
    __table_args__ = {"schema": "dbo"}

    recvineta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    vendedor = Column(Integer, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    pagada = Column(Boolean, nullable=False)
    notas = Column(String(250), nullable=False)
    fecha = Column(DateTime, nullable=False)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Recvineta(recvineta={self.recvineta})>"