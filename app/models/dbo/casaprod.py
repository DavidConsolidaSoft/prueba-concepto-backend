# Generado automáticamente
# Tabla: dbo.casaprod
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Casaprod(Base):
    __tablename__ = "casaprod"
    __table_args__ = {"schema": "dbo"}

    ncasaprod = Column(String(35), nullable=False)
    preferido = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    casaprod = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    contacto = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False)
    porc1 = Column(Numeric(18, 6), nullable=False)
    porc2 = Column(Numeric(18, 6), nullable=False)
    porc3 = Column(Numeric(18, 6), nullable=False)
    porc4 = Column(Numeric(18, 6), nullable=False)
    porc5 = Column(Numeric(18, 6), nullable=False)
    lim1 = Column(Numeric(18, 6), nullable=False)
    lim2 = Column(Numeric(18, 6), nullable=False)
    lim3 = Column(Numeric(18, 6), nullable=False)
    lim4 = Column(Numeric(18, 6), nullable=False)
    lim5 = Column(Numeric(18, 6), nullable=False)
    comisionfija = Column(Boolean, nullable=False)
    porclogro = Column(Numeric(18, 6), nullable=False)
    porcNoLogro = Column(Numeric(18, 6), nullable=False)
    umedida = Column(Integer, nullable=False)
    factor1 = Column(Integer, nullable=False)
    factor2 = Column(Integer, nullable=False)
    factor3 = Column(Integer, nullable=False)
    factor4 = Column(Integer, nullable=False)
    factor5 = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Casaprod(casaprod={self.casaprod})>"