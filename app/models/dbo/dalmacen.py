# Generado automáticamente
# Tabla: dbo.dalmacen
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dalmacen(Base):
    __tablename__ = "dalmacen"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    kardex = Column(Integer, nullable=False)
    almacen = Column(Integer, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    reservado = Column(Numeric(16, 6), nullable=False)
    cuarentena = Column(Numeric(16, 6), nullable=False)
    hcantidad = Column(Numeric(16, 6), nullable=False)
    hreservado = Column(Numeric(16, 6), nullable=False)
    hcuarentena = Column(Numeric(16, 6), nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    dalmacen = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    PRECIO = Column(Numeric(18, 6), nullable=False)
    nula = Column(Boolean, nullable=False)
    dfactura = Column(Integer, nullable=False)
    nombre = Column(String(150))
    dordentrabajo = Column(Integer, nullable=False)
    presenta = Column(Integer, nullable=False)
    facturar = Column(Boolean, nullable=False)
    facturado = Column(Boolean, nullable=False)
    factura = Column(Integer, nullable=False)
    linea = Column(Integer, nullable=False)
    tipoescala = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    lote = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    nolote = Column(String(20))
    fecvence = Column(DateTime)

    # Relaciones
    # almacen_rel = relationship("Almacen", back_populates="dalmacen_set")  # Comentado automáticamente
    # kardex_rel = relationship("Kardex", back_populates="dalmacen_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dalmacen(dalmacen={self.dalmacen})>"