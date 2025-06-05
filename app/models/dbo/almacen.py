# Generado automáticamente
# Tabla: dbo.almacen
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
# # from sqlalchemy.orm import relationship  # Comentado temporalmente  # Comentado temporalmente

class Almacen(Base):
    __tablename__ = "almacen"
    __table_args__ = {"schema": "dbo"}
    
    almacen = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    tipomov = Column(Integer, ForeignKey("dbo.tipomov.tipomov"), nullable=False)  # Agregar ForeignKey
    numedocu = Column(String(9), nullable=False)
    fecha = Column(DateTime, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    notas = Column(String(150), nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    clientes = Column(String(25), nullable=False)
    dfactura = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    camion = Column(Integer, nullable=False)
    pfactura = Column(Integer, nullable=False)
    transpte = Column(Integer, nullable=False)
    OrdenTrabajo = Column(Integer, nullable=False)
    rupfase = Column(Integer, nullable=False)
    gestiontaller = Column(Integer, nullable=False)
    prodprec = Column(Integer, nullable=False)
    motorista = Column(Integer, nullable=False)
    factura = Column(Integer, nullable=False)
    compra = Column(Integer, nullable=False)
    PrecioActualizado = Column(Boolean, nullable=False)
    tienecambiobodega = Column(Boolean, nullable=False)
    almacenReferencia = Column(Integer, nullable=False)
    caja = Column(Integer, nullable=False)
    IngxDevolucion = Column(Boolean, nullable=False)
    NcAplicada = Column(Integer, nullable=False)
    equipoprocess = Column(Integer)
    fentrega = Column(DateTime)
    fechacierre = Column(DateTime)
    
    # Relaciones - cambiar el nombre para evitar conflicto
    # # tipomov_rel = relationship(...)  # Comentado automáticamente  # Comentado temporalmente  # Cambiar nombre
    
    def __repr__(self):
        return f"<Almacen(almacen={self.almacen})>"