from flask import Flask
from config import Config
from backend.database.connection import db
from backend.routes.auth import auth_bp
from backend.database.models.uzytkownik import Uzytkownik
from backend.database.models.dane_kadrowe import DaneKadrowe
from backend.database.models.klienci import Klient
from backend.database.models.zlecenia_naprawy import ZlecenieNaprawy
from backend.database.models.czesci import Czesc
from backend.database.models.czesci_wykorzystane import CzescWykorzystana
from backend.database.models.zamowienia_czesci import ZamowienieCzesci
from backend.database.models.pozycje_zamowienia import PozycjaZamowienia


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Rejestracja blueprintów
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
