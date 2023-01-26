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
        return f"Kontaktuję się z {self.imie} {self.nazwisko} {self.stanowisko} {self.mail}"

    @property
    def sum(self):
        return sum([len(self.imie), len(self.nazwisko), +1])


class BaseContact(Cards):
    def __init__(self, telefon, **kwargs):
        super().__init__(telefon, **kwargs)
        self.telefon = telefon


class BusinessContact(Cards):
    def __init__(self, telefon1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.telefon1 = telefon1


if __name__ == "__main__":

    Jakub = Cards(
        imie="Jakub",
        nazwisko="Dziurgot",
        firma="Heating",
        stanowisko="Logistyk",
        mail="j.dziurgot@heating.pl",
        telefon=321,
        telefon1=123,
    )
    Jacek = Cards(
        imie="Jacek",
        nazwisko="Nowak",
        firma="ACV",
        stanowisko="Kierownik",
        mail="j.nowak@acv.pl",
        telefon="123",
    )
    Jan = Cards(
        imie="Jan",
        nazwisko="Kowalski",
        firma="AED",
        stanowisko="Prezes",
        mail="j.kowalski@aed.pl",
        telefon="123",
    )
    Pawel = Cards(
        imie="Paweł",
        nazwisko="Adamczyk",
        firma="RAZ",
        stanowisko="Sprzedawca",
        mail="p.adamczyk@raz.pl",
        telefon="123",
    )
    Andrzej = Cards(
        imie="Andrzej",
        nazwisko="Sobota",
        firma="Heat",
        stanowisko="Magazynier",
        mail="a.sobota@heat.pl",
        telefon="123",
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
