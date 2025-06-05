# Generado automáticamente
# Tabla: dbo.aAutorizar
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Boolean, Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String


class Aautorizar(Base):
    __tablename__ = "aAutorizar"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    accesos = Column(Integer, nullable=False)
    documentoid = Column(Integer, nullable=False)
    esperfil = Column(Boolean, nullable=False)
    pedidoVenta = Column(Boolean, nullable=False)
    pedidoCompra = Column(Boolean, nullable=False)
    factura = Column(Boolean, nullable=False)
    compra = Column(Boolean, nullable=False)
    almacen = Column(Boolean, nullable=False)
    otros = Column(Boolean, nullable=False)
    tipomov = Column(Integer, nullable=False)
    datos = Column(String(250), nullable=False)
    autorizado = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    autoriza = Column(Integer, nullable=False)
    fechaautorizado = Column(DateTime)
    aAutorizar = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    original = Column(Integer, nullable=False)
    nueva = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Aautorizar(aAutorizar={self.aAutorizar})>"