from backend.database.connection import db

class PozycjaZamowienia(db.Model):
    __tablename__ = "pozycje_zamowienia"

    id_pozycji = db.Column(db.Integer, primary_key=True)
    id_zamowienia = db.Column(db.Integer, db.ForeignKey("zamowienia_czesci.id_zamowienia"))
    id_czesci = db.Column(db.Integer, db.ForeignKey("czesci.id_czesci"))

    ilosc = db.Column(db.Integer)
    cena_jednostkowa = db.Column(db.Numeric(10, 2))

    zamowienie = db.relationship("ZamowienieCzesci", back_populates="pozycje")
    czesc = db.relationship("Czesc", back_populates="pozycje_zamowien")