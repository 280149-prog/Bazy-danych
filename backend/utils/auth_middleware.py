from functools import wraps
from flask import request, jsonify, g
import jwt
from config import Config


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", None)

        if not auth_header:
            return jsonify({"error": "Brak tokena"}), 401

        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Nieprawidłowy format tokena"}), 401

        token = auth_header.split(" ")[1]

        try:
            decoded = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token wygasł"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Nieprawidłowy token"}), 401

        # zapisujemy dane użytkownika do obiektu requestu
        g.user_id = decoded["user_id"]
        g.user_role = decoded["role"]

        return f(*args, **kwargs)
    return wrapper


def role_required(*roles):
    """
    Użycie:
    @token_required
    @role_required("admin", "kierownik")
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):

            # upewniamy się, że token_required ustawił dane w g
            if not hasattr(g, "user_role"):
                return jsonify({"error": "Brak informacji o roli użytkownika"}), 403

            # sprawdzamy rolę
            if g.user_role not in roles:
                return jsonify({"error": "Brak uprawnień"}), 403

            return f(*args, **kwargs)
        return wrapper
    return decorator
