from flask import Blueprint, request, jsonify, g
from backend.database.connection import db
from backend.database.models.uzytkownik import Uzytkownik
from backend.utils.auth_middleware import token_required, role_required

users_bp = Blueprint("users", __name__)


# ===========================
#   LISTA UŻYTKOWNIKÓW (ADMIN)
# ===========================
@users_bp.route("/", methods=["GET"])
@token_required
@role_required("admin")
def list_users():
    users = Uzytkownik.query.all()

    return jsonify([
        {
            "id": u.id_uzytkownika,
            "login": u.login,
            "rola": u.rola,
            "aktywny": u.aktywny
        }
        for u in users
    ])


# ===========================
#   POBRANIE KONKRETNEGO UŻYTKOWNIKA
# ===========================
@users_bp.route("/<int:user_id>", methods=["GET"])
@token_required
@role_required("admin")
def get_user(user_id):
    user = Uzytkownik.query.get(user_id)

    if not user:
        return jsonify({"error": "Użytkownik nie istnieje"}), 404

    return jsonify({
        "id": user.id_uzytkownika,
        "login": user.login,
        "rola": user.rola,
        "aktywny": user.aktywny
    })


# ===========================
#   DODAWANIE UŻYTKOWNIKA
# ===========================
@users_bp.route("/", methods=["POST"])
@token_required
@role_required("admin")
def add_user():
    data = request.json or {}

    login = data.get("login")
    password = data.get("password")
    rola = data.get("rola", "pracownik")

    if not login or not password:
        return jsonify({"error": "Brak loginu lub hasła"}), 400

    if Uzytkownik.query.filter_by(login=login).first():
        return jsonify({"error": "Login jest już zajęty"}), 400

    user = Uzytkownik(
        login=login,
        rola=rola,
        aktywny=True
    )
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Użytkownik dodany", "id": user.id_uzytkownika})


# ===========================
#   EDYCJA UŻYTKOWNIKA
# ===========================
@users_bp.route("/<int:user_id>", methods=["PUT"])
@token_required
@role_required("admin")
def update_user(user_id):
    user = Uzytkownik.query.get(user_id)

    if not user:
        return jsonify({"error": "Użytkownik nie istnieje"}), 404

    data = request.json or {}

    user.login = data.get("login", user.login)
    user.rola = data.get("rola", user.rola)

    db.session.commit()

    return jsonify({"message": "Dane użytkownika zmienione"})


# ===========================
#   DEZAKTYWACJA UŻYTKOWNIKA
# ===========================
@users_bp.route("/<int:user_id>/deactivate", methods=["PATCH"])
@token_required
@role_required("admin")
def deactivate_user(user_id):
    user = Uzytkownik.query.get(user_id)

    if not user:
        return jsonify({"error": "Użytkownik nie istnieje"}), 404

    user.aktywny = False
    db.session.commit()

    return jsonify({"message": "Użytkownik dezaktywowany"})


# ===========================
#   RESET HASŁA
# ===========================
@users_bp.route("/<int:user_id>/reset-password", methods=["POST"])
@token_required
@role_required("admin")
def reset_password(user_id):
    user = Uzytkownik.query.get(user_id)

    if not user:
        return jsonify({"error": "Użytkownik nie istnieje"}), 404

    new_pass = request.json.get("new_password")

    if not new_pass:
        return jsonify({"error": "Brak nowego hasła"}), 400

    user.set_password(new_pass)
    db.session.commit()

    return jsonify({"message": "Hasło zmienione"})
