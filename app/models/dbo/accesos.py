# Generado automáticamente
# Tabla: dbo.accesos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Boolean, Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Numeric


class Accesos(Base):
    __tablename__ = "accesos"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    proceso = Column(Integer, nullable=False)
    acceso = Column(Boolean, nullable=False)
    crear = Column(Boolean, nullable=False)
    modificar = Column(Boolean, nullable=False)
    eliminar = Column(Boolean, nullable=False)
    imprimir = Column(Boolean, nullable=False)
    excel = Column(Boolean, nullable=False)
    accesos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    rusuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    monto = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Accesos(accesos={self.accesos})>"