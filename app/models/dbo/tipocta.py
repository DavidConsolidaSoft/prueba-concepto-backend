# Generado automáticamente
# Tabla: dbo.tipocta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipocta(Base):
    __tablename__ = "tipocta"
    __table_args__ = {"schema": "dbo"}

    ntipocta = Column(String(20), nullable=False)
    activo = Column(Boolean, nullable=False)
    cheque = Column(Boolean, nullable=False)
    tipocta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer)
    simb = Column(String(10))

    def __repr__(self):
        return "<Tipocta(tipocta={self.tipocta})>"