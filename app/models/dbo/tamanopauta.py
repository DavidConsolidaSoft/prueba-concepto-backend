# Generado automáticamente
# Tabla: dbo.TamanoPauta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tamanopauta(Base):
    __tablename__ = "TamanoPauta"
    __table_args__ = {"schema": "dbo"}

    nTamanoPauta = Column(String(35), nullable=False)
    sizePauta = Column(Integer, nullable=False)
    TamanoPauta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Tamanopauta(TamanoPauta={self.TamanoPauta})>"