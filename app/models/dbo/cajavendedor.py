# Generado automáticamente
# Tabla: dbo.cajavendedor
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Cajavendedor(Base):
    __tablename__ = "cajavendedor"
    __table_args__ = {"schema": "dbo"}

    cajavendedor = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    caja = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Cajavendedor(cajavendedor={self.cajavendedor})>"