# Generado automáticamente
# Tabla: dbo.drecvineta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Drecvineta(Base):
    __tablename__ = "drecvineta"
    __table_args__ = {"schema": "dbo"}

    clientes = Column(String(50), nullable=False)
    dfactura = Column(Integer, nullable=False)
    recvineta = Column(Integer, nullable=False)
    vvineta = Column(Numeric(18, 6), nullable=False)
    precioa = Column(Numeric(18, 6), nullable=False)
    preciob = Column(Numeric(18, 6), nullable=False)
    drecvineta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    pagada = Column(Boolean, nullable=False)
    factura = Column(Integer, nullable=False)
    vinetanum = Column(Integer, nullable=False)
    icdbarra = Column(String(25), nullable=False)
    notas = Column(String(300), nullable=False)

    def __repr__(self):
        return "<Drecvineta(drecvineta={self.drecvineta})>"