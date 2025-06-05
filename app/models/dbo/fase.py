# Generado automáticamente
# Tabla: dbo.fase
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Fase(Base):
    __tablename__ = "fase"
    __table_args__ = {"schema": "dbo"}

    fase = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nfase = Column(String(50), nullable=False)
    iteracion = Column(Integer, nullable=False)
    duracion = Column(Numeric(18, 2), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Fase(fase={self.fase})>"