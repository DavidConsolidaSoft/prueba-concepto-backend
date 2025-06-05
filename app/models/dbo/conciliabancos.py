# Generado automáticamente
# Tabla: dbo.ConciliaBancos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Conciliabancos(Base):
    __tablename__ = "ConciliaBancos"
    __table_args__ = {"schema": "dbo"}

    ConciliaBancos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tipopart = Column(Integer, nullable=False)
    partida = Column(Integer, nullable=False)
    cuentaBanco = Column(Integer, nullable=False)
    FechaBanco = Column(DateTime, nullable=False)
    noEstadoCuenta = Column(String(15), nullable=False)
    Debe = Column(Numeric(18, 6), nullable=False)
    haber = Column(Numeric(18, 6), nullable=False)
    conciliado = Column(Boolean, nullable=False)
    notas = Column(String(250), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Conciliabancos(ConciliaBancos={self.ConciliaBancos})>"