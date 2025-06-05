# Generado automáticamente
# Tabla: dbo.Clientes_caja
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class ClientesCaja(Base):
    __tablename__ = "Clientes_caja"
    __table_args__ = {"schema": "dbo"}

    caja = Column(Integer, nullable=False)
    clientes = Column(String(60), nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    clientes_caja = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<ClientesCaja(clientes_caja={self.clientes_caja})>"