# Generado automáticamente
# Tabla: dbo.OrdenTrabajo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Ordentrabajo(Base):
    __tablename__ = "OrdenTrabajo"
    __table_args__ = {"schema": "dbo"}

    OrdenTrabajo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tipomov = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    lote = Column(Integer, nullable=False)
    fase = Column(Integer, nullable=False)
    numedocu = Column(String(12), nullable=False)
    fecha = Column(DateTime, nullable=False)
    fecvence = Column(DateTime, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    suspendida = Column(Boolean, nullable=False)
    aReservado = Column(Boolean, nullable=False)
    nolote = Column(String(20), nullable=False)
    notas = Column(String(250), nullable=False)
    adicion = Column(Boolean, nullable=False)
    devolucion = Column(Boolean, nullable=False)
    perdida = Column(Numeric(18, 6), nullable=False)
    cantidad = Column(Numeric(18, 6), nullable=False)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    rupstatus = Column(Integer, nullable=False)
    rupfase = Column(Integer, nullable=False)
    deltaTiempo = Column(Numeric(18, 6), nullable=False)
    Batch = Column(Numeric(18, 6), nullable=False)
    BatchNo = Column(Integer, nullable=False)
    producido = Column(Numeric(18, 6), nullable=False)
    fechaplan = Column(DateTime, nullable=False)
    bodegaInsumos = Column(Integer, nullable=False)
    totalbatch = Column(Integer, nullable=False)
    fechapesada = Column(DateTime, nullable=False)
    ControlSolicitud = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Ordentrabajo(OrdenTrabajo={self.OrdenTrabajo})>"