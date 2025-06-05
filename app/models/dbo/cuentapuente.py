# Generado automáticamente
# Tabla: dbo.cuentapuente
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Cuentapuente(Base):
    __tablename__ = "cuentapuente"
    __table_args__ = {"schema": "dbo"}

    cuenta = Column(Integer, nullable=False)
    cuentapuente = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Cuentapuente(cuentapuente={self.cuentapuente})>"