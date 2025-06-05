# Generado automáticamente
# Tabla: dbo.ftablapart
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Ftablapart(Base):
    __tablename__ = "ftablapart"
    __table_args__ = {"schema": "dbo"}

    dfpartida = Column(Integer, nullable=False)
    tabla = Column(String(150), nullable=False)
    ncampo = Column(String(150), nullable=False)
    campo = Column(Integer, nullable=False)
    cuenta = Column(Integer, nullable=False)
    ctrocosto = Column(Integer, nullable=False)
    ftablapart = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Ftablapart(ftablapart={self.ftablapart})>"