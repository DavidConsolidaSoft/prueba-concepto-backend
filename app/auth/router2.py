from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import uget_db
from . import schemas, models, oauth, two_factor, utils
from typing import Optional
from datetime import timedelta
from . import azure_auth
from fastapi import Request, Depends
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
two_fa = two_factor.TwoFactorAuth()

@router.get("/azure-login")
async def azure_login():
    """
    Inicia el flujo de autenticación con Microsoft Entra ID
    """
    auth_url = azure_auth.get_auth_url()
    return auth_url

# Ruta para el callback de Microsoft Entra ID
@router.get("/callback")
async def azure_callback(code: str, state: str = None, db: Session = Depends(uget_db)):
    """
    Maneja el callback después de la autenticación con Microsoft Entra ID
    """
    result = await azure_auth.authenticate_azure_user(code, db)
    # En un entorno real, podrías redirigir a una página de éxito con el token
    # Por ahora, simplemente devolvemos el token
    return result

# Ruta protegida que requiere autenticación
@router.get("/me", response_model=schemas.UserResponse)
async def get_current_user(user: models.User = Depends(azure_auth.get_current_user)):
    """
    Devuelve la información del usuario autenticado
    """
    return user