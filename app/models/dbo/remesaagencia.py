# Generado automáticamente
# Tabla: dbo.RemesaAgencia
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Remesaagencia(Base):
    __tablename__ = "RemesaAgencia"
    __table_args__ = {"schema": "dbo"}

    Clientes = Column(String(25), nullable=False)
    Banco = Column(Integer, nullable=False)
    Remesa = Column(String(25), nullable=False)
    fecha = Column(DateTime)
    Monto = Column(Numeric(16, 6), nullable=False)
    Activo = Column(Boolean, nullable=False)
    RemesaAgencia = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Remesaagencia(RemesaAgencia={self.RemesaAgencia})>"