from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UsuarioEmpresa(Base):
    __tablename__ = "usuarioEmpresa"
    
    # Clave primaria
    usuarioEmpresa = Column(Integer, primary_key=True)
    
    # Claves foráneas
    usuario = Column(Integer, ForeignKey("usuario.usuario"))
    empresa = Column(Integer, ForeignKey("empresa.empresa"))
    
    # Campos adicionales
    activo = Column(Boolean)
    rempresa = Column(Integer)  # Referencias adicionales
    rusuario = Column(Integer)  # Referencias adicionales
    horatiempo = Column(DateTime)
    
    # Relaciones (opcional, depende de cómo quieras estructurar tu ORM)
    usuario_rel = relationship("Usuario", back_populates="empresas_rel")
    empresa_rel = relationship("Empresa", back_populates="usuarios_rel")
    
    def __repr__(self):
        return f"<UsuarioEmpresa(id={self.usuarioEmpresa}, usuario_id={self.usuario}, empresa_id={self.empresa})>"