# Generado automáticamente
# Tabla: dbo.aproducto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Aproducto(Base):
    __tablename__ = "aproducto"
    __table_args__ = {"schema": "dbo"}

    naproducto = Column(String(100), nullable=False)
    valoradquisicion = Column(Numeric(18, 6), nullable=False)
    atipo = Column(Integer, nullable=False)
    sucursal = Column(Integer, nullable=False)
    seccion = Column(Integer, nullable=False)
    serie = Column(String(50), nullable=False)
    codigo = Column(String(25), nullable=False)
    residual = Column(Numeric(18, 6), nullable=False)
    cuota = Column(Numeric(18, 6), nullable=False)
    cuenta = Column(Integer, nullable=False)
    ctrocosto = Column(Integer, nullable=False)
    notas = Column(String(200), nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    aproducto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    fechaadquisicion = Column(DateTime)
    aplicado = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Aproducto(aproducto={self.aproducto})>"