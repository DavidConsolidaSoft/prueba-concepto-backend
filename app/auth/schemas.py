from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class GoogleLogin(BaseModel):
    token: str

class Token(BaseModel):
    access_token: str
    token_type: str
    requires_2fa: bool = False

class TwoFactorSetup(BaseModel):
    qr_code: str
    secret: str

class TwoFactorVerify(BaseModel):
    code: str
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    is_2fa_enabled: bool