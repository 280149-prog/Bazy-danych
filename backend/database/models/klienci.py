from backend.database.connection import db

class Klient(db.Model):
    __tablename__ = "klienci"

    id_klienta = db.Column(db.Integer, primary_key=True)
    imie = db.Column(db.String(255))
    nazwisko = db.Column(db.String(255))
    email = db.Column(db.String(255))
    nr_telefonu = db.Column(db.String(20))
    adres = db.Column(db.String(255))
    data_rejestracji = db.Column(db.Date)

    zlecenia = db.relationship("ZlecenieNaprawy", back_populates="klient")
