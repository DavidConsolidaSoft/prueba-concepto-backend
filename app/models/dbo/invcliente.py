# Generado automáticamente
# Tabla: dbo.invcliente
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Invcliente(Base):
    __tablename__ = "invcliente"
    __table_args__ = {"schema": "dbo"}

    clientes = Column(String(25), nullable=False)
    tipomov = Column(Integer, nullable=False)
    factura = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    numedocu = Column(String(15), nullable=False)
    fecha = Column(DateTime, nullable=False)
    fechacan = Column(DateTime)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    montfact = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    abono = Column(Numeric(16, 6), nullable=False)
    cargo = Column(Numeric(16, 6), nullable=False)
    hmontfact = Column(Numeric(16, 6), nullable=False)
    habono = Column(Numeric(16, 6), nullable=False)
    hcargo = Column(Numeric(16, 6), nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    invcliente = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    incluir = Column(Boolean, nullable=False)
    vendedor = Column(Integer, nullable=False)
    cheque = Column(Boolean, nullable=False)
    nocheque = Column(String(15), nullable=False)
    montochq = Column(Numeric(16, 6), nullable=False)
    hexenta = Column(Numeric(18, 6), nullable=False)
    hviva = Column(Numeric(18, 6), nullable=False)
    enruta = Column(Boolean, nullable=False)
    escheque = Column(Boolean, nullable=False)
    bodega = Column(Integer, nullable=False)
    notas = Column(String(200), nullable=False)
    DPAGOS = Column(Integer, nullable=False)
    CAJA = Column(Integer, nullable=False)
    apagar = Column(Boolean, nullable=False)
    ccontrato = Column(Integer, nullable=False)
    cambodega = Column(Integer, nullable=False)
    montoaplicar = Column(Numeric(18, 6), nullable=False)
    esprima = Column(Boolean, nullable=False)
    ofactura = Column(Integer, nullable=False)
    pdesc = Column(Numeric(18, 6), nullable=False)
    quedan = Column(String(9))
    fechaquedan = Column(DateTime)
    fechapago = Column(DateTime)

    # Relaciones
    # clientes_rel = relationship("Clientes", back_populates="invcliente_set")  # Comentado automáticamente
    # factura_rel = relationship("Factura", back_populates="invcliente_set")  # Comentado automáticamente
    # tipomov_rel = relationship("Tipomov", back_populates="invcliente_set")  # Comentado automáticamente
    # vendedor_rel = relationship("Vendedor", back_populates="invcliente_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Invcliente(invcliente={self.invcliente})>"