from faker import Faker

fake = Faker("pl_PL")

class BaseContact:
    def __init__(self, imie, nazwisko, telefon, mail):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.mail = mail

    @property
    def label_lenght(self): 
        return len(self.imie + " " + self.nazwisko)
    
    def contact(self):
        return f"Wybieram {self.telefon} i dzwonię do {self.imie} {self.nazwisko}"

    def __repr__(self):
        return f'{self.imie} {self.nazwisko}, {self.telefon}, {self.mail}'
class BusinessContact(BaseContact):
    def __init__(self, stanowisko, firma, telefon1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon1 = telefon1


    def contact(self):
        return f"Wybieram {self.telefon1} i dzwonię do {self.imie} {self.nazwisko}"
    
    def __repr__(self):
        return f'{self.imie} {self.nazwisko}, {self.telefon}, {self.mail}, {self.stanowisko}, {self.firma}, {self.telefon1}'

def create_contacts(rodzaj, ilosc):
    my_list = []
    if rodzaj == "prywatna":
        for i in range (ilosc):
            my_list.append(BaseContact(imie = fake.first_name(), nazwisko = fake.last_name (), telefon = fake.phone_number(), mail=fake.email()))
    elif rodzaj == "firmowa":
        for i in range (ilosc):
            my_list.append(BusinessContact(imie = fake.first_name(), nazwisko = fake.last_name(), telefon = fake.phone_number(), mail=fake.email(), stanowisko=fake.job(), firma = fake.company(), telefon1 = fake.phone_number()))
    return my_list

if __name__ == "__main__":

    my_list= create_contacts("firmowa",5)
    print(my_list)
