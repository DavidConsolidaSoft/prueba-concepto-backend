# Generado automáticamente
# Tabla: dbo.contratoabono
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Contratoabono(Base):
    __tablename__ = "contratoabono"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    invcliente = Column(Integer, nullable=False)
    factura = Column(Integer, nullable=False)
    montfact = Column(Numeric(18, 6), nullable=False)
    contratoabono = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    pagos = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Contratoabono(contratoabono={self.contratoabono})>"