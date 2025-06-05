# Generado automáticamente
# Tabla: dbo.factorxcli
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Factorxcli(Base):
    __tablename__ = "factorxcli"
    __table_args__ = {"schema": "dbo"}

    clientes = Column(String(25), nullable=False)
    presenta = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    factor = Column(Numeric(16, 6), nullable=False)
    factorxcli = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    # Relaciones
    # clientes_rel = relationship("Clientes", back_populates="factorxcli_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Factorxcli(factorxcli={self.factorxcli})>"