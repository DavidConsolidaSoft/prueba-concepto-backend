# Generado automáticamente
# Tabla: dbo.asegurad
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String

class Asegurad(Base):
    __tablename__ = "asegurad"
    __table_args__ = {"schema": "dbo", "extend_existing": True}
    
    asegurad = Column(Integer, primary_key=True, autoincrement=True)  # Agregado primary_key=True
    nasegurad = Column(String(80), nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"<Asegurad(asegurad={self.asegurad}, nasegurad={self.nasegurad})>"