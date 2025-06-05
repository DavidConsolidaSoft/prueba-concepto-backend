# Generado automáticamente
# Tabla: dbo.tipoprest
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Tipoprest(Base):
    __tablename__ = "tipoprest"
    __table_args__ = {"schema": "dbo"}

    ntipoprest = Column(String(80), nullable=False)
    bancos = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    procuraduria = Column(Boolean, nullable=False)
    prestamo = Column(Boolean, nullable=False)
    tipoprest = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fsv = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    factor = Column(Numeric(8, 2))

    def __repr__(self):
        return "<Tipoprest(ntipoprest={self.ntipoprest})>"