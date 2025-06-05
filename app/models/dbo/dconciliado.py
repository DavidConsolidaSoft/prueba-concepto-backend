# Generado automáticamente
# Tabla: dbo.dconciliado
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dconciliado(Base):
    __tablename__ = "dconciliado"
    __table_args__ = {"schema": "dbo"}

    dconciliado = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    conciliado = Column(Numeric(9, 2))
    partida = Column(Integer)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Dconciliado(dconciliado={self.dconciliado})>"