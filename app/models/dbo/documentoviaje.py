# Generado automáticamente
# Tabla: dbo.Documentoviaje
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Documentoviaje(Base):
    __tablename__ = "Documentoviaje"
    __table_args__ = {"schema": "dbo"}

    DocumentoViaje = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nDocumentoViaje = Column(String(25), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Documentoviaje(DocumentoViaje={self.DocumentoViaje})>"