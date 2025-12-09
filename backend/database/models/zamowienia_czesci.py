from backend.database.connection import db

class ZamowienieCzesci(db.Model):
    __tablename__ = "zamowienia_czesci"

    id_zamowienia = db.Column(db.Integer, primary_key=True)
    id_skladajacego = db.Column(db.Integer, db.ForeignKey("uzytkownicy.id_uzytkownika"))
    id_zatwierdzajacego = db.Column(db.Integer, db.ForeignKey("uzytkownicy.id_uzytkownika"))

    data_zlozenia = db.Column(db.Date)
    data_zatwierdzenia = db.Column(db.Date)
    data_realizacji = db.Column(db.Date)
    status_zamowienia = db.Column(db.Integer)

    pozycje = db.relationship("PozycjaZamowienia", back_populates="zamowienie")

    skladajacy = db.relationship("Uzytkownik", foreign_keys=[id_skladajacego],
                                 back_populates="zamowienia_skladane")
    zatwierdzajacy = db.relationship("Uzytkownik", foreign_keys=[id_zatwierdzajacego],
                                     back_populates="zamowienia_zatwierdzane")
