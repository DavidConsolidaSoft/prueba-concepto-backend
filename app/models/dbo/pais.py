# Generado automáticamente
# Tabla: dbo.pais
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Pais(Base):
    __tablename__ = "pais"
    __table_args__ = {"schema": "dbo"}

    npais = Column(String(30), nullable=False)
    activo = Column(Boolean, nullable=False)
    preferido = Column(Boolean, nullable=False)
    pais = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    NACIONAL = Column(Integer, nullable=False)
    elsalvador = Column(Boolean, nullable=False)
    Guatemala = Column(Boolean, nullable=False)
    Honduras = Column(Boolean, nullable=False)
    Costarica = Column(Boolean, nullable=False)
    Panama = Column(Boolean, nullable=False)
    Nicaragua = Column(Boolean, nullable=False)
    EstadosUnidos = Column(Boolean, nullable=False)
    Mexico = Column(Boolean, nullable=False)
    Chile = Column(Boolean, nullable=False)
    Ecuador = Column(Boolean, nullable=False)
    Peru = Column(Boolean, nullable=False)
    bolivia = Column(Boolean, nullable=False)
    Venezuela = Column(Boolean, nullable=False)
    moneda = Column(Integer, nullable=False)
    ImpresorFiscal = Column(Boolean, nullable=False)
    datosfactura = Column(Boolean, nullable=False)
    tipoCompra = Column(Integer, nullable=False)
    dominicana = Column(Boolean, nullable=False)
    libroconsumidor = Column(Boolean, nullable=False)
    limitepago = Column(Numeric(18, 6), nullable=False)
    belice = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Pais(pais={self.pais})>"