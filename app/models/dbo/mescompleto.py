# Generado automáticamente
# Tabla: dbo.mesCompleto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Mescompleto(Base):
    __tablename__ = "mesCompleto"
    __table_args__ = {"schema": "dbo"}

    meses = Column(Integer, nullable=False)
    ano = Column(Integer, nullable=False)
    D1 = Column(String(1), nullable=False)
    D2 = Column(String(1), nullable=False)
    D3 = Column(String(1), nullable=False)
    D4 = Column(String(1), nullable=False)
    D5 = Column(String(1), nullable=False)
    D6 = Column(String(1), nullable=False)
    D7 = Column(String(1), nullable=False)
    D8 = Column(String(1), nullable=False)
    D9 = Column(String(1), nullable=False)
    D10 = Column(String(1), nullable=False)
    D11 = Column(String(1), nullable=False)
    D12 = Column(String(1), nullable=False)
    D13 = Column(String(1), nullable=False)
    D14 = Column(String(1), nullable=False)
    D15 = Column(String(1), nullable=False)
    D16 = Column(String(1), nullable=False)
    D17 = Column(String(1), nullable=False)
    D18 = Column(String(1), nullable=False)
    D19 = Column(String(1), nullable=False)
    D20 = Column(String(1), nullable=False)
    D21 = Column(String(1), nullable=False)
    D22 = Column(String(1), nullable=False)
    D23 = Column(String(1), nullable=False)
    D24 = Column(String(1), nullable=False)
    D25 = Column(String(1), nullable=False)
    D26 = Column(String(1), nullable=False)
    D27 = Column(String(1), nullable=False)
    D28 = Column(String(1), nullable=False)
    D29 = Column(String(1), nullable=False)
    D30 = Column(String(1), nullable=False)
    D31 = Column(String(1), nullable=False)
    mescompleto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Mescompleto(mescompleto={self.mescompleto})>"