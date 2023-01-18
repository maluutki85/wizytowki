class Cards:
    def __init__(self, imie, nazwisko, firma, stanowisko, mail):
        self.imie = imie
        self.nazwisko = nazwisko
        self.firma = firma
        self.stanowisko = stanowisko
        self.mail = mail

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.mail}"

    def contact(self):
        return f"Kontaktuję się z {self.imie} {self.nazwisko} {self.mail}"


Jakub = Cards(
    imie="Jakub",
    nazwisko="Dziurgot",
    firma="Heating",
    stanowisko="Logistyk",
    mail="j.dziurgot@heating.pl",
)
Jacek = Cards(
    imie="Jacek",
    nazwisko="Nowak",
    firma="ACV",
    stanowisko="Kierownik",
    mail="j.nowak@acv.pl",
)
Jan = Cards(
    imie="Jan",
    nazwisko="Kowalski",
    firma="AED",
    stanowisko="Prezes",
    mail="j.kowalski@aed.pl",
)
Paweł = Cards(
    imie="Paweł",
    nazwisko="Adamczyk",
    firma="RAZ",
    stanowisko="Sprzedawca",
    mail="p.adamczyk@raz.pl",
)
Andrzej = Cards(
    imie="Andrzej",
    nazwisko="Sobota",
    firma="Heat",
    stanowisko="Magazynier",
    mail="a.sobota@heat.pl",
)
