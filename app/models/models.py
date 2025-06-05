# app/db/models/facturacion/models.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Factura(Base):
    __tablename__ = "factura"
    
    factura = Column(Integer, primary_key=True)
    empresa = Column(Integer, ForeignKey("empresa.empresa"))
    numedocu = Column(String(50))
    fecha = Column(DateTime)
    fecha1 = Column(DateTime)
    clientes = Column(String(50), ForeignKey("clientes.clientes"))
    vendedor = Column(Integer, ForeignKey("vendedor.vendedor"))
    tipomov = Column(Integer, ForeignKey("tipomov.tipomov"))
    tipovta = Column(Integer, ForeignKey("tipovta.tipovta"))
    condpago = Column(Integer, ForeignKey("condpago.condpago"))
    bodega = Column(Integer, ForeignKey("bodega.bodega"))
    caja = Column(Integer, ForeignKey("caja.caja"))
    montfact = Column(Numeric(18, 2))
    afecta = Column(Numeric(18, 2))
    exenta = Column(Numeric(18, 2))
    iva = Column(Numeric(18, 2))
    percepcion = Column(Numeric(18, 2))
    retencion = Column(Numeric(18, 2))
    propina = Column(Numeric(18, 2))
    vdesc = Column(Numeric(18, 2))
    dgratif = Column(Numeric(18, 2))
    pdesc = Column(Numeric(10, 2))
    impresa = Column(Boolean)
    nula = Column(Boolean)
    estado = Column(Integer)
    notas = Column(String(500))
    pedido = Column(String(50))
    efectivo = Column(Numeric(18, 2))
    cheque = Column(Numeric(18, 2))
    tarjeta = Column(Numeric(18, 2))
    tipopago = Column(Integer)
    
    # Relationships
    empresa_rel = relationship("Empresa", back_populates="facturas")
    cliente_rel = relationship("Clientes", back_populates="facturas")
    vendedor_rel = relationship("Vendedor", back_populates="facturas")
    tipomov_rel = relationship("TipoMov", back_populates="facturas")
    tipovta_rel = relationship("TipoVta", back_populates="facturas")
    condpago_rel = relationship("CondPago", back_populates="facturas")
    bodega_rel = relationship("Bodega", back_populates="facturas")
    caja_rel = relationship("Caja", back_populates="facturas")
    detalles = relationship("DFactura", back_populates="factura_rel")
    factcont_rel = relationship("FactCont", back_populates="factura_rel", uselist=False)

class DFactura(Base):
    __tablename__ = "dfactura"
    
    dfactura = Column(Integer, primary_key=True)
    factura = Column(Integer, ForeignKey("factura.factura"))
    kardex = Column(Integer, ForeignKey("kardex.kardex"))
    cantidad = Column(Numeric(18, 4))
    bonificado = Column(Numeric(18, 4))
    precio = Column(Numeric(18, 4))
    pdesc = Column(Numeric(10, 2))
    vdesc = Column(Numeric(18, 2))
    afecta = Column(Numeric(18, 2))
    exenta = Column(Numeric(18, 2))
    viva = Column(Numeric(18, 2))
    montfact = Column(Numeric(18, 2))
    gratificado = Column(Integer)
    gratif = Column(Numeric(18, 2))
    
    # Relationships
    factura_rel = relationship("Factura", back_populates="detalles")
    kardex_rel = relationship("Kardex")

class Clientes(Base):
    __tablename__ = "clientes"
    
    clientes = Column(String(50), primary_key=True)
    empresa = Column(Integer)
    nclientes = Column(String(100))
    registro = Column(String(50))
    direccion = Column(String(200))
    telefono1 = Column(String(20))
    nit = Column(String(20))
    dui = Column(String(20))
    contado = Column(Boolean)
    
    # Relationships
    facturas = relationship("Factura", back_populates="cliente_rel")

class FactCont(Base):
    __tablename__ = "factcont"
    
    factcont = Column(Integer, primary_key=True)
    factura = Column(Integer, ForeignKey("factura.factura"))
    nclientes = Column(String(100))
    registro = Column(String(50))
    direccion = Column(String(200))
    dui = Column(String(20))
    
    # Relationships
    factura_rel = relationship("Factura", back_populates="factcont_rel")

class Vendedor(Base):
    __tablename__ = "vendedor"
    
    vendedor = Column(Integer, primary_key=True)
    nvendedor = Column(String(100))
    
    # Relationships
    facturas = relationship("Factura", back_populates="vendedor_rel")

class TipoMov(Base):
    __tablename__ = "tipomov"
    
    tipomov = Column(Integer, primary_key=True)
    ntipomov = Column(String(100))
    factura = Column(Boolean)
    anticipo = Column(Boolean)
    notacred = Column(Boolean)
    
    # Relationships
    facturas = relationship("Factura", back_populates="tipomov_rel")

class Empresa(Base):
    __tablename__ = "empresa"
    
    empresa = Column(Integer, primary_key=True)
    nempresa = Column(String(100))
    
    # Relationships
    facturas = relationship("Factura", back_populates="empresa_rel")

class CondPago(Base):
    __tablename__ = "condpago"
    
    condpago = Column(Integer, primary_key=True)
    ncondpago = Column(String(100))
    plazo = Column(Integer)
    
    # Relationships
    facturas = relationship("Factura", back_populates="condpago_rel")

class Caja(Base):
    __tablename__ = "caja"
    
    caja = Column(Integer, primary_key=True)
    ncaja = Column(String(100))
    
    # Relationships
    facturas = relationship("Factura", back_populates="caja_rel")

class Kardex(Base):
    __tablename__ = "kardex"
    
    kardex = Column(Integer, primary_key=True)
    producto = Column(Integer, ForeignKey("producto.producto"))
    lote = Column(Integer, ForeignKey("lote.lote"))
    bodega = Column(Integer, ForeignKey("bodega.bodega"))
    cantidad = Column(Numeric(18, 4))
    
    # Relationships
    producto_rel = relationship("Producto")
    lote_rel = relationship("Lote")
    bodega_rel = relationship("Bodega")

class Producto(Base):
    __tablename__ = "producto"
    
    producto = Column(Integer, primary_key=True)
    nproducto = Column(String(200))
    icdbarra = Column(String(50))
    exento = Column(Boolean)
    servicios = Column(Boolean)
    tipoprod = Column(Integer, ForeignKey("tipoprod.tipoprod"))
    
    # Relationships
    tipoprod_rel = relationship("TipoProd")

class TipoProd(Base):
    __tablename__ = "tipoprod"
    
    tipoprod = Column(Integer, primary_key=True)
    ntipoprod = Column(String(100))

class Lote(Base):
    __tablename__ = "lote"
    
    lote = Column(Integer, primary_key=True)
    nolote = Column(String(50))

class Bodega(Base):
    __tablename__ = "bodega"
    
    bodega = Column(Integer, primary_key=True)
    nbodega = Column(String(100))
    
    # Relationships
    facturas = relationship("Factura", back_populates="bodega_rel")