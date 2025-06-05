from typing import Optional, Dict, Any
import os
import msal
import requests
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from sqlalchemy.orm import Session
from app.db.database import uget_db
from . import models, utils

# Configuración de Microsoft Entra ID External
CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
EXTERNAL_TENANT_ID = os.getenv("AZURE_EXTERNAL_TENANT_ID")
EXTERNAL_AUTHORITY = f"https://login.microsoftonline.com/{EXTERNAL_TENANT_ID}"
REDIRECT_URI = os.getenv("AZURE_REDIRECT_URI")

# Configuramos el esquema OAuth2 para la autenticación External
azure_external_oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{EXTERNAL_AUTHORITY}/oauth2/v2.0/authorize",
    tokenUrl=f"{EXTERNAL_AUTHORITY}/oauth2/v2.0/token",
    scopes={"openid": "OpenID Connect", "profile": "User Profile", "email": "User Email"}
)

# Creamos el cliente de autenticación de MSAL para External
external_app = msal.ConfidentialClientApplication(
    client_id=CLIENT_ID,
    client_credential=CLIENT_SECRET,
    authority=EXTERNAL_AUTHORITY
)

def get_external_auth_url() -> Dict[str, str]:
    """
    Genera la URL para iniciar el flujo de autorización de Microsoft Entra ID External
    """
    auth_url = external_app.get_authorization_request_url(
        scopes=["openid", "profile", "email", "User.Read"],
        redirect_uri=REDIRECT_URI,
        state="external-auth"
    )
    return {"auth_url": auth_url}

async def get_external_token_from_code(code: str) -> Dict[str, Any]:
    """
    Intercambia el código de autorización por un token de acceso (para usuarios externos)
    """
    result = external_app.acquire_token_by_authorization_code(
        code=code,
        scopes=["openid", "profile", "email", "User.Read"],
        redirect_uri=REDIRECT_URI
    )
    
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Azure External authentication error: {result.get('error_description', 'Unknown error')}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return result

async def authenticate_external_user(code: str, db: Session) -> Dict[str, Any]:
    """
    Autentica al usuario externo con Microsoft Entra ID External
    """
    token_result = await get_external_token_from_code(code)
    access_token = token_result.get("access_token")
    id_token_claims = token_result.get("id_token_claims", {})
    
    if not id_token_claims:
        # Obtenemos la información del usuario desde Microsoft Graph
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get("https://graph.microsoft.com/v1.0/me", headers=headers)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to get external user info from Microsoft Graph API",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        user_info = response.json()
    else:
        user_info = id_token_claims
    
    # Buscamos o creamos el usuario en la base de datos
    user = db.query(models.User).filter(models.User.email == user_info.get("email")).first()
    
    if not user:
        # Si el usuario no existe, lo creamos
        user = models.User(
            email=user_info.get("email"),
            full_name=user_info.get("name", ""),
            hashed_password=None,  # No se necesita contraseña para la autenticación de Azure
            is_external=True  # Marcamos que es un usuario externo
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    
    # Generamos un token JWT para la sesión del usuario
    access_token = utils.create_access_token(data={"sub": user.email, "is_external": True})
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "requires_2fa": user.is_2fa_enabled,
        "user_info": {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name,
            "is_external": True
        }
    }