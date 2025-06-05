# app/models/facturacion/dfactura.py
from sqlalchemy import Column, Integer, String, DateTime, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.all_models import Base

class DFactura(Base):
    __tablename__ = "dfactura"
    
    # Clave primaria
    dfactura = Column(Integer, primary_key=True)
    
    # Relación con factura
    factura = Column(Integer, ForeignKey("factura.factura"))
    
    # Relación con kardex/producto
    kardex = Column(Integer)
    producto = Column(Integer)
    
    # Información del producto
    codbarra = Column(String(50))
    nombre = Column(String(200))
    
    # Cantidades
    cantidad = Column(Numeric(18, 4))
    reservado = Column(Numeric(18, 4))
    bonificado = Column(Numeric(18, 4))
    uvendidas = Column(Numeric(18, 4))
    
    # Precios y descuentos
    precio = Column(Numeric(18, 4))
    oprecio = Column(Numeric(18, 4))
    pdesc = Column(Numeric(10, 2))
    vdesc = Column(Numeric(18, 2))
    yvdesc = Column(Numeric(18, 2))
    apdesc = Column(Numeric(10, 2))
    
    # Valores calculados
    afecta = Column(Numeric(18, 2))
    exenta = Column(Numeric(18, 2))
    impuesto = Column(Numeric(18, 2))
    monto = Column(Numeric(18, 2))
    gratificado = Column(Integer)
    gratif = Column(Numeric(18, 2))
    gratificadouventa = Column(Numeric(18, 2))
    
    # Otros valores monetarios
    fovial = Column(Numeric(18, 2))
    cotrans = Column(Numeric(18, 2))
    descglobal = Column(Numeric(18, 2))
    nosujeto = Column(Numeric(18, 2))
    costo = Column(Numeric(18, 4))
    tallak = Column(Numeric(18, 4))
    
    # Identificadores
    empresa = Column(Integer)
    vendedor = Column(Integer)
    talonario = Column(Integer)
    linea = Column(Integer)
    umedida = Column(Integer)
    
    # Estados y configuración
    estado = Column(Integer)
    vinculado = Column(Boolean)
    exento = Column(Integer)
    bitnosujeto = Column(Integer)
    servicios = Column(Boolean)
    parte = Column(Boolean)
    apliquemora = Column(Boolean)
    
    # Valores adicionales
    pcomision = Column(Numeric(10, 2))
    peso = Column(Numeric(18, 4))
    recargo = Column(Numeric(18, 2))
    condicion1 = Column(Numeric(18, 2))
    fraccion = Column(Numeric(18, 4))
    factor = Column(Numeric(18, 4))
    
    # Otros campos
    texto = Column(String(500))
    mformula = Column(Integer)
    dregciclo = Column(Integer)
    cicloanterior = Column(Numeric(18, 2))
    factalm = Column(Integer)
    preciolista = Column(Numeric(18, 4))
    
    # Timestamp
    horatiempo = Column(DateTime)
    
    # Fecha de vencimiento (puede ser null)
    fecvence = Column(DateTime)
    
    # Relaciones (si las necesitas)
    # factura_rel = relationship("Factura", back_populates="detalles")
    
    def __repr__(self):
        return f"<DFactura(id={self.dfactura}, factura={self.factura}, producto='{self.nombre}')>"