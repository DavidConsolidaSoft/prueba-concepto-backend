from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric, Text, LargeBinary, ForeignKey
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
    
    # El resto de campos...
    
    # Relaciones - DEFINIDAS AL FINAL

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
    
    # El resto de campos...
    
    # Relaciones - DEFINIDAS AL FINAL

class UsuarioEmpresa(Base):
    __tablename__ = "usuarioEmpresa"
    
    # Clave primaria
    usuarioEmpresa = Column(Integer, primary_key=True)
    
    # Claves foráneas
    usuario = Column(Integer, ForeignKey("usuario.usuario"))
    empresa = Column(Integer, ForeignKey("empresa.empresa"))
    
    # Campos adicionales
    activo = Column(Boolean)
    rempresa = Column(Integer)
    rusuario = Column(Integer)
    horatiempo = Column(DateTime)
    
    # Relaciones - DEFINIDAS AL FINAL

# AHORA DEFINIMOS LAS RELACIONES
Usuario.empresas_rel = relationship("UsuarioEmpresa", back_populates="usuario_rel")
UsuarioEmpresa.usuario_rel = relationship("Usuario", back_populates="empresas_rel")
UsuarioEmpresa.empresa_rel = relationship("Empresa", back_populates="usuarios_rel")
Empresa.usuarios_rel = relationship("UsuarioEmpresa", back_populates="empresa_rel")