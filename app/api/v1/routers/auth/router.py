# app/api/v1/routers/auth/router.py - Versión simplificada usando settings
import json
import urllib.parse
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

# Importaciones según tu estructura
from app.db.database import get_db
from app.models.all_models import Usuario, Empresa, UsuarioEmpresa
from .azure_auth import authenticate_azure_user, get_auth_url
from .jwt_handler import create_access_token, verify_token

# Importar configuración centralizada
from app.core.config import settings

print(f"🔧 Router cargado con configuración:")
print(f"🌍 Environment: {settings.ENVIRONMENT}")
print(f"🔗 Frontend URL: {settings.FRONTEND_URL}")
print(f"📞 Callback URL: {settings.frontend_callback_url}")

# Crear el router
router = APIRouter()

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

@router.get("/azure-login")
async def azure_login(request: Request):
    """
    Endpoint para iniciar el proceso de autenticación con Microsoft
    """
    try:
        print("🚀 Iniciando proceso de login con Azure...")
        print(f"🌍 Environment: {settings.ENVIRONMENT}")
        print(f"🔗 Frontend: {settings.FRONTEND_URL}")
        
        # Obtener la URL de autenticación
        auth_data = get_auth_url()
        
        print(f"✅ URL de auth generada correctamente")
        
        return JSONResponse(content={
            "status": "success",
            "auth_url": auth_data["auth_url"],
            "environment": settings.ENVIRONMENT,
            "frontend_url": settings.FRONTEND_URL  # Para debugging
        })
    except Exception as e:
        print(f"❌ Error en azure-login: {str(e)}")
        import traceback
        print(traceback.format_exc())
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al generar URL de autenticación: {str(e)}"
        )

@router.get("/callback")
async def auth_callback(
    code: str = None,
    error: str = None,
    error_description: str = None,
    state: str = None,
    db: Session = Depends(get_db)
):
    """
    Endpoint de callback que recibe la respuesta de Microsoft Entra ID
    """
    try:
        print("🔄 === CALLBACK RECIBIDO ===")
        print(f"🌍 Environment: {settings.ENVIRONMENT}")
        print(f"🔄 Redirigiendo a: {settings.frontend_callback_url}")
        print(f"📝 Code: {code[:15] if code else 'None'}...")
        print(f"❌ Error: {error}")
        print(f"📄 Error description: {error_description}")
        print(f"🏷️ State: {state}")
        
        # Si hay un error de Microsoft
        if error:
            error_msg = error_description or error
            print(f"❌ Error de Microsoft: {error_msg}")
            
            # Redirigir al frontend con el error
            redirect_url = f"{settings.frontend_callback_url}?error={urllib.parse.quote(error)}&error_description={urllib.parse.quote(error_msg)}"
            print(f"🔄 Redirigiendo con error a: {redirect_url}")
            return RedirectResponse(url=redirect_url)
        
        # Si no hay código, es inválido
        if not code:
            print("❌ No se recibió código de autorización")
            redirect_url = f"{settings.frontend_callback_url}?error=missing_code&error_description=No se recibió código de autorización"
            print(f"🔄 Redirigiendo sin código a: {redirect_url}")
            return RedirectResponse(url=redirect_url)
        
        # Autenticar usuario
        print("🔐 Procesando autenticación...")
        auth_result = await authenticate_azure_user(code, db)
        
        if auth_result["status"] == "error":
            print(f"❌ Error en autenticación: {auth_result['message']}")
            error_msg = auth_result.get('message', 'Error de autenticación')
            redirect_url = f"{settings.frontend_callback_url}?error=auth_failed&error_description={urllib.parse.quote(error_msg)}"
            print(f"🔄 Redirigiendo con error de auth a: {redirect_url}")
            return RedirectResponse(url=redirect_url)
        
        # Autenticación exitosa - redirigir al frontend con los datos
        print("🎉 Autenticación exitosa, redirigiendo al frontend...")
        
        # Convertir a JSON y codificar para URL
        auth_result_json = json.dumps(auth_result)
        auth_result_encoded = urllib.parse.quote(auth_result_json)
        
        redirect_url = f"{settings.frontend_callback_url}?auth_result={auth_result_encoded}"
        
        print(f"🔄 Redirigiendo exitosamente a: {redirect_url[:100]}...")
        return RedirectResponse(url=redirect_url)
        
    except Exception as e:
        print(f"❌ Error inesperado en callback: {str(e)}")
        import traceback
        print(traceback.format_exc())
        
        error_msg = f"Error interno del servidor: {str(e)}"
        redirect_url = f"{settings.frontend_callback_url}?error=server_error&error_description={urllib.parse.quote(error_msg)}"
        print(f"🔄 Redirigiendo con error interno a: {redirect_url}")
        return RedirectResponse(url=redirect_url)

