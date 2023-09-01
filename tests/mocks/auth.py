from datetime import datetime, timedelta

from jose import jwt

from app.config import settings

INVALID_TOKEN = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZ"
    "SI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36PO"
    "k6yJV_adQssw5c"
)


def generate_expire_token():
    expired = datetime.utcnow() + timedelta(minutes=-15)
    to_encode = {"sub": "testuser", "exp": expired}
    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.algorithm
    )
    return encoded_jwt
