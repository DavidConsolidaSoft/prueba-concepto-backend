# Generado automáticamente
# Tabla: dbo.transpte
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Transpte(Base):
    __tablename__ = "transpte"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    ntranspte = Column(String(50), nullable=False)
    motorista = Column(String(50), nullable=False)
    placas = Column(String(10), nullable=False)
    descripcion = Column(String(30), nullable=False)
    valorfleteton = Column(Numeric(16, 6), nullable=False)
    valorfleteviaje = Column(Numeric(16, 6), nullable=False)
    transpte = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    controlcorrel = Column(Integer, nullable=False)
    clientes = Column(String(25), nullable=False)
    propio = Column(Boolean, nullable=False)
    toneladas = Column(Numeric(18, 6), nullable=False)
    m3 = Column(Numeric(18, 6), nullable=False)
    correl = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Transpte(transpte={self.transpte})>"