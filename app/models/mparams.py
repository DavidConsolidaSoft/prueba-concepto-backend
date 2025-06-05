from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ParamsDB(Base):
    __tablename__ = "vtabla"
   
    nombre = Column(String, nullable=False)
    nusuario = Column(String, nullable=False)
    cc = Column(String, nullable=False)
    id = Column("id", Integer, primary_key=True, index=True)
    empresa = Column(Integer, nullable=False)
    caja = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    prodprec = Column(Integer, nullable=False)