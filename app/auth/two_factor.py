import pyotp
from fastapi import HTTPException
import qrcode
import base64
from io import BytesIO

class TwoFactorAuth:
    def __init__(self):
        self.totp = pyotp.TOTP(pyotp.random_base32())

    def generate_secret(self) -> str:
        return self.totp.secret

    def generate_qr_code(self, email: str, secret: str) -> str:
        totp = pyotp.TOTP(secret)
        provisioning_uri = totp.provisioning_uri(
            email,
            issuer_name="ConsolidaERP"
        )

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(provisioning_uri)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        buffered = BytesIO()
        img.save(buffered)
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return f"data:image/png;base64,{img_str}"

    def verify_code(self, secret: str, code: str) -> bool:
        totp = pyotp.TOTP(secret)
        return totp.verify(code)