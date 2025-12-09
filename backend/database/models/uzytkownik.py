from backend.database.connection import db
from datetime import datetime

class Uzytkownik(db.Model):
    __tablename__ = "uzytkownicy"

    id_uzytkownika = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    haslo = db.Column(db.String(255), nullable=False)
    rola = db.Column(db.Enum("admin", "kierownik", "pracownik"), nullable=False)
    aktywny = db.Column(db.Boolean, default=True)
    data_utworzenia = db.Column(db.DateTime, default=datetime.now)

    dane_kadrowe = db.relationship("DaneKadrowe", back_populates="uzytkownik", uselist=False)
    zlecenia = db.relationship("ZlecenieNaprawy", back_populates="pracownik")

    # POPRAWNE relacje
    zamowienia_skladane = db.relationship(
        "ZamowienieCzesci",
        foreign_keys="ZamowienieCzesci.id_skladajacego",
        back_populates="skladajacy"
    )

    zamowienia_zatwierdzane = db.relationship(
        "ZamowienieCzesci",
        foreign_keys="ZamowienieCzesci.id_zatwierdzajacego",
        back_populates="zatwierdzajacy"
    )
