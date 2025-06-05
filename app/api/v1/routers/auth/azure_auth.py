# app/api/v1/routers/auth/azure_auth.py - Versión corregida con configuración centralizada
from typing import Optional, Dict, Any
import os
import msal
import requests
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

# Importaciones corregidas según tu estructura
from app.models.all_models import Usuario as User
from .jwt_handler import create_access_token

# Importar configuración centralizada
try:
    from app.core.config import settings
    print(f"✅ Usando configuración centralizada desde settings")
    
    CLIENT_ID = settings.AZURE_CLIENT_ID
    CLIENT_SECRET = settings.AZURE_CLIENT_SECRET
    TENANT_ID = settings.AZURE_TENANT_ID
    AUTHORITY = settings.AZURE_AUTHORITY
    # AQUÍ ESTÁ EL CAMBIO CLAVE: usar configuración centralizada
    REDIRECT_URI = settings.AZURE_REDIRECT_URI
    
except ImportError:
    print("⚠️ No se pudo importar settings, usando variables de entorno directamente")
    
    CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
    CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
    TENANT_ID = os.getenv("AZURE_TENANT_ID")
    AUTHORITY = os.getenv("AZURE_AUTHORITY", f"https://login.microsoftonline.com/{TENANT_ID}")
    REDIRECT_URI = os.getenv("AZURE_REDIRECT_URI")

print(f"=== CONFIGURACIÓN AZURE (azure_auth.py) ===")
print(f"CLIENT_ID: {CLIENT_ID}")
print(f"TENANT_ID: {TENANT_ID}")
print(f"AUTHORITY: {AUTHORITY}")
print(f"REDIRECT_URI: {REDIRECT_URI}")
print(f"===============================")

if not all([CLIENT_ID, CLIENT_SECRET, TENANT_ID, REDIRECT_URI]):
    print("⚠️  ADVERTENCIA: Faltan variables de entorno de Azure")
    missing = []
    if not CLIENT_ID: missing.append("AZURE_CLIENT_ID")
    if not CLIENT_SECRET: missing.append("AZURE_CLIENT_SECRET")
    if not TENANT_ID: missing.append("AZURE_TENANT_ID")
    if not REDIRECT_URI: missing.append("AZURE_REDIRECT_URI")
    print(f"Variables faltantes: {', '.join(missing)}")

# Cliente MSAL
app = msal.ConfidentialClientApplication(
    client_id=CLIENT_ID,
    client_credential=CLIENT_SECRET,
    authority=AUTHORITY
) if all([CLIENT_ID, CLIENT_SECRET, AUTHORITY]) else None

def get_auth_url() -> Dict[str, str]:
    """
    Genera la URL para iniciar el flujo de autorización de Microsoft Entra ID
    """
    if not app:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Configuración de Azure incompleta"
        )
        
    try:
        print(f"🔗 Generando URL de auth con redirect_uri: {REDIRECT_URI}")
        
        # Scopes básicos
        scopes = ["User.Read"]
        
        auth_url = app.get_authorization_request_url(
            scopes=scopes,
            redirect_uri=REDIRECT_URI,
            state="auth-state-token"
        )
        
        print(f"✅ URL de auth generada exitosamente")
        print(f"🔗 URL: {auth_url[:100]}...")
        return {"auth_url": auth_url}
        
    except Exception as e:
        print(f"❌ Error generando auth URL: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al generar URL de autenticación: {str(e)}"
        )

async def get_token_from_code(code: str) -> Dict[str, Any]:
    """
    Intercambia el código de autorización por un token de acceso
    """
    if not app:
        return {
            "error": True,
            "error_message": "Configuración de Azure incompleta"
        }
        
    try:
        print(f"🔄 Intercambiando código: {code[:10]}...")
        print(f"🔗 Usando redirect_uri: {REDIRECT_URI}")
        
        result = app.acquire_token_by_authorization_code(
            code=code,
            scopes=["User.Read"],
            redirect_uri=REDIRECT_URI
        )
        
        print(f"📦 Resultado de MSAL: {list(result.keys())}")
        
        if "error" in result:
            error_desc = result.get("error_description", "Error desconocido")
            print(f"❌ Error de MSAL: {result.get('error')} - {error_desc}")
            return {
                "error": True,
                "error_type": result.get("error"),
                "error_message": error_desc,
                "details": result
            }
        
        if "access_token" not in result:
            print("❌ No se recibió access_token en la respuesta")
            return {
                "error": True,
                "error_message": "No se recibió token de acceso",
                "details": result
            }
        
        print("✅ Token obtenido exitosamente")
        return result
        
    except Exception as e:
        print(f"❌ Excepción en get_token_from_code: {str(e)}")
        import traceback
        print(traceback.format_exc())
        
        return {
            "error": True,
            "error_message": str(e),
            "error_type": type(e).__name__
        }

