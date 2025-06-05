# Generado automáticamente
# Tabla: dbo.dperiodo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dperiodo(Base):
    __tablename__ = "dperiodo"
    __table_args__ = {"schema": "dbo"}

    cerrado = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    periodo = Column(Integer, nullable=False)
    dperiodo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fecha = Column(DateTime, nullable=False)
    ano = Column(Integer, nullable=False)
    mes = Column(Integer, nullable=False)

    # Relaciones
    # periodo_rel = relationship("Periodo", back_populates="dperiodo_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dperiodo(dperiodo={self.dperiodo})>"