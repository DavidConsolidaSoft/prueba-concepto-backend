# app/models/facturacion/clientes.py
from sqlalchemy import Column, Integer, String, Boolean, Numeric, DateTime
from app.models.all_models import Base

class Clientes(Base):
    __tablename__ = "clientes"
    
    # Identificadores
    clientes = Column(String(50), primary_key=True)
    empresa = Column(Integer)
    
    # Información básica
    nclientes = Column(String(100))
    registro = Column(String(50))
    direccion = Column(String(200))
    telefono1 = Column(String(20))
    telefono2 = Column(String(20))
    email = Column(String(100))
    
    # Información fiscal
    nit = Column(String(20))
    dui = Column(String(20))
    razonsoc = Column(String(100))
    giro = Column(String(100))
    
    # Información geográfica
    municip = Column(Integer)
    depto = Column(Integer)
    zona = Column(Integer)
    
    # Configuración
    contado = Column(Boolean, default=False)
    tipcli = Column(Integer)
    
    # Referencias
    referencia1 = Column(String(50))
    referencia2 = Column(String(50))
    valorreferencia1 = Column(Integer)
    valorreferencia2 = Column(Integer)
    valorreferencia3 = Column(Integer)
    valorreferencia4 = Column(Integer)
    
    # Crédito
    limitecredito = Column(Numeric(18, 2))
    conpagare = Column(Boolean)
    
    # Otros campos
    trabajo = Column(String(100))
    propietario = Column(String(100))
    direnvio = Column(String(200))
    localidad = Column(String(100))
    notas = Column(String(500))
    
    # Estados
    activo = Column(Boolean, default=True)
    exento = Column(Boolean, default=False)
    nosujeto = Column(Boolean, default=False)
    
    # Valores monetarios
    retencion = Column(Numeric(18, 2))
    percepcion = Column(Numeric(18, 2))
    
    def __repr__(self):
        return f"<Clientes(id={self.clientes}, nombre='{self.nclientes}')>"