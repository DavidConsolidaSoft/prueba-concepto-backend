# Generado automáticamente
# Tabla: dbo.document
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, LargeBinary
from sqlalchemy import Column, String


class Document(Base):
    __tablename__ = "document"
    __table_args__ = {"schema": "dbo"}

    document = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ndocument = Column(String(50), nullable=False)
    departamento = Column(Integer, nullable=False)
    adjunto = Column(LargeBinary)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Document(document={self.document})>"