# Generado automáticamente
# Tabla: dbo.RecintoFiscal
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Recintofiscal(Base):
    __tablename__ = "RecintoFiscal"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    nRecintoFiscal = Column(String(35), nullable=False)
    RecintoFiscal = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    direccion = Column(String(200), nullable=False)
    contacto = Column(String(150), nullable=False)
    telefono = Column(String(25), nullable=False)
    cuotam3 = Column(Numeric(18, 6), nullable=False)
    cuotam3seg = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Recintofiscal(RecintoFiscal={self.RecintoFiscal})>"