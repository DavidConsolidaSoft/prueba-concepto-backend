# Generado automáticamente
# Tabla: dbo.tipopart
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipopart(Base):
    __tablename__ = "tipopart"
    __table_args__ = {"schema": "dbo"}

    ntipopart = Column(String(35), nullable=False)
    activo = Column(Boolean, nullable=False)
    diario = Column(Boolean, nullable=False)
    banco = Column(Boolean, nullable=False)
    remesa = Column(Boolean, nullable=False)
    tipopart = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    provision = Column(Boolean, nullable=False)
    ingreso = Column(Boolean, nullable=False)
    QUEDAM = Column(Boolean, nullable=False)
    CORRELATIVO = Column(Integer, nullable=False)
    NotaCred = Column(Boolean, nullable=False)
    NotaDebito = Column(Boolean, nullable=False)
    notaremision = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Tipopart(tipopart={self.tipopart})>"