from typing import Optional, Dict, Any
import os
import msal
import requests
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from sqlalchemy.orm import Session
from app.db.database import uget_db
from . import models, utils

CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
TENANT_ID = os.getenv("AZURE_TENANT_ID")
AUTHORITY = os.getenv("AZURE_AUTHORITY")
REDIRECT_URI = os.getenv("AZURE_REDIRECT_URI")

EXTERNAL_TENANT_ID = os.getenv("AZURE_EXTERNAL_TENANT_ID")

azure_oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{AUTHORITY}/oauth2/v2.0/authorize",
    tokenUrl=f"{AUTHORITY}/oauth2/v2.0/token",
    scopes={"openid": "OpenID Connect", "profile": "User Profile", "email": "User Email"}
)

app = msal.ConfidentialClientApplication(
    client_id=CLIENT_ID,
    client_credential=CLIENT_SECRET,
    authority=AUTHORITY
)

def get_auth_url() -> Dict[str, str]:
    """
    Genera la URL para iniciar el flujo de autorización de Microsoft Entra ID
    """
    auth_url = app.get_authorization_request_url(
        scopes=["openid", "profile", "email", "User.Read"],
        redirect_uri=REDIRECT_URI,
        state="some-state-value"
    )
    return {"auth_url": auth_url}

async def get_token_from_code(code: str) -> Dict[str, Any]:
    """
    Intercambia el código de autorización por un token de acceso
    """
    result = app.acquire_token_by_authorization_code(
        code=code,
        scopes=["openid", "profile", "email", "User.Read"],
        redirect_uri=REDIRECT_URI
    )
    
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Azure authentication error: {result.get('error_description', 'Unknown error')}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return result

async def get_user_info(token: str) -> Dict[str, Any]:
    """
    Obtiene la información del usuario utilizando el token de acceso
    """
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get("https://graph.microsoft.com/v1.0/me", headers=headers)
    
    if response.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed to get user info from Microsoft Graph API",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return response.json()

async def authenticate_azure_user(code: str, db: Session) -> Dict[str, Any]:
    """
    Autentica al usuario con Microsoft Entra ID y crea/actualiza el usuario en la base de datos
    """
    token_result = await get_token_from_code(code)
    access_token = token_result.get("access_token")
    id_token_claims = token_result.get("id_token_claims", {})
    
    # Si no hay claims en el id_token, obtenemos la información del usuario desde Microsoft Graph
    if not id_token_claims:
        user_info = await get_user_info(access_token)
    else:
        user_info = id_token_claims
    
    # Buscamos o creamos el usuario en la base de datos
    user = db.query(models.User).filter(models.User.email == user_info.get("email")).first()
    
    if not user:
        # Si el usuario no existe, lo creamos
        user = models.User(
            email=user_info.get("email"),
            full_name=user_info.get("name", ""),
            hashed_password=None  # No se necesita contraseña para la autenticación de Azure
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    
    # Generamos un token JWT para la sesión del usuario
    access_token = utils.create_access_token(data={"sub": user.email})
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "requires_2fa": user.is_2fa_enabled,
        "user_info": {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name
        }
    }

async def verify_azure_token(token: str) -> Dict[str, Any]:
    """
    Verifica el token de Microsoft Entra ID
    """
    # Esto es una simplificación, en un entorno de producción deberías validar el token con las claves públicas de Microsoft
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get("https://graph.microsoft.com/v1.0/me", headers=headers)
    
    if response.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired Microsoft Entra ID token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return response.json()

async def get_current_user(token: str = Depends(azure_oauth2_scheme), db: Session = Depends(uget_db)):
    """
    Middleware para obtener el usuario actual a partir del token JWT
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