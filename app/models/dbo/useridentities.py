# Generado automáticamente
# Tabla: dbo.userIdentities
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Useridentities(Base):
    __tablename__ = "userIdentities"
    __table_args__ = {"schema": "dbo"}

    Id = Column(String(450), primary_key=True, nullable=False)
    UserName = Column(String)
    NormalizedUserName = Column(String)
    Email = Column(String)
    NormalizedEmail = Column(String)
    EmailConfirmed = Column(Boolean, nullable=False)
    PasswordHash = Column(String)
    SecurityStamp = Column(String)
    ConcurrencyStamp = Column(String)
    PhoneNumber = Column(String)
    PhoneNumberConfirmed = Column(Boolean, nullable=False)
    TwoFactorEnabled = Column(Boolean, nullable=False)
    LockoutEnd = Column(String)
    LockoutEnabled = Column(Boolean, nullable=False)
    AccessFailedCount = Column(Integer, nullable=False)
    caja = Column(Integer)

    def __repr__(self):
        return "<Useridentities(Id={self.Id})>"