@router.get("/config")
async def get_current_config():
    """
    Endpoint para mostrar la configuración actual (útil para debugging)
    """
    return {
        "environment": settings.ENVIRONMENT,
        "is_development": settings.is_development,
        "is_production": settings.is_production,
        "frontend_url": settings.FRONTEND_URL,
        "frontend_callback": settings.frontend_callback_url,
        "allowed_origins": settings.ALLOWED_ORIGINS,
        "azure_config": {
            "client_id": settings.AZURE_CLIENT_ID[:8] + "...", # Mostrar solo parte por seguridad
            "tenant_id": settings.AZURE_TENANT_ID,
            "authority": settings.AZURE_AUTHORITY,
            "redirect_uri": settings.AZURE_REDIRECT_URI
        }
    }

@router.get("/callback-debug")
async def auth_callback_debug(
    code: str = None,
    error: str = None,
    error_description: str = None,
    state: str = None,
    db: Session = Depends(get_db)
):
    """
    Endpoint de callback que devuelve JSON (útil para debugging)
    """
    try:
        print("🐛 === DEBUG CALLBACK ===")
        print(f"🌍 Environment: {settings.ENVIRONMENT}")
        
        if error:
            return JSONResponse(
                status_code=400,
                content={
                    "status": "error",
                    "error": error,
                    "error_description": error_description,
                    "environment": settings.ENVIRONMENT
                }
            )
        
        if not code:
            return JSONResponse(
                status_code=400,
                content={
                    "status": "error",
                    "error": "missing_code",
                    "message": "No se recibió código de autorización",
                    "environment": settings.ENVIRONMENT
                }
            )
        
        # Autenticar usuario
        auth_result = await authenticate_azure_user(code, db)
        auth_result["environment"] = settings.ENVIRONMENT  # Agregar para debugging
        
        return JSONResponse(content=auth_result)
        
    except Exception as e:
        print(f"❌ Error en debug callback: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": f"Error interno: {str(e)}",
                "environment": settings.ENVIRONMENT
            }
        )

# ... resto de las rutas (login, logout, etc.) sin cambios
# Ejemplo de cómo usarías settings en otras rutas:

@router.post("/login")
async def login_traditional(credentials: dict, db: Session = Depends(get_db)):
    """
    Login tradicional con email/password
    """
    try:
        print(f"🔐 Login tradicional en environment: {settings.ENVIRONMENT}")
        
        email = credentials.get("email")
        password = credentials.get("password")
        
        if not email or not password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email y contraseña son requeridos",
            )
        
        # Buscar el usuario por email
        user = db.query(Usuario).filter(Usuario.email == email).first()
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas",
            )
        
        # Aquí deberías verificar la contraseña
        # if not verify_password(password, user.clave): ...
        
        # Crear token JWT usando configuración centralizada
        jwt_token = create_access_token(data={"sub": email, "user_id": user.usuario})
        
        return {
            "access_token": jwt_token,
            "token_type": "bearer",
            "user_info": {
                "id": user.usuario,
                "email": user.email,
                "nombre": user.nusuario
            },
            "environment": settings.ENVIRONMENT  # Para debugging
        }
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Error en login tradicional: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al iniciar sesión: {str(e)}",
        )