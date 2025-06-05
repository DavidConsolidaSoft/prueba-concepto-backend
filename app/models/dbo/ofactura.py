# Generado automáticamente
# Tabla: dbo.ofactura
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, BigInteger
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Ofactura(Base):
    __tablename__ = "ofactura"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    cancelada = Column(Boolean, nullable=False)
    impbod = Column(Boolean, nullable=False)
    impresa = Column(Boolean, nullable=False)
    numedocu = Column(String(9))
    pedido = Column(String(10), nullable=False)
    comentario = Column(String(80), nullable=False)
    expcomen = Column(String(80), nullable=False)
    notas = Column(String(200), nullable=False)
    fecha = Column(DateTime, nullable=False)
    fechacanc = Column(DateTime)
    clientes = Column(String(25), nullable=False)
    bodega = Column(Integer, nullable=False)
    prodprec = Column(Integer, nullable=False)
    iva = Column(Integer, nullable=False)
    transpte = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    tipovta = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    tipomov = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    factoriva = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    montfact = Column(Numeric(16, 6), nullable=False)
    pdesc = Column(Numeric(16, 6), nullable=False)
    vdesc = Column(Numeric(16, 6), nullable=False)
    ofactura = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fovial = Column(Numeric(16, 6), nullable=False)
    pesoofactura = Column(Numeric(16, 6), nullable=False)
    pagos = Column(Integer, nullable=False)
    basesiniva = Column(Boolean, nullable=False)
    retencion = Column(Numeric(16, 6), nullable=False)
    efectivo = Column(Numeric(16, 6), nullable=False)
    cheque = Column(Numeric(16, 6), nullable=False)
    tarjeta = Column(Numeric(16, 6), nullable=False)
    nocheque = Column(String(25), nullable=False)
    notarjeta = Column(String(25), nullable=False)
    caja = Column(Integer, nullable=False)
    combustible = Column(Numeric(18, 6), nullable=False)
    encomienda = Column(Numeric(18, 6), nullable=False)
    ivaCombustible = Column(Numeric(18, 6), nullable=False)
    ivaencomienda = Column(Numeric(18, 6), nullable=False)
    Cotrans = Column(Numeric(16, 8), nullable=False)
    fechafin = Column(DateTime)
    estado = Column(Integer, nullable=False)
    prioridad = Column(Integer, nullable=False)
    terminado = Column(Boolean, nullable=False)
    turno = Column(Integer, nullable=False)
    rliquida = Column(Integer, nullable=False)
    aprobado = Column(Boolean, nullable=False)
    impempaque = Column(Boolean, nullable=False)
    impvineta = Column(Boolean, nullable=False)
    vineta = Column(Integer, nullable=False)
    enfirme = Column(Boolean, nullable=False)
    dgratif = Column(Numeric(18, 6), nullable=False)
    tipopago = Column(Integer, nullable=False)
    bnotas = Column(String(250), nullable=False)
    cobrador = Column(Integer, nullable=False)
    docunico = Column(String(9), nullable=False)
    percepcion = Column(Numeric(18, 6), nullable=False)
    nosujeto = Column(Numeric(18, 6), nullable=False)
    concaja = Column(Boolean, nullable=False)
    clientes2 = Column(String(25), nullable=False)
    pais = Column(Integer, nullable=False)
    pagencia = Column(Numeric(5, 2), nullable=False)
    fecha1 = Column(DateTime)
    fecha2 = Column(DateTime)
    ordenno = Column(String(15), nullable=False)
    nombreref = Column(String(35), nullable=False)
    docref = Column(String(25), nullable=False)
    camion = Column(Integer, nullable=False)
    ofacturaReferencia = Column(BigInteger, nullable=False)
    enruta = Column(Boolean, nullable=False)
    anulada = Column(Boolean, nullable=False)
    propina = Column(Numeric(18, 6), nullable=False)
    nopropina = Column(Boolean, nullable=False)
    mesa = Column(Boolean, nullable=False)
    nomesa = Column(String(25), nullable=False)
    nclientes = Column(String(60))
    Descautorizado = Column(Numeric(18, 2), nullable=False)
    fechaEntrega = Column(DateTime, nullable=False)
    entregas = Column(Integer, nullable=False)
    showroom = Column(Boolean, nullable=False)

    # Relaciones
    # clientes_rel = relationship("Clientes", back_populates="ofactura_set")  # Comentado automáticamente
    # iva_rel = relationship("Iva", back_populates="ofactura_set")  # Comentado automáticamente
    # tipomov_rel = relationship("Tipomov", back_populates="ofactura_set")  # Comentado automáticamente
    # vendedor_rel = relationship("Vendedor", back_populates="ofactura_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Ofactura(ofactura={self.ofactura})>"