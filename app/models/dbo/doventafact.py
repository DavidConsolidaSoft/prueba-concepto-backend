# Generado automáticamente
# Tabla: dbo.doventafact
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Doventafact(Base):
    __tablename__ = "doventafact"
    __table_args__ = {"schema": "dbo"}

    dfactura = Column(Integer)
    doventa = Column(Integer)
    cantidad = Column(Numeric(18, 2))
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    doventafact = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dcambodega = Column(Integer)

    def __repr__(self):
        return "<Doventafact(doventafact={self.doventafact})>"