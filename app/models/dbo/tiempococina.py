# Generado automáticamente
# Tabla: dbo.tiempococina
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Tiempococina(Base):
    __tablename__ = "tiempococina"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    tiempoInicio = Column(DateTime, nullable=False)
    dfactura = Column(Integer, nullable=False)
    tiempococina = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Tiempococina(tiempococina={self.tiempococina})>"