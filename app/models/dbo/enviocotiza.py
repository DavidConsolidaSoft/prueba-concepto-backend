# Generado automáticamente
# Tabla: dbo.envioCotiza
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Enviocotiza(Base):
    __tablename__ = "envioCotiza"
    __table_args__ = {"schema": "dbo"}

    Activo = Column(Boolean, nullable=False)
    dcambodega = Column(Integer, nullable=False)
    dfactura = Column(Integer, nullable=False)
    doventa = Column(Integer, nullable=False)
    envioCotiza = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Enviocotiza(envioCotiza={self.envioCotiza})>"