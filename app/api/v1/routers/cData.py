from app.core import encrypt
from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/encrypt_data/")
def encrypt_data(cString: str = Query(...)):
    encrypted_data = encrypt.encrypt_data(cString)

    return encrypted_data

# @router.get("/dencrypt_data/")
# def dencrypt_data(cString: str = Query(...)):
#     encrypted_data = encrypt.dencrypt_data(cString)

#     return encrypted_data