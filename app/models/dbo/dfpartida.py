# Generado automáticamente
# Tabla: dbo.dfpartida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dfpartida(Base):
    __tablename__ = "dfpartida"
    __table_args__ = {"schema": "dbo"}

    concepto = Column(String(50), nullable=False)
    tcondicion1 = Column(String(250), nullable=False)
    tcondicion2 = Column(String(250), nullable=False)
    tcondicion3 = Column(String(250), nullable=False)
    tcondicion4 = Column(String(250), nullable=False)
    tcondicion5 = Column(String(250), nullable=False)
    cuenta = Column(Integer, nullable=False)
    ctrocosto = Column(Integer, nullable=False)
    debe = Column(Boolean, nullable=False)
    fpartida = Column(Integer, nullable=False)
    dfpartida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    # Relaciones
    # fpartida_rel = relationship("Fpartida", back_populates="dfpartida_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dfpartida(dfpartida={self.dfpartida})>"