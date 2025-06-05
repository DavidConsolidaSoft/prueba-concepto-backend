# Generado automáticamente
# Tabla: dbo.periodoiva
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Periodoiva(Base):
    __tablename__ = "periodoiva"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    fecha = Column(DateTime, nullable=False)
    exportacion = Column(Numeric(16, 6), nullable=False)
    remanente = Column(Numeric(16, 6), nullable=False)
    rempagocta = Column(Numeric(16, 6), nullable=False)
    ventas = Column(Numeric(16, 6), nullable=False)
    compras = Column(Numeric(16, 6), nullable=False)
    debitos = Column(Numeric(16, 6), nullable=False)
    creditos = Column(Numeric(16, 6), nullable=False)
    sujetos = Column(Numeric(16, 6), nullable=False)
    retenciones = Column(Numeric(16, 6), nullable=False)
    pagoacuenta = Column(Numeric(16, 6), nullable=False)
    excluido = Column(Numeric(16, 6), nullable=False)
    periodoiva = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)

    def __repr__(self):
        return "<Periodoiva(periodoiva={self.periodoiva})>"