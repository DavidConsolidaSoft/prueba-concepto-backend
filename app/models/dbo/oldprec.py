# Generado automáticamente
# Tabla: dbo.oldprec
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Oldprec(Base):
    __tablename__ = "oldprec"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime, nullable=False)
    preciopublico = Column(Numeric(16, 6), nullable=False)
    nvoprecio = Column(Numeric(16, 6), nullable=False)
    activo = Column(Boolean, nullable=False)
    producto = Column(Integer, nullable=False)
    prodprec = Column(Integer, nullable=False)
    oldprec = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Oldprec(oldprec={self.oldprec})>"