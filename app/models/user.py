from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric, Text, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"
    
    # Columna de clave primaria
    usuario = Column(Integer, primary_key=True)
    
    # Información básica del usuario
    nusuario = Column(String(30))
    correo = Column(String(250))
    email = Column(String(30))
    clave = Column(String(250))
    hash = Column(Text)
    llave = Column(Text)
    foto = Column(LargeBinary)
    nota = Column(String(250))
    
    # Estatus y rol general
    activo = Column(Boolean)
    administrador = Column(Boolean)
    empresa = Column(Integer)
    roles = Column(Integer)
    PerfilUsuario = Column(Integer)
    
    # Permisos generales
    acceso = Column(Integer)
    crear = Column(Integer)
    modificar = Column(Integer)
    eliminar = Column(Integer)
    imprimir = Column(Integer)
    excel = Column(Integer)
    reporte = Column(Integer)
    lectura = Column(Boolean)
    escritura = Column(Boolean)
    
    # Permisos por departamento/área
    administracion = Column(Boolean)
    ventas = Column(Boolean)
    bodega = Column(Boolean)
    gerencial = Column(Boolean)
    Autoriza = Column(Boolean)
    Supervisa = Column(Boolean)
    Produccion = Column(Boolean)
    supervisor = Column(Boolean)
    puedeSupervisor = Column(Boolean)
    
    # Permisos contables
    estadocta = Column(Boolean)
    cierremes = Column(Boolean)
    conta1 = Column(Boolean)
    conta2 = Column(Boolean)
    conta3 = Column(Boolean)
    conta4 = Column(Boolean)
    conta5 = Column(Boolean)
    conta6 = Column(Boolean)
    conta7 = Column(Boolean)
    
    # Permisos de precios y costos
    cambiaprecio = Column(Boolean)
    puedePrecio = Column(Boolean)
    actualizaprecio = Column(Boolean)
    vecostos = Column(Boolean)
    
    # Permisos de inventario
    puedecorte = Column(Boolean)
    invkardexbloqueado = Column(Boolean)
    vecompras = Column(Boolean)
    
    # Otros permisos específicos
    REGISTRADO = Column(Boolean)
    puedeBackup = Column(Boolean)
    vecortecaja = Column(Boolean)
    otrospermisos = Column(Boolean)
    
    # Flags de uso múltiple o para funcionalidades futuras
    uno = Column(Boolean)
    dos = Column(Boolean)
    tres = Column(Boolean)
    cuatro = Column(Boolean)
    cinco = Column(Boolean)
    seis = Column(Boolean)
    siete = Column(Boolean)
    ocho = Column(Boolean)
    nueve = Column(Boolean)
    diez = Column(Boolean)
    
    # Información relacionada con tiempo y costos
    horatiempo = Column(DateTime)
    costohora = Column(Numeric(18, 6))
    fechacambio = Column(DateTime)
    cambiolaClave = Column(Boolean)
    
    # Relaciones con otras tablas
    vendedor = Column(Integer)
    
    # Añadir esta relación
    empresas_rel = relationship("UsuarioEmpresa", back_populates="usuario_rel")
    
    def __repr__(self):
        return f"<Usuario(id={self.usuario}, nombre='{self.nusuario}', email='{self.email}')>"
    
User = Usuario