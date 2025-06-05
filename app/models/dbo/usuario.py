# Generado automáticamente
# Tabla: dbo.usuario
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, LargeBinary
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
from sqlalchemy import Column, Text


class Usuario(Base):
    __tablename__ = "usuario"
    __table_args__ = {"schema": "dbo"}

    nusuario = Column(String(30), nullable=False)
    activo = Column(Boolean, nullable=False)
    administrador = Column(Boolean, nullable=False)
    acceso = Column(Integer, nullable=False)
    crear = Column(Integer, nullable=False)
    modificar = Column(Integer, nullable=False)
    eliminar = Column(Integer, nullable=False)
    imprimir = Column(Integer, nullable=False)
    excel = Column(Integer, nullable=False)
    reporte = Column(Integer, nullable=False)
    clave = Column(String(250))
    nota = Column(String(250))
    foto = Column(LargeBinary)
    usuario = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    costohora = Column(Numeric(18, 6), nullable=False)
    roles = Column(Integer, nullable=False)
    lectura = Column(Boolean, nullable=False)
    escritura = Column(Boolean, nullable=False)
    REGISTRADO = Column(Boolean, nullable=False)
    estadocta = Column(Boolean, nullable=False)
    cierremes = Column(Boolean, nullable=False)
    gerencial = Column(Boolean, nullable=False)
    Autoriza = Column(Boolean, nullable=False)
    Supervisa = Column(Boolean, nullable=False)
    Produccion = Column(Boolean, nullable=False)
    administracion = Column(Boolean, nullable=False)
    ventas = Column(Boolean, nullable=False)
    bodega = Column(Boolean, nullable=False)
    puedecorte = Column(Boolean, nullable=False)
    invkardexbloqueado = Column(Boolean, nullable=False)
    supervisor = Column(Boolean, nullable=False)
    vecostos = Column(Boolean, nullable=False)
    puedeBackup = Column(Boolean, nullable=False)
    puedePrecio = Column(Boolean, nullable=False)
    vecompras = Column(Boolean, nullable=False)
    PerfilUsuario = Column(Integer, nullable=False)
    cambiaprecio = Column(Boolean, nullable=False)
    uno = Column(Boolean, nullable=False)
    dos = Column(Boolean, nullable=False)
    tres = Column(Boolean, nullable=False)
    cuatro = Column(Boolean, nullable=False)
    cinco = Column(Boolean, nullable=False)
    seis = Column(Boolean, nullable=False)
    siete = Column(Boolean, nullable=False)
    ocho = Column(Boolean, nullable=False)
    nueve = Column(Boolean, nullable=False)
    diez = Column(Boolean, nullable=False)
    correo = Column(String(250), nullable=False)
    conta1 = Column(Boolean, nullable=False)
    conta2 = Column(Boolean, nullable=False)
    conta3 = Column(Boolean, nullable=False)
    conta4 = Column(Boolean, nullable=False)
    conta5 = Column(Boolean, nullable=False)
    conta6 = Column(Boolean, nullable=False)
    vendedor = Column(Integer, nullable=False)
    puedeSupervisor = Column(Boolean, nullable=False)
    otrospermisos = Column(Boolean, nullable=False)
    actualizaprecio = Column(Boolean, nullable=False)
    conta7 = Column(Boolean, nullable=False)
    fechacambio = Column(DateTime)
    cambiolaClave = Column(Boolean)
    vecortecaja = Column(Boolean, nullable=False)
    llave = Column(Text)
    email = Column(String(30))
    hash = Column(Text)

    def __repr__(self):
        return "<Usuario(usuario={self.usuario})>"