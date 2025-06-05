# Generado automáticamente
# Tabla: dbo.fpartida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Fpartida(Base):
    __tablename__ = "fpartida"
    __table_args__ = {"schema": "dbo"}

    nfpartida = Column(String(40), nullable=False)
    tipopart = Column(Integer, nullable=False)
    concepto = Column(String(100), nullable=False)
    fpartida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Fpartida(fpartida={self.fpartida})>"