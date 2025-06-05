# Generado automáticamente
# Tabla: dbo.tipodatotxt
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipodatotxt(Base):
    __tablename__ = "tipodatotxt"
    __table_args__ = {"schema": "dbo"}

    dia = Column(DateTime, nullable=False)
    txt = Column(String(255))
    tipodatotxt = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Tipodatotxt(tipodatotxt={self.tipodatotxt})>"