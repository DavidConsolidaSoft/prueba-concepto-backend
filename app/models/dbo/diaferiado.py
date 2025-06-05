# Generado automáticamente
# Tabla: dbo.diaferiado
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Diaferiado(Base):
    __tablename__ = "diaferiado"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime, nullable=False)
    ndiaferiado = Column(String(150), nullable=False)
    diaferiado = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    nhoraspago = Column(Numeric(18, 6))

    def __repr__(self):
        return "<Diaferiado(diaferiado={self.diaferiado})>"