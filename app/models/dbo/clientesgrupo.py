# Generado automáticamente
# Tabla: dbo.clientesGrupo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Clientesgrupo(Base):
    __tablename__ = "clientesGrupo"
    __table_args__ = {"schema": "dbo"}

    nClientesGrupo = Column(String(50), nullable=False)
    clientes = Column(String(25), nullable=False)
    activo = Column(Boolean, nullable=False)
    pareja = Column(Boolean, nullable=False)
    hijo = Column(Boolean, nullable=False)
    pariente = Column(Boolean, nullable=False)
    Nota = Column(String(250), nullable=False)
    ClientesGrupo = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Clientesgrupo(nClientesGrupo={self.nClientesGrupo})>"