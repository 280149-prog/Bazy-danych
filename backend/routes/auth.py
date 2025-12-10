from flask import Blueprint, request, jsonify, g
from backend.database.models.uzytkownik import Uzytkownik
from backend.utils.jwt import create_token
from backend.utils.auth_middleware import token_required
from backend.utils.auth_middleware import role_required

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json or {}

    login = data.get("login")
    password = data.get("password")

    if not login or not password:
        return jsonify({"error": "Brak loginu lub hasła"}), 400

    user = Uzytkownik.query.filter_by(login=login).first()

    if not user:
        return jsonify({"error": "Nieprawidłowy login"}), 401

    if not user.aktywny:
        return jsonify({"error": "Konto jest dezaktywowane"}), 403

    if not user.check_password(password):
        return jsonify({"error": "Nieprawidłowe hasło"}), 401

    token = create_token(user.id_uzytkownika, user.rola)

    return jsonify({
        "message": "Zalogowano",
        "token": token,
        "rola": user.rola,
        "id": user.id_uzytkownika
    })



@auth_bp.route("/me", methods=["GET"])
@token_required
def me():
    user = Uzytkownik.query.get(g.user_id)

    if not user:
        return jsonify({"error": "Użytkownik nie istnieje"}), 404

    return jsonify({
        "id": user.id_uzytkownika,
        "login": user.login,
        "rola": user.rola,
        "aktywny": user.aktywny
    })

@auth_bp.route("/check-admin", methods=["GET"])
@token_required
@role_required("admin")
def check_admin():
    return jsonify({"message": "OK, jesteś adminem"})

@auth_bp.route("/dev-login", methods=["GET"])
def dev_login():
    from backend.database.models.uzytkownik import Uzytkownik
    from backend.utils.jwt import create_token

    user = Uzytkownik.query.filter_by(login="admin").first()

    if not user:
        return jsonify({"error": "Brak użytkownika admin"}), 404

    token = create_token(user.id_uzytkownika, user.rola)

    return jsonify({
        "message": "Token dev wygenerowany",
        "token": token
    })

