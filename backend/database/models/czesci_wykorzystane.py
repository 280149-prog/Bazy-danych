from backend.database.connection import db

class CzescWykorzystana(db.Model):
    __tablename__ = "czesci_wykorzystane"

    id_pozycji = db.Column(db.Integer, primary_key=True)
    id_zlecenia = db.Column(db.Integer, db.ForeignKey("zlecenia_naprawy.id_zlecenia"))
    id_czesci = db.Column(db.Integer, db.ForeignKey("czesci.id_czesci"))

    ilosc = db.Column(db.Integer)
    cena_jednostkowa = db.Column(db.Numeric(10, 2))
    data_wykorzystania = db.Column(db.Date)

    zlecenie = db.relationship("ZlecenieNaprawy", back_populates="czesci_wykorzystane")
    czesc = db.relationship("Czesc", back_populates="wykorzystania")
