import os
from pydantic import AnyHttpUrl, validator, Field
from pydantic_settings import BaseSettings
from typing import List, Optional
from dotenv import load_dotenv

# Cargar archivo .env específico según el entorno
environment = os.getenv("ENVIRONMENT", "development")
print(f"🌍 Loading environment: {environment}")

# Limpiar variables específicas para evitar conflictos
env_vars_to_clear = ['FRONTEND_URL', 'AZURE_REDIRECT_URI']
for var in env_vars_to_clear:
    if var in os.environ:
        del os.environ[var]
        print(f"🧹 Cleared existing: {var}")

if environment == "production":
    result = load_dotenv(".env.production", override=True)
    print(f"📁 Loaded .env.production (success: {result})")
else:
    result = load_dotenv(".env", override=True)
    print(f"📁 Loaded .env (success: {result})")

# Verificar que las variables críticas se cargaron
print(f"🔍 FRONTEND_URL after load: {os.getenv('FRONTEND_URL', 'NOT SET')}")
print(f"🔍 AZURE_REDIRECT_URI after load: {os.getenv('AZURE_REDIRECT_URI', 'NOT SET')}")

class Settings(BaseSettings):
    # Environment
    ENVIRONMENT: str = Field(default="development", env="ENVIRONMENT")
    
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Azure Consolida ERP"
   
    # Database
    DB_DRIVER: str = "ODBC Driver 18 for SQL Server"
    DB_SERVER: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
   
    # Azure AD
    AZURE_CLIENT_ID: str
    AZURE_CLIENT_SECRET: str
    AZURE_TENANT_ID: str
    AZURE_REDIRECT_URI: str = "https://siscal-agent-ai.siscal.one/api/v1/auth/callback"
    AZURE_AUTHORITY: Optional[str] = None
    AZURE_EXTERNAL_TENANT_ID: Optional[str] = None
   
    # Azure OpenAI
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_API_VERSION: str = "2023-05-15"
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT: str = "text-embedding-ada-002"
    AZURE_OPENAI_CHAT_MODEL: str = "gpt-4"
    AZURE_OPENAI_CHAT_DEPLOYMENT: Optional[str] = None
    AZURE_OPENAI_CHAT_API_VERSION: Optional[str] = None
   
    # Redis
    REDIS_HOST: str
    REDIS_PORT: int = 6380
    REDIS_PASSWORD: str
    REDIS_SSL: bool = True
   
    # Security
    FERNET_KEY: str
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    ALGORITHM: str = "HS256"
   
    # Language Service
    AZURE_LANGUAGE_ENDPOINT: Optional[str] = None
    AZURE_LANGUAGE_KEY: Optional[str] = None
    AZURE_LANGUAGE_PROJECT_NAME: Optional[str] = None
    AZURE_LANGUAGE_DEPLOYMENT_NAME: Optional[str] = None
   
    # Frontend Configuration (NEW)
    FRONTEND_URL: Optional[str] = None
    
    # CORS - Configuración automática según entorno
    ALLOWED_ORIGINS: List[str] = []
    PRODUCTION_URL: Optional[AnyHttpUrl] = None
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Configuración automática de Frontend URL
        if not self.FRONTEND_URL:
            frontend_urls = {
                "development": "http://localhost:5000",
                "production": "https://green-ocean-06fb1390f.6.azurestaticapps.net",
                "staging": "https://your-staging-url.azurestaticapps.net"  # Si tienes staging
            }
            self.FRONTEND_URL = frontend_urls.get(self.ENVIRONMENT, frontend_urls["development"])
        
        # Configuración automática de CORS
        if not self.ALLOWED_ORIGINS:
            if self.ENVIRONMENT == "production":
                self.ALLOWED_ORIGINS = [
                    "https://green-ocean-06fb1390f.6.azurestaticapps.net",
                    "https://siscal-agent-ai.siscal.one",
                    # Mantener localhost para testing desde local
                    "http://localhost:5000",
                    "http://localhost:3000"
                ]
            else:
                self.ALLOWED_ORIGINS = [
                    "http://localhost:5000",
                    "http://localhost:3000",
                    "http://localhost:3001",
                    "http://IP_PUBLICA:3000",
                    # Incluir producción para testing
                    "https://green-ocean-06fb1390f.6.azurestaticapps.net"
                ]
        
        # Configurar Azure Authority si no está definida
        if not self.AZURE_AUTHORITY and self.AZURE_TENANT_ID:
            self.AZURE_AUTHORITY = f"https://login.microsoftonline.com/{self.AZURE_TENANT_ID}"
        
        # Log de configuración
        print(f"🔧 === CONFIGURACIÓN CARGADA ===")
        print(f"🌍 Environment: {self.ENVIRONMENT}")
        print(f"🔗 Frontend URL: {self.FRONTEND_URL}")
        print(f"📞 Callback URL: {self.frontend_callback_url}")
        print(f"🔐 Azure Redirect URI: {self.AZURE_REDIRECT_URI}")  # NUEVA LÍNEA
        print(f"🌐 Allowed Origins: {len(self.ALLOWED_ORIGINS)} URLs")
        for origin in self.ALLOWED_ORIGINS:
            print(f"   - {origin}")
        print(f"🔐 Azure Authority: {self.AZURE_AUTHORITY}")
        print(f"===============================")
    
    @property
    def frontend_callback_url(self) -> str:
        """URL del callback del frontend"""
        return f"{self.FRONTEND_URL}/auth/callback"
    
    @property
    def is_development(self) -> bool:
        """Check if running in development"""
        return self.ENVIRONMENT == "development"
    
    @property
    def is_production(self) -> bool:
        """Check if running in production"""
        return self.ENVIRONMENT == "production"
    
    @validator("ALLOWED_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v):
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, list):
            # Convertir AnyHttpUrl a string si es necesario
            return [str(origin) for origin in v]
        return v
    
    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignorar variables no definidas
        case_sensitive = True
    
    @property
    def DATABASE_URI(self):
        from urllib.parse import quote_plus
        password_encoded = quote_plus(self.DB_PASSWORD)
        return (
            f"mssql+pyodbc://{self.DB_USER}:{password_encoded}"
            f"@{self.DB_SERVER}:1433/{self.DB_NAME}?"
            f"driver={self.DB_DRIVER}&Encrypt=yes&TrustServerCertificate=no"
        )

# Instancia global de configuración
settings = Settings()

# Función helper para obtener configuración
def get_settings() -> Settings:
    return settings