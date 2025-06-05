# Generado automáticamente
# Tabla: dbo.clidprodprec
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Clidprodprec(Base):
    __tablename__ = "clidprodprec"
    __table_args__ = {"schema": "dbo"}

    clidprodprec = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    cliprodprec = Column(Integer, nullable=False)
    prodprec = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    condpago = Column(Integer)
    usuario = Column(Integer, nullable=False)
    monto = Column(Numeric(18, 9))

    def __repr__(self):
        return "<Clidprodprec(clidprodprec={self.clidprodprec})>"