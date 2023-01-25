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
        print(
            f"Kontaktuję się z {self.imie} {self.nazwisko} {self.stanowisko} {self.mail}"
        )

    @property
    def sum(self):
        print(len(self.imie + " " + self.nazwisko))


class BaseContact(Cards):
    def __init__(self, imie, nazwisko, telefon, mail):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.mail = mail

    def contact(self):
        print(f"Wybieram numer {self.telefon} i dzownię do {self.imie}{self.nazwisko}")

    @property
    def sum(self):
        print(len(self.imie + " " + self.nazwisko))


class BusinessContact(Cards):
    def __init__(self, stanowisko, firma, telefon1):
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon1 = telefon1

    def contact(self):
        print(f"Wybieram numer {self.telefon1} i dzownię do {self.imie}{self.nazwisko}")

    @property
    def sum(self):
        print(len(self.imie + " " + self.nazwisko))


if __name__ == "__main__":

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
    Pawel = Cards(
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
    cards = [Jakub, Jacek, Jan, Pawel, Andrzej]

    for obj in cards:
        print(obj)
    print("---")

    for card in sorted(cards, key=lambda card: card.imie):
        print(card)
    print("---")
    for card in sorted(cards, key=lambda card: card.nazwisko):
        print(card)
    print("---")
    for card in sorted(cards, key=lambda card: card.mail):
        print(card)
    print("---")

    Jakub.contact()
    Jacek.contact()
    Jan.contact()
    Pawel.contact()
    Andrzej.contact()

    Jakub.sum
    Jacek.sum
    Jan.sum
    Pawel.sum
    Andrzej.sum