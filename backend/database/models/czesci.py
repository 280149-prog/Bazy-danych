from backend.database.connection import db

class Czesc(db.Model):
    __tablename__ = "czesci"

    id_czesci = db.Column(db.Integer, primary_key=True)
    nazwa_czesci = db.Column(db.String(255))
    typ_czesci = db.Column(db.Integer)
    producent = db.Column(db.String(255))
    numer_katalogowy = db.Column(db.String(255))
    cena_katalogowa = db.Column(db.Numeric(10, 2))
    ilosc_dostepna = db.Column(db.Integer)

    wykorzystania = db.relationship("CzescWykorzystana", back_populates="czesc")
    pozycje_zamowien = db.relationship("PozycjaZamowienia", back_populates="czesc")
