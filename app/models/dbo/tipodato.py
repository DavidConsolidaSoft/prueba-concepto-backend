# Generado automáticamente
# Tabla: dbo.tipodato
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipodato(Base):
    __tablename__ = "tipodato"
    __table_args__ = {"schema": "dbo"}

    equipo = Column(String(100), nullable=False)
    dia = Column(Integer, nullable=False)
    mes = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    tipodato = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    anio = Column(Integer, nullable=False)
    miIp = Column(String(50))
    milp = Column(String(50))

    def __repr__(self):
        return "<Tipodato(tipodato={self.tipodato})>"