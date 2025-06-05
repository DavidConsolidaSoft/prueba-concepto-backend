# Generado automáticamente
# Tabla: dbo.factcont
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente

class FactCont(Base):  # Cambiado de Factcont a FactCont
    __tablename__ = "factcont"
    __table_args__ = {"schema": "dbo", "extend_existing": True}
    
    factcont = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    factura = Column(Integer, nullable=False)
    nclientes = Column(String(50), nullable=False)
    registro = Column(String(20), nullable=False)
    nit = Column(String(20), nullable=False)
    direccion = Column(String(200), nullable=False)
    nmunicip = Column(String(20), nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    dui = Column(String(20), nullable=False)
    ofactura = Column(Integer, nullable=False)
    telefono = Column(String(10))
    
    # Relaciones - NOTA: hay un conflicto aquí, 'factura' está definido dos veces
    # # factura_rel = relationship("Factura", back_populates="factcont_set")  # Comentado automáticamente
    
    def __repr__(self):
        return f"<FactCont(factcont={self.factcont})>"