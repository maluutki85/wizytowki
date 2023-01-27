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


# funkcja create_contacts

if __name__ == "__main__":

    rodzaj_wizytowki = int(
        input("Jaki rodzaj wizytówki chcesz utworzyć? 1 - prywatna, 2 - firmowa: ")
    )
    ilosc_wizytowki = int(input("Ile wizytówek chcesz utworzyć?"))

    for i in range(ilosc_wizytowki):
        if rodzaj_wizytowki == 1:
            card = f"{fake.first_name()} {fake.last_name()}, {fake.phone_number()}, {fake.email()}"
            print(card)
        elif rodzaj_wizytowki == 2:
            card = f"{fake.first_name()} {fake.last_name()}, {fake.phone_number()}, {fake.email()}, {fake.job()},{fake.company()}"
            print(card)
