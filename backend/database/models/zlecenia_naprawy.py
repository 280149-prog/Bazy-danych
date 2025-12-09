from backend.database.connection import db

class ZlecenieNaprawy(db.Model):
    __tablename__ = "zlecenia_naprawy"

    id_zlecenia = db.Column(db.Integer, primary_key=True)
    id_klienta = db.Column(db.Integer, db.ForeignKey("klienci.id_klienta"))
    id_pracownika = db.Column(db.Integer, db.ForeignKey("uzytkownicy.id_uzytkownika"))

    typ_sprzetu = db.Column(db.Integer)
    data_rozpoczecia = db.Column(db.Date)
    data_zakonczenia = db.Column(db.Date)
    opis_usterki = db.Column(db.String(2000))
    status_zlecenia = db.Column(db.Integer)

    koszt_robocizny = db.Column(db.Numeric(10, 2))
    koszt_czesci = db.Column(db.Numeric(10, 2))
    koszt_calkowity = db.Column(db.Numeric(10, 2))

    marka_sprzetu = db.Column(db.String(255))
    model_sprzetu = db.Column(db.String(255))
    numer_seryjny = db.Column(db.String(255))
    diagnoza = db.Column(db.String(255))
    wykonane_czynnosci = db.Column(db.String(255))

    klient = db.relationship("Klient", back_populates="zlecenia")
    pracownik = db.relationship("Uzytkownik", back_populates="zlecenia")
    czesci_wykorzystane = db.relationship("CzescWykorzystana", back_populates="zlecenie")
