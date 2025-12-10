import jwt
from datetime import datetime, timedelta
from backend.config import Config


def create_token(user_id, role):
    payload = {
        "user_id": user_id,
        "role": role,  # Uwaga: "role", nie "rola"
        "exp": datetime.utcnow() + timedelta(hours=12),
    }
    return jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm="HS256")


def verify_token(token):
    try:
        return jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
