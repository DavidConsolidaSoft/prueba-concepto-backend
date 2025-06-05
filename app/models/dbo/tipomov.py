# Generado automáticamente
# Tabla: dbo.tipomov
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String
# # from sqlalchemy.orm import relationship  # Comentado temporalmente  # Comentado temporalmente


class TipoMov(Base):
    __tablename__ = "tipomov"
    __table_args__ = {"schema": "dbo"}

    tipomov = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ntipomov = Column(String(35), nullable=False)
    activo = Column(Boolean, nullable=False)
    preferido = Column(Boolean, nullable=False)
    factura = Column(Boolean, nullable=False)
    coniva = Column(Boolean, nullable=False)
    iva = Column(Boolean, nullable=False)
    cancelacion = Column(Boolean, nullable=False)
    anulacion = Column(Boolean, nullable=False)
    notacargo = Column(Boolean, nullable=False)
    notadebito = Column(Boolean, nullable=False)
    notacred = Column(Boolean, nullable=False)
    produccion = Column(Boolean, nullable=False)
    cambodega = Column(Boolean, nullable=False)
    devolucion = Column(Boolean, nullable=False)
    efectivo = Column(Boolean, nullable=False)
    cheque = Column(Boolean, nullable=False)
    ajuste = Column(Boolean, nullable=False)
    impuesto = Column(Boolean, nullable=False)
    costo = Column(Boolean, nullable=False)
    bonificacion = Column(Boolean, nullable=False)
    bonifextra = Column(Boolean, nullable=False)
    inventario = Column(Boolean, nullable=False)
    pedido = Column(Boolean, nullable=False)
    invinicial = Column(Boolean, nullable=False)
    nlineasmax = Column(Integer, nullable=False)
    cargo = Column(String(1), nullable=False)
    correl = Column(Integer, nullable=False)
    modulo = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    compra = Column(Boolean, nullable=False)
    contrato = Column(Boolean, nullable=False)
    ocompra = Column(Boolean, nullable=False)
    informe = Column(String(25), nullable=False)
    tiquet = Column(Boolean, nullable=False)
    retencion = Column(Boolean, nullable=False)
    bodega = Column(Integer, nullable=False)
    ptovta = Column(Integer, nullable=False)
    Movauto = Column(Boolean, nullable=False)
    cd = Column(Boolean, nullable=False)
    cp = Column(Boolean, nullable=False)
    impresor = Column(String(35))
    noaplicariva = Column(Boolean, nullable=False)
    docunico = Column(Integer, nullable=False)
    controlcorrel = Column(Integer, nullable=False)
    correlpropio = Column(Boolean, nullable=False)
    qmin = Column(Integer, nullable=False)
    qmax = Column(Integer, nullable=False)
    chequerechazado = Column(Boolean, nullable=False)
    antifactura = Column(Boolean, nullable=False)
    warningcorrel = Column(Integer, nullable=False)
    fwarning = Column(DateTime)
    ANTICIPO = Column(Boolean, nullable=False)
    controlcarga = Column(Boolean, nullable=False)
    remision = Column(Boolean, nullable=False)
    ruta = Column(Boolean, nullable=False)
    nccompra = Column(Boolean, nullable=False)
    exportacion = Column(Boolean, nullable=False)
    empaque = Column(Boolean, nullable=False)
    Taller = Column(Boolean, nullable=False)
    notaenvio = Column(Boolean, nullable=False)
    diasparaAnular = Column(Integer, nullable=False)
    oventa = Column(Boolean, nullable=False)
    ncaja = Column(String(35), nullable=False)
    caja = Column(Integer, nullable=False)
    ofactura = Column(Boolean)
    IngxDevolucion = Column(Boolean, nullable=False)
    tipoventa = Column(Integer, nullable=False)
    cortesia = Column(Boolean, nullable=False)
    norestariva = Column(Boolean, nullable=False)
    cuenta1 = Column(Integer)
    cuenta = Column(Integer)
    cuenta2 = Column(Integer)
    prodprec = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    compuesto = Column(Boolean, nullable=False)
    
    # Relaciones
    # # almacenes = relationship(...)  # Comentado automáticamente  # Comentado temporalmente
    # # facturas = relationship(...)  # Comentado automáticamente  # Comentado temporalmente

    def __repr__(self):
        return f"<TipoMov(tipomov={self.tipomov}, ntipomov={self.ntipomov})>"