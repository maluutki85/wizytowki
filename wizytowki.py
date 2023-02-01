from faker import Faker

fake = Faker("pl_PL")


class Cards:
    def __init__(self, imie, nazwisko, telefon, mail):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.mail = mail

    @property
    def label_length(self):
        return len(self.imie + " " + self.nazwisko)

    def contact(self):
        print(f"Wybieram {self.telefon}" f" i dzwonię do {self.imie} {self.nazwisko}")

    def __str__(self):
        return f"{self.imie}, {self.nazwisko}, {self.mail}"


# klasa BusinessContact


class BusinessContact(Cards):
    def __init__(self, firma, stanowisko, telefon1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.firma = firma
        self.stanowisko = stanowisko
        self.telefon1 = telefon1

    def contact(self):
        print(f"Wybieram {self.telefon1} i dzwonię do {self.imie} {self.nazwisko}")


def create_contacts(rodzaj, ilosc):

    if rodzaj == "prywatna":
        for i in range(ilosc):
            card = f"{fake.first_name()} {fake.last_name()}, {fake.phone_number()}, {fake.email()}"
            print(card)
    elif rodzaj == "firmowa":
        for i in range(ilosc):
            card = f"{fake.first_name()} {fake.last_name()}, {fake.phone_number()}, {fake.email()}, {fake.job()},{fake.company()}"
            print(card)


create_contacts("firmowa", 10)
