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


class BusinessContact(Cards):
    def __init__(self, firma, stanowisko, telefon1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.firma = firma
        self.stanowisko = stanowisko
        self.telefon1 = telefon1

    @property
    def label_length(self):
        return len(self.imie + " " + self.nazwisko)

    def contact(self):
        print(f"Wybieram {self.telefon1}" f" i dzwonię do {self.imie} {self.nazwisko}")
