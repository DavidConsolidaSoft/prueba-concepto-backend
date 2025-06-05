# Generado automáticamente
# Tabla: dbo.pagom3
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Pagom3(Base):
    __tablename__ = "pagom3"
    __table_args__ = {"schema": "dbo"}

    pagom3 = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ocompra = Column(Integer)
    fecha = Column(DateTime)
    montom3 = Column(Numeric(18, 6))
    monto = Column(Numeric(18, 6))
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Pagom3(pagom3={self.pagom3})>"