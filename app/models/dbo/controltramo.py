# Generado automáticamente
# Tabla: dbo.controlTramo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Controltramo(Base):
    __tablename__ = "controlTramo"
    __table_args__ = {"schema": "dbo"}

    dpfactura = Column(Integer, nullable=False)
    tramo = Column(Integer, nullable=False)
    nTramo = Column(String(50), nullable=False)
    fecha = Column(DateTime)
    controlTramo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    precio = Column(Numeric(18, 6), nullable=False)
    facturar = Column(Boolean, nullable=False)
    facturado = Column(Boolean, nullable=False)
    TIRExport = Column(String(25), nullable=False)
    TIRImport = Column(String(25), nullable=False)
    OrdenPago = Column(String(25))
    producto = Column(Integer, nullable=False)
    bl = Column(String(25), nullable=False)
    precioAgregado = Column(Numeric(18, 6), nullable=False)
    fechaQuedan = Column(DateTime)
    precioParte = Column(Numeric(18, 6), nullable=False)
    factura = Column(Integer, nullable=False)
    PRECIOPROV = Column(Numeric(18, 6), nullable=False)
    FECHAPROV = Column(DateTime)
    OTROSCPROV = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Controltramo(controlTramo={self.controlTramo})>"