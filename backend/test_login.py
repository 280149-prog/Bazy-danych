from backend.database.connection import db
from backend.database.models.uzytkownik import Uzytkownik
from backend.app import app

with app.app_context():
    users = Uzytkownik.query.all()
    print("Użytkownicy:", users)

    admin = Uzytkownik.query.filter_by(login="admin").first()
    print("Admin:", admin)
    print("Hash hasła admina:", admin.haslo)
