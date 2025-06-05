import os
from cryptography.fernet import Fernet

import app.core.global_vars as global_vars

# Supongamos que estos son los parámetros de conexión

def encrypt_data(cdata: str):

    # print(cdata)

    # Utilizar la clave generada anteriormente
    key = os.getenv("FERNET_KEY")
    cipher_suite = Fernet(key)

    # Encriptar los parámetros de conexión
    encrypted_db_user = cipher_suite.encrypt(cdata.encode())

    endcoded_data = encrypted_db_user.decode()

    # global_vars.set_ptest(encrypt_data)

    print(f"Encrypted DB User: {endcoded_data}")

    return "saliendo"
    
def dencrypt_data(cdata: str):
    # Utilizar la clave generada anteriormente
    key = os.getenv("FERNET_KEY")
    cipher_suite = Fernet(key)

    encrypt_data = cdata.encode()

    mtest = cipher_suite.decrypt(encrypt_data).decode()
    
    print(f"Encrypted hola mundo: {mtest}")

    return "saliendo"
