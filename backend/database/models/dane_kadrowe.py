from backend.database.connection import db

class DaneKadrowe(db.Model):
    __tablename__ = "dane_kadrowe"

    id_uzytkownika = db.Column(db.Integer, db.ForeignKey("uzytkownicy.id_uzytkownika"), primary_key=True)
    pesel = db.Column(db.BigInteger)
    nr_konta = db.Column(db.String(26))
    adres_zamieszkania = db.Column(db.String(255))
    stawka_godzinowa = db.Column(db.Numeric(10, 2))
    data_zatrudnienia = db.Column(db.Date)

    uzytkownik = db.relationship("Uzytkownik", back_populates="dane_kadrowe")
