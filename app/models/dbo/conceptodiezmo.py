# Generado automáticamente
# Tabla: dbo.ConceptoDiezmo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Conceptodiezmo(Base):
    __tablename__ = "ConceptoDiezmo"
    __table_args__ = {"schema": "dbo"}

    ConceptoDiezmo = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    nConceptoDiezmo = Column(String(35), nullable=False)
    diezmo = Column(Boolean, nullable=False)
    ofrenda = Column(Boolean, nullable=False)
    primicia = Column(Boolean, nullable=False)
    evento = Column(Boolean, nullable=False)
    festividad = Column(Boolean, nullable=False)
    siembra = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Conceptodiezmo(ConceptoDiezmo={self.ConceptoDiezmo})>"