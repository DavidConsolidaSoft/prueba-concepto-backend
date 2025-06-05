import os
from fastapi import HTTPException
from google.oauth2 import id_token
from google.auth.transport import requests
from typing import Optional

google_id = os.getenv('GOOGLE_CLIENT_ID')  # Replace with your Google Client ID

async def verify_google_token(token: str) -> dict:
    try:
        idinfo = id_token.verify_oauth2_token(
            token, requests.Request(), google_id
        )
        return idinfo
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid Google token")