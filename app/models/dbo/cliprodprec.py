# Generado automáticamente
# Tabla: dbo.cliprodprec
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Cliprodprec(Base):
    __tablename__ = "cliprodprec"
    __table_args__ = {"schema": "dbo"}

    cliprodprec = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    clientes = Column(String(25), nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    lcobro = Column(String(100))
    vendedor = Column(Integer, nullable=False)
    fechapertura = Column(DateTime)
    LugarCobro = Column(String(100))
    fcobro = Column(DateTime)
    factura = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Cliprodprec(cliprodprec={self.cliprodprec})>"