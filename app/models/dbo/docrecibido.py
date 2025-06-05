# Generado automáticamente
# Tabla: dbo.docRecibido
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Docrecibido(Base):
    __tablename__ = "docRecibido"
    __table_args__ = {"schema": "dbo"}

    docRecibido = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    DocumentoViaje = Column(Integer, nullable=False)
    dpfactura = Column(Integer, nullable=False)
    Recibido = Column(Boolean, nullable=False)
    Notas = Column(String(250), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Docrecibido(docRecibido={self.docRecibido})>"