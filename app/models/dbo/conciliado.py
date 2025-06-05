# Generado automáticamente
# Tabla: dbo.conciliado
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Conciliado(Base):
    __tablename__ = "conciliado"
    __table_args__ = {"schema": "dbo"}

    conciliado = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    saldo = Column(Numeric(9, 2))
    Fecha = Column(DateTime)
    diferencia = Column(Numeric(9, 2))
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Conciliado(conciliado={self.conciliado})>"