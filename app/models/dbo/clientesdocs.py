# Generado automáticamente
# Tabla: dbo.ClientesDocs
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Clientesdocs(Base):
    __tablename__ = "ClientesDocs"
    __table_args__ = {"schema": "dbo"}

    ClientesDocs = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    nClientesDocs = Column(String(150))
    ClientesDocsRef = Column(String(250))
    clientes = Column(String(25))
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Clientesdocs(ClientesDocs={self.ClientesDocs})>"