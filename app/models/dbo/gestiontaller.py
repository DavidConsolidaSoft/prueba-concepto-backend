# Generado automáticamente
# Tabla: dbo.GestionTaller
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Gestiontaller(Base):
    __tablename__ = "GestionTaller"
    __table_args__ = {"schema": "dbo"}

    GestionTaller = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tipomov = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    lote = Column(Integer, nullable=False)
    fase = Column(Integer, nullable=False)
    numedocu = Column(String(12), nullable=False)
    fecha = Column(DateTime, nullable=False)
    fecvence = Column(DateTime, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    suspendida = Column(Boolean, nullable=False)
    aReservado = Column(Boolean, nullable=False)
    nolote = Column(String(20), nullable=False)
    notas = Column(String(250), nullable=False)
    adicion = Column(Boolean, nullable=False)
    devolucion = Column(Boolean, nullable=False)
    perdida = Column(Numeric(18, 6), nullable=False)
    cantidad = Column(Numeric(18, 6), nullable=False)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    rupstatus = Column(Integer, nullable=False)
    camion = Column(Integer, nullable=False)
    rupfase = Column(Integer, nullable=False)
    RTFrontNew = Column(Boolean, nullable=False)
    RTFrontRecord = Column(Boolean, nullable=False)
    RTFrontFlat = Column(Boolean, nullable=False)
    LTFrontNew = Column(Boolean, nullable=False)
    LTFrontRecord = Column(Boolean, nullable=False)
    LTFrontFlat = Column(Boolean, nullable=False)
    STNew = Column(Boolean, nullable=False)
    STRecord = Column(Boolean, nullable=False)
    STFlat = Column(Boolean, nullable=False)
    RTBackNew = Column(Boolean, nullable=False)
    RTBackRecord = Column(Boolean, nullable=False)
    RTBackFlat = Column(Boolean, nullable=False)
    LTBackNew = Column(Boolean, nullable=False)
    LTBackRecord = Column(Boolean, nullable=False)
    LTBackFlat = Column(Boolean, nullable=False)
    Mica = Column(Boolean, nullable=False)
    Spanner = Column(Boolean, nullable=False)
    Tools = Column(Boolean, nullable=False)
    extinguisher = Column(Boolean, nullable=False)
    triangles = Column(Boolean, nullable=False)
    GasCap = Column(Boolean, nullable=False)
    CCard = Column(Boolean, nullable=False)
    fuelTank = Column(String(3), nullable=False)
    LMirror = Column(Boolean, nullable=False)
    RMirror = Column(Boolean, nullable=False)
    RVMirror = Column(Boolean, nullable=False)
    Stereo = Column(Boolean, nullable=False)
    lighter = Column(Boolean, nullable=False)
    TSlock = Column(Boolean, nullable=False)
    PadLock = Column(Boolean, nullable=False)
    GoodSeat = Column(Boolean, nullable=False)
    BrokenSeat = Column(Boolean, nullable=False)
    DirtySeat = Column(Boolean, nullable=False)
    BSFront = Column(String(100), nullable=False)
    BSLeft = Column(String(100), nullable=False)
    BSRight = Column(String(100), nullable=False)
    BSBack = Column(String(100), nullable=False)
    kilometraje = Column(String(10), nullable=False)
    formulataller = Column(Integer, nullable=False)
    motorista = Column(Integer, nullable=False)
    clientes = Column(String(25), nullable=False)
    clientes2 = Column(String(25), nullable=False)
    comments = Column(String(200), nullable=False)
    facturado = Column(Boolean, nullable=False)
    fechafin = Column(DateTime)

    # Relaciones
    # camion_rel = relationship("Camion", back_populates="gestiontaller_set")  # Comentado automáticamente
    # clientes_rel = relationship("Clientes", back_populates="gestiontaller_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Gestiontaller(GestionTaller={self.GestionTaller})>"