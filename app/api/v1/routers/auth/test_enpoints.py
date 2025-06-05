from fastapi import APIRouter, Depends
from . import jwt_handler, azure_auth

# Este router es solo para pruebas
router = APIRouter()

@router.get("/test")
async def test_route():
    """
    Ruta de prueba simple para verificar que el router está funcionando
    """
    return {"message": "Test route is working!"}

@router.get("/azure-config")
async def get_azure_config():
    """
    Muestra la configuración actual de Azure para diagnóstico
    """
    import os
    return {
        "client_id": os.getenv("AZURE_CLIENT_ID", "No configurado"),
        "tenant_id": os.getenv("AZURE_TENANT_ID", "No configurado"),
        "authority": os.getenv("AZURE_AUTHORITY", "No configurado"),
        "redirect_uri": os.getenv("AZURE_REDIRECT_URI", "No configurado")
    }

@router.get("/generate-test-token")
async def generate_test_token(email: str = "test@example.com"):
    """
    Genera un token de prueba para facilitar las pruebas
    """
    token = jwt_handler.create_access_token(data={"sub": email})
    return {"access_token": token, "token_type": "bearer"}