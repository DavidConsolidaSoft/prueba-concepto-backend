# Generado automáticamente
# Tabla: dbo.dcambodega
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class DCamboBodega(Base):
    __tablename__ = "dcambodega"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    reservado = Column(Numeric(16, 6), nullable=False)
    cuarentena = Column(Numeric(16, 6), nullable=False)
    hcantidad = Column(Numeric(16, 6), nullable=False)
    hreservado = Column(Numeric(16, 6), nullable=False)
    hcuarentena = Column(Numeric(16, 6), nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    kardex = Column(Integer, nullable=False)
    kardex1 = Column(Integer, nullable=False)
    cambodega = Column(Integer, nullable=False)
    dcambodega = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    precio = Column(Numeric(16, 6), nullable=False)
    nula = Column(Boolean, nullable=False)
    nombre = Column(String(1000), nullable=False)
    exenta = Column(Numeric(18, 6), nullable=False)
    afecta = Column(Numeric(18, 6), nullable=False)
    viva = Column(Numeric(18, 6), nullable=False)
    montfact = Column(Numeric(18, 6), nullable=False)
    retencion = Column(Numeric(18, 6), nullable=False)
    percepcion = Column(Numeric(18, 6), nullable=False)
    nosujeto = Column(Numeric(18, 6), nullable=False)
    original = Column(Numeric(18, 6), nullable=False)
    devolucion1 = Column(Numeric(18, 6), nullable=False)
    devolucion2 = Column(Numeric(18, 6), nullable=False)
    devolucion3 = Column(Numeric(18, 6), nullable=False)
    devolucion4 = Column(Numeric(18, 6), nullable=False)
    devolucion5 = Column(Numeric(18, 6), nullable=False)
    fProducto = Column(Integer, nullable=False)
    afacturar = Column(Boolean, nullable=False)
    facturado = Column(Boolean, nullable=False)
    fkardex = Column(Integer, nullable=False)
    fcantidad = Column(Numeric(18, 6), nullable=False)
    precio1 = Column(Numeric(18, 6), nullable=False)
    precio2 = Column(Numeric(18, 6), nullable=False)
    facturar = Column(Boolean, nullable=False)
    factura = Column(Integer, nullable=False)
    fisico = Column(Integer, nullable=False)
    fechaliq = Column(DateTime)
    venta = Column(Integer, nullable=False)
    efectivo = Column(Numeric(18, 6), nullable=False)
    linea = Column(Integer, nullable=False)
    tipoescala = Column(Integer, nullable=False)
    mformula = Column(Integer)
    gratif = Column(Numeric(9, 2), nullable=False)
    devolucion6 = Column(Numeric(18, 6), nullable=False)
    devolucion7 = Column(Numeric(18, 6), nullable=False)
    devolucion8 = Column(Numeric(18, 6), nullable=False)
    devolucion9 = Column(Numeric(18, 6), nullable=False)
    devolucion10 = Column(Numeric(18, 6), nullable=False)
    devolucion11 = Column(Numeric(18, 6), nullable=False)
    devolucion12 = Column(Numeric(18, 6), nullable=False)
    devolucion13 = Column(Numeric(18, 6), nullable=False)
    devolucion14 = Column(Numeric(18, 6), nullable=False)
    devolucion15 = Column(Numeric(18, 6), nullable=False)

    # Relaciones
    # cambodega_rel = relationship("Cambodega", back_populates="dcambodega_set")  # Comentado automáticamente
    # kardex_rel = relationship("Kardex", back_populates="dcambodega_set")  # Comentado automáticamente
    # kardex_rel = relationship("Kardex", back_populates="dcambodega_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dcambodega(dcambodega={self.dcambodega})>"