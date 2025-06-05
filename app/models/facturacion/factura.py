from sqlalchemy import Column, Integer, String, DateTime, Numeric, Boolean, Text
from app.models.all_models import Base

class Factura(Base):
    __tablename__ = "factura"
    
    # Campos principales basados en FacturaResponse
    factura = Column(Integer, primary_key=True)
    basesiniva = Column(Boolean)
    bnotas = Column(String(500))
    docunico = Column(String(50))
    nocheque = Column(String(50))
    notarjeta = Column(String(50))
    retencion = Column(Numeric(18, 2))
    
    # Relaciones con otras tablas
    bodega = Column(Integer)
    clientes = Column(String(50))
    condpago = Column(Integer)
    
    # Fechas
    fecha = Column(DateTime)
    fecha1 = Column(DateTime)
    fecha2 = Column(DateTime)
    
    # Estados
    impresa = Column(Boolean, default=False)
    nula = Column(Boolean, default=False)
    estado = Column(Integer, default=0)
    enfirme = Column(Boolean)
    impbod = Column(Boolean)
    
    # Valores monetarios
    iva = Column(Numeric(18, 2))
    montfact = Column(Numeric(18, 2))
    afecta = Column(Numeric(18, 2))
    exenta = Column(Numeric(18, 2))
    viva = Column(Numeric(18, 2))
    vdesc = Column(Numeric(18, 2))
    pdesc = Column(Numeric(10, 2))
    propina = Column(Numeric(18, 2))
    percepcion = Column(Numeric(18, 2))
    fovial = Column(Numeric(18, 2))
    cotrans = Column(Numeric(18, 2))
    dgratif = Column(Numeric(18, 2))
    nosujeto = Column(Numeric(18, 2))
    
    # Identificadores
    numedocu = Column(String(50))
    pedido = Column(String(50))
    ordenno = Column(String(50))
    
    # Otros campos
    notas = Column(Text)
    nombreref = Column(String(100))
    docref = Column(String(50))
    
    # Claves foráneas
    moneda = Column(Integer)
    prodprec = Column(Integer)
    tipomov = Column(Integer)
    tipovta = Column(Integer)
    transpte = Column(Integer)
    vendedor = Column(Integer)
    clientes2 = Column(String(50))
    empresa = Column(Integer)
    caja = Column(Integer)
    usuario = Column(Integer)
    cobrador = Column(Integer)
    
    # Tiempo
    horatiempo = Column(DateTime)
    
    # Pagos
    efectivo = Column(Numeric(18, 2))
    cheque = Column(Numeric(18, 2))
    tarjeta = Column(Numeric(18, 2))
    tipopago = Column(Integer)
    aprobado = Column(Boolean)
    
    # Campos adicionales
    pesofactura = Column(Numeric(18, 4))
    encomienda = Column(Numeric(18, 2))
    nomesa = Column(String(50))
    
    # Referencias
    pagencia = Column(Numeric(18, 2))
    valorreferencia1 = Column(Integer)
    valorreferencia2 = Column(Integer)
    valorreferencia3 = Column(Integer)
    valorreferencia4 = Column(Integer)
    
    def __repr__(self):
        return f"<Factura(id={self.factura}, numedocu='{self.numedocu}', fecha={self.fecha})>"