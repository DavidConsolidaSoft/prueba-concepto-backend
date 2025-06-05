# Generado automáticamente
# Tabla: dbo.lpagosnula
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Lpagosnula(Base):
    __tablename__ = "lpagosnula"
    __table_args__ = {"schema": "dbo"}

    motivo = Column(String(60), nullable=False)
    fecha = Column(DateTime, nullable=False)
    lpagos = Column(Integer, nullable=False)
    lpagosnula = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    impresa = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Lpagosnula(lpagosnula={self.lpagosnula})>"