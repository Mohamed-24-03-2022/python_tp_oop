from S02_TP04_template import get_all_letters
import random


class Human:

    def __init__(self, first_names, last_name, alpha_code2, greetings, majority=18):
        """ Constructeur de la classe Human
        - attribut 'full_name' initialisé en concaténant les éléments de 'first_names' au nom de famille 'last_name'
        - attribut 'nationality' initialisé avec le code de la nationalité 'alpha_code2'
        - attribut 'greetings' initialisé avec le texte de salutation 'greetings'
        - attribut 'age' initialisé à la valeur 0
        - attribut 'majority' initialisé avec 'majority"
        """
        self.full_name = f'{' '.join(first_names)} {last_name}'
        self.nationality = alpha_code2
        self.greetings = greetings
        self.age = 0
        self.majority = majority

    def is_adult(self):
        """
        Retourne 'True' si la majorité est atteinte. 'False' sinon.
        """
        return self.age >= 18

    def get_info(self):
        """
        Retourne la chaine de caractère indiquant toutes les informations
        """
        majority = 'majeur' if self.is_adult() else 'mineur'
        return f'Identité : {self.full_name} - Nationalité : {self.nationality.upper()} - Age : {self.age} ans ({majority})'

    def ageing(self, years=1):
        """
        ajoute les années 'years' à l'age
        """
        self.age += years

    def get_shout(self):
        """
                Retourne la chaine de caractère selon l'âge:
                - jusqu'à an : "Ouin ouin"
                - jusqu'à 2 ans : "Areuh baba gaga"
                - jusqu'à 3 ans : les salutations en mélangeant les lettres
                - à partir de 3 ans : les salutations normales
                """
        salutation = ''
        if (self.age < 1):
            salutation = 'Ouin ouin'
        elif (self.age >= 1 and self.age < 2):
            salutation = 'Areuh baba gaga'
        elif (self.age >= 2 and self.age < 3):
            shuffled_greeting = list(self.greetings)
            random.shuffle(shuffled_greeting)
            salutation = ''.join(shuffled_greeting)
        else:
            salutation = self.greetings

        return salutation


class Cow:

    def __init__(self, nickname, weight, owner):
        """Constructor de la classe Cow
        - attribut 'nickname" initialisé par la chaine de caractère du paramètre 'nickname'
        - attribut 'weight' initialisé par le réel du paramètre 'weight"
        - attribut 'owner' initialisé par un objet Human du paramètre 'owner'
        """
        self.nickname = nickname
        self.weight = weight
        self.owner = owner

    def get_info(self):
        """ Retourne la chaine de caractère indiquant toutes les informations """
        return f'{self.nickname} : cow de {self.weight} Kg. Appartient à {self.owner.full_name}.'

    def gain_weight(self, weight=1):
        """ ajoute le réel 'weight' au poids """
        self.weight += weight

    def lose_weight(self, weight=1):
        """ retire le réel 'weight' au poids """
        self.weight -= weight

    def take_owner(self, owner):
        """ désigne l'objet Human 'owner' comme propriétaire """
        self.owner = owner

    def get_shout(self):
        """ Retourne la chaine de caractère 'Meuh'"""
        return 'Meuh'


class Dog:

    def __init__(self, nickname, owner=None, state=0):
        """Constructor de la classe Dog
        - attribut 'nickname" initialisé par la chaine de caractère du paramètre 'nickname'
        - attribut 'owner' initialisé par un objet Human ou None du paramètre 'owner'
        - attribut 'state' initialisé par la valeur 0 ou 1 du paramètre 'state'"
        """
        self.nickname = nickname
        self.owner = owner
        self.state = state

    def get_info(self):
        """ Retourne la chaine de caractère indiquant toutes les informations """
        state = 'colère' if (self.owner) else 'cool'

        if (self.owner):
            return f"{self.nickname} : dog en {state}. Appartient à {self.owner.full_name}."

        return f"{self.nickname} : dog {state}. N'a pas de propriétaire."

    def swap_state(self):
        """ inverse l'état"""
        if (self.state):
            self.state = 0
        else:
            self.state = 1

    def take_owner(self, owner):
        """ désigne l'objet Human 'owner' comme propriétaire """
        self.owner = owner

    def get_shout(self):
        """ Retourne la chaine de caractère 'Ouah ouah' ou 'Grrr' selon l'état"""
        if (self.state):
            return 'Grrr'
        return 'Ouah ouah'


if __name__ == "__main__":
    random.seed(100)
    farmer = Human(["Marcel", "Robert"], "Duchamps", "fr", "Bonjour", 18)
    farmer.ageing(35)
    assert farmer.get_info(
    ) == 'Identité : Marcel Robert Duchamps - Nationalité : FR - Age : 35 ans (majeur)'
    assert farmer.get_shout() == 'Bonjour'
    farmeress = Human(["Marcela"], "Zpola", "pl", "Dzień dobry", 18)
    farmeress.ageing(36)
    assert farmeress.get_info(
    ) == 'Identité : Marcela Zpola - Nationalité : PL - Age : 36 ans (majeur)'
    assert farmeress.get_shout() == 'Dzień dobry'
    boy = Human(["Marcel",  "junior"], "Duchamps Zpola", "fr", "Bonjour")
    assert boy.get_info() == 'Identité : Marcel junior Duchamps Zpola - Nationalité : FR - Age : 0 ans (mineur)'
    assert boy.get_shout() == 'Ouin ouin'
    boy.ageing()
    assert boy.get_info() == 'Identité : Marcel junior Duchamps Zpola - Nationalité : FR - Age : 1 ans (mineur)'
    assert boy.get_shout() == 'Areuh baba gaga'
    boy.ageing()
    assert boy.get_info() == 'Identité : Marcel junior Duchamps Zpola - Nationalité : FR - Age : 2 ans (mineur)'
    assert boy.get_shout() == 'Bonrujo'
    boy.ageing()
    assert boy.get_info() == 'Identité : Marcel junior Duchamps Zpola - Nationalité : FR - Age : 3 ans (mineur)'
    assert boy.get_shout() == 'Bonjour'
    milk_cow = Cow("Aglaë", 300, farmer)
    milk_cow.gain_weight(30)
    milk_cow.lose_weight(20)
    assert milk_cow.get_info() == 'Aglaë : cow de 310 Kg. Appartient à Marcel Robert Duchamps.'
    milk_cow.take_owner(farmeress)
    assert milk_cow.get_info() == 'Aglaë : cow de 310 Kg. Appartient à Marcela Zpola.'
    assert milk_cow.get_shout() == 'Meuh'
    stray_dog = Dog("Médor", state=0)
    assert stray_dog.get_info() == "Médor : dog cool. N'a pas de propriétaire."
    assert stray_dog.get_shout() == 'Ouah ouah'
    stray_dog.take_owner(boy)
    stray_dog.swap_state()
    assert stray_dog.get_info(
    ) == "Médor : dog en colère. Appartient à Marcel junior Duchamps Zpola."
    assert stray_dog.get_shout() == 'Grrr'
    print("Tests all OK")
