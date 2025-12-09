from backend.database.connection import db
from backend.database.models.uzytkownik import Uzytkownik

# tworzysz aplikację
from backend.app import create_app

app = create_app()

with app.app_context():

    if not Uzytkownik.query.filter_by(login="admin").first():

        admin = Uzytkownik(
            login="admin",
            haslo="admin123",  # później będzie hashing
            rola="admin",
            aktywny=True
        )

        db.session.add(admin)
        db.session.commit()

        print("Admin utworzony!")
    else:
        print("Admin już istnieje")
