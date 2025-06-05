from datetime import datetime, timedelta, timezone
import os
from typing import Optional
from jose import JWTError, jwt
from fastapi import HTTPException, status
from passlib.context import CryptContext

# Configuración de JWT
secret = os.getenv('SECRET_KEY')  # Cambia esto en producción
ALGORITHM = "HS256"
access_time = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30)

# Configuración de hash de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Crea un token JWT con los datos proporcionados
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=access_time)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> dict:
    """
    Verifica un token JWT y retorna los datos decodificados
    """
    try:
        payload = jwt.decode(token, secret, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

def get_password_hash(password: str) -> str:
    """
    Genera un hash de la contraseña proporcionada
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña coincide con su hash
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_current_user_email(token: str) -> str:
    """
    Obtiene el email del usuario actual desde el token
    """
    payload = verify_token(token)
    email: str = payload.get("sub")
    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return email