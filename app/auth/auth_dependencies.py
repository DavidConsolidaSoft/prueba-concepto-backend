from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.database import uget_db
from . import models, utils

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(uget_db)):
    """
    Middleware para obtener el usuario actual basado en el token JWT
    Puedes usar este Depends en cualquier ruta que requiera autenticación
    """
    email = utils.get_current_user_email(token)
    user = db.query(models.User).filter(models.User.email == email).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user

# Opcional: puedes crear un middleware adicional para verificar roles o permisos
async def get_current_admin_user(user: models.User = Depends(get_current_user)):
    """
    Middleware para verificar que el usuario actual sea un administrador
    """
    # Esto es solo un ejemplo, deberías implementar tu lógica de roles
    if not getattr(user, "is_admin", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions",
        )
    return user