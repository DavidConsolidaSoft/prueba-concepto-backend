# Generado automáticamente
# Tabla: dbo.autfact
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Autfact(Base):
    __tablename__ = "autfact"
    __table_args__ = {"schema": "dbo"}

    factura = Column(Integer, nullable=False)
    autusr = Column(Integer, nullable=False)
    concepto = Column(String(40), nullable=False)
    valor = Column(Integer, nullable=False)
    autorizada = Column(Boolean, nullable=False)
    autfact = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Autfact(autfact={self.autfact})>"