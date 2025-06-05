from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import uget_db
from . import schemas, models, oauth, two_factor, utils
from typing import Optional
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["Authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
two_fa = two_factor.TwoFactorAuth()

@router.post("/google-login", response_model=schemas.Token)
async def google_login(google_token: schemas.GoogleLogin, db: Session = Depends(uget_db)):
    user_data = await oauth.verify_google_token(google_token.token)
    
    user = db.query(models.User).filter(models.User.google_id == user_data['sub']).first()
    if not user:
        user = models.User(
            email=user_data['email'],
            full_name=user_data['name'],
            google_id=user_data['sub']
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    access_token = utils.create_access_token(data={"sub": user.email})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "requires_2fa": user.is_2fa_enabled
    }

@router.post("/2fa/setup", response_model=schemas.TwoFactorSetup)
async def setup_2fa(email: str, db: Session = Depends(uget_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    secret = two_fa.generate_secret()
    qr_code = two_fa.generate_qr_code(user.email, secret)
    
    user.two_factor_secret = secret
    db.commit()

    return {"qr_code": qr_code, "secret": secret}

@router.post("/2fa/verify", response_model=schemas.Token)
async def verify_2fa(verify_data: schemas.TwoFactorVerify, db: Session = Depends(uget_db)):
    user = db.query(models.User).filter(models.User.email == verify_data.email).first()
    if not user or not user.two_factor_secret:
        raise HTTPException(status_code=404, detail="User not found or 2FA not setup")

    if not two_fa.verify_code(user.two_factor_secret, verify_data.code):
        raise HTTPException(status_code=400, detail="Invalid 2FA code")

    if not user.is_2fa_enabled:
        user.is_2fa_enabled = True
        db.commit()

    access_token = utils.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer", "requires_2fa": False}