from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Empresa(Base):
    __tablename__ = "empresa"
    
    # Clave primaria
    empresa = Column(Integer, primary_key=True)
    
    # Información básica de la empresa
    nempresa = Column(String(55))
    activo = Column(Boolean)
    direccion = Column(String(60))
    dirFactura = Column(String(250))
    telefono1 = Column(String(14))
    telefono2 = Column(String(14))
    fax = Column(String(14))
    email = Column(String(150))
    
    # Información legal
    registro = Column(String(20))
    dui = Column(String(20))
    nit = Column(String(20))
    numissspat = Column(String(9))
    giro = Column(String(60))
    representa = Column(String(55))
    
    # Información geográfica
    municip = Column(Integer)
    PAIS = Column(Integer)
    MONEDA = Column(Integer)
    
    # Configuración de países
    elSalvador = Column(Boolean)
    Guatemala = Column(Boolean)
    nicaragua = Column(Boolean)
    honduras = Column(Boolean)
    costarica = Column(Boolean)
    panama = Column(Boolean)
    estadosunidos = Column(Boolean)
    mexico = Column(Boolean)
    chile = Column(Boolean)
    ecuador = Column(Boolean)
    peru = Column(Boolean)
    venezuela = Column(Boolean)
    
    # Configuración de puertos
    puertoDescarga = Column(String(35))
    puertoEntrega = Column(String(35))
    
    # Configuración de impuestos
    fPercepcion = Column(Integer)
    pPercepcion = Column(Boolean)
    fRetencion = Column(Integer)
    pRetencion = Column(Boolean)
    vretencion = Column(Boolean)
    vpercepcion = Column(Boolean)
    sinImpuesto = Column(Boolean)
    isr = Column(Numeric(18, 6))
    aportacionsoli = Column(Numeric(18, 6))
    
    # Configuración de precios
    preciocaja = Column(Boolean)
    variosprecios = Column(Boolean)
    precioenCompra = Column(Boolean)
    escoje_precio = Column(Boolean)
    PrecioCompcIva = Column(Boolean)
    blockcprecio = Column(Boolean)
    cambiaPrecios = Column(Boolean)
    cambiaLprecio = Column(Boolean)
    margenPrecio = Column(Boolean)
    descxvol = Column(Boolean)
    descxval = Column(Boolean)
    cuantasListasPrecio = Column(Integer)
    
    # Configuración de inventario
    soloExistencias = Column(Boolean)
    manejaLote = Column(Boolean)
    pcontrolexist = Column(Boolean)
    consigna = Column(Boolean)
    sipreciocosto = Column(Boolean)
    
    # Configuración de ventas
    vendedorbodega = Column(Boolean)
    bonifica = Column(Boolean)
    solocontado = Column(Boolean)
    solocredito = Column(Boolean)
    boniplus = Column(Boolean)
    tasaInteres = Column(Numeric(5, 2))
    lockvendedor = Column(Boolean)
    gestionventa = Column(Integer)
    
    # Configuración de impresión
    escogerprinter = Column(Boolean)
    vistaprevia = Column(Boolean)
    confirmaprint = Column(Boolean)
    justprint = Column(Boolean)
    noselectPrint = Column(Integer)
    cuantosPrint = Column(Integer)
    
    # Configuración de seguridad
    activapermisos = Column(Boolean)
    fseguridad = Column(Boolean)
    obligaclave = Column(Boolean)
    mesobligaclave = Column(Integer)
    
    # Metadatos y auditoría
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    
    # Configuración de documentos
    docunico = Column(Boolean)
    autorizacion = Column(String(25))
    correlativoQuedan = Column(Integer)
    
    # Configuración de operación
    planilla30 = Column(Boolean)
    sidomingo = Column(Boolean)
    ppistola = Column(Boolean)
    preparapedido = Column(Boolean)
    rembodcaja = Column(Boolean)
    cajanumero = Column(String(100))
    cdespacho = Column(Boolean)
    
    # Configuraciones especiales
    pcloud = Column(Boolean)
    rutareloj = Column(String(300))
    notas = Column(String(350))
    autosinctipomov = Column(Boolean)
    sinInternet = Column(Boolean)
    preservado = Column(Boolean)
    offline = Column(Boolean)
    
    # Configuraciones específicas de negocio
    escalzado = Column(Boolean)
    esdefinitiva = Column(Boolean)
    siCantidad = Column(Boolean)
    blockCliRapido = Column(Boolean)
    llevacxp = Column(Boolean)
    solof2 = Column(Boolean)
    busca_por_registro = Column(Boolean)
    prefijarcantuno = Column(Integer)
    factor_fob = Column(Numeric(5, 2))
    a90 = Column(Boolean)
    iglesia = Column(Boolean)
    cambioacero = Column(Boolean)
    esfactor = Column(Boolean)
    tipo = Column(Integer)
    conemail = Column(Boolean)
    
    usuarios_rel = relationship("UsuarioEmpresa", back_populates="empresa_rel")
    
    def __repr__(self):
        return f"<Empresa(id={self.empresa}, nombre='{self.nempresa}')>"