async def get_user_info(token: str) -> Dict[str, Any]:
    """
    Obtiene la información del usuario desde Microsoft Graph
    """
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get("https://graph.microsoft.com/v1.0/me", headers=headers)
        
        print(f"📊 Graph API response status: {response.status_code}")
        
        if response.status_code != 200:
            print(f"❌ Error en Graph API: {response.text}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No se pudo obtener información del usuario de Microsoft Graph"
            )
        
        user_info = response.json()
        user_email = user_info.get('mail', user_info.get('userPrincipalName'))
        print(f"👤 Info de usuario obtenida: {user_email}")
        return user_info
        
    except requests.RequestException as e:
        print(f"❌ Error en request a Graph API: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Error comunicándose con Microsoft Graph API"
        )

async def authenticate_azure_user(code: str, db: Session) -> Dict[str, Any]:
    """
    Flujo completo de autenticación: código -> token -> usuario -> JWT
    """
    try:
        print("🚀 === INICIANDO AUTENTICACIÓN AZURE ===")
        print(f"📝 Código recibido: {code[:15]}...")
        print(f"🔗 Usando REDIRECT_URI: {REDIRECT_URI}")
        
        # Paso 1: Intercambiar código por token
        print("🔄 Paso 1: Intercambiando código por token...")
        token_result = await get_token_from_code(code)
        
        if token_result.get("error"):
            print(f"❌ Error obteniendo token: {token_result.get('error_message')}")
            return {
                "status": "error",
                "message": f"Error obteniendo token: {token_result.get('error_message')}",
                "details": token_result
            }
        
        access_token = token_result.get("access_token")
        if not access_token:
            print("❌ No se obtuvo access_token")
            return {
                "status": "error",
                "message": "No se pudo obtener el token de acceso",
                "details": token_result
            }
        
        print(f"✅ Token obtenido: {access_token[:20]}...")
        
        # Paso 2: Obtener información del usuario
        print("👤 Paso 2: Obteniendo información del usuario...")
        try:
            # Primero intentamos usar los claims del ID token si están disponibles
            id_token_claims = token_result.get("id_token_claims", {})
            if id_token_claims:
                print("📋 Usando claims del ID token")
                user_info = id_token_claims
            else:
                print("🌐 Obteniendo info del usuario desde Graph API")
                user_info = await get_user_info(access_token)
                
        except Exception as graph_error:
            print(f"❌ Error obteniendo info del usuario: {str(graph_error)}")
            return {
                "status": "error",
                "message": f"Error obteniendo información del usuario: {str(graph_error)}"
            }
        
        # Paso 3: Extraer email
        print("📧 Paso 3: Extrayendo email del usuario...")
        email = (
            user_info.get("mail") or 
            user_info.get("email") or 
            user_info.get("userPrincipalName") or
            user_info.get("preferred_username")
        )
        
        if not email:
            print("❌ No se pudo extraer email del usuario")
            print(f"📋 User info disponible: {list(user_info.keys())}")
            return {
                "status": "error",
                "message": "No se pudo obtener el email del usuario"
            }
        
        print(f"✅ Email del usuario: {email}")
        
        # Paso 4: Buscar/crear usuario en BD
        print("🗃️ Paso 4: Buscando/creando usuario en BD...")
        user_id = None
        user_name = None
        
        try:
            user = db.query(User).filter(
                (User.email == email) | (User.correo == email)
            ).first()
            
            if not user:
                print(f"➕ Creando nuevo usuario: {email}")
                display_name = user_info.get("displayName", user_info.get("name", email.split("@")[0]))
                user = User(
                    email=email,
                    correo=email,
                    nusuario=display_name,
                    activo=True,
                    clave=None  # Sin contraseña para auth Azure
                )
                db.add(user)
                db.commit()
                db.refresh(user)
                user_id = user.usuario
                user_name = user.nusuario
                print(f"✅ Usuario creado con ID: {user_id}")
            else:
                user_id = user.usuario
                user_name = user.nusuario
                print(f"✅ Usuario existente encontrado: ID {user_id}")
                
        except Exception as db_error:
            print(f"❌ Error de BD: {str(db_error)}")
            import traceback
            print(traceback.format_exc())
            
            # Continuar sin persistir en BD
            user_id = 0
            user_name = user_info.get("displayName", user_info.get("name", email))
            print("⚠️ Continuando con usuario temporal")
        
        # Paso 5: Generar JWT
        print("🔐 Paso 5: Generando JWT...")
        jwt_token = create_access_token(data={"sub": email, "user_id": user_id})
        
        result = {
            "status": "success",
            "access_token": jwt_token,
            "token_type": "bearer",
            "user_info": {
                "id": user_id,
                "email": email,
                "nombre": user_name
            }
        }
        
        print("🎉 === AUTENTICACIÓN COMPLETADA EXITOSAMENTE ===")
        return result
        
    except Exception as e:
        print(f"❌ Error inesperado en authenticate_azure_user: {str(e)}")
        import traceback
        print(traceback.format_exc())
        
        return {
            "status": "error",
            "message": f"Error interno durante la autenticación: {str(e)}"
        }