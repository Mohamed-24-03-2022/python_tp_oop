from S02_TP04_template import get_all_letters
import random


class Farm:
    def __init__(self, name, owner):
        self.__name = name
        self.__inhabitants = {owner}

    def get_name(self):
        return self.__name

    def get_inhabitants(self):
        return self.__inhabitants

    def populate(self, inhabitant):
        self.__inhabitants.add(inhabitant)

    def get_talk(self):
        num_of_inhabitants = len(self.__inhabitants)

        talk = f'Les {num_of_inhabitants} habitants de la ferme {
            self.__name} se retrouvent :\n'

        for inhabitant in self.__inhabitants:
            if (hasattr(inhabitant, 'get_full_name')):
                name = inhabitant.get_full_name()
            else:
                name = inhabitant.get_nickname()
            talk += name + ' : ' + inhabitant.get_shout() + '\n'

        return talk


class Human:
    __humans_count = 0
    __nationality_greetings = {
    }

    def statique():
        return 'method statique'

    def get_humans_count(cls):
        return cls.__humans_count

    def add_nationality_greetings(cls, nationality, greeting):
        cls.__nationality_greetings[nationality] = greeting

    def get_nationality_greetings(cls):
        return cls.__nationality_greetings

    def __init__(self, first_names, last_name, alpha_code2, greetings, majority=18):
        """ Constructeur de la classe Human
        - attribut 'full_name' initialisé en concaténant les éléments de 'first_names' au nom de famille 'last_name'
        - attribut 'nationality' initialisé avec le code de la nationalité 'alpha_code2'
        - attribut 'greetings' initialisé avec le texte de salutation 'greetings'
        - attribut 'age' initialisé à la valeur 0
        - attribut 'majority' initialisé avec 'majority"
        """
        self.__full_name = f'{' '.join(first_names)} {last_name}'
        self.__nationality = alpha_code2
        self.__greetings = greetings
        self.__age = 0
        self.__majority = majority

        Human.__humans_count += 1

    def get_full_name(self):
        return self.__full_name

    def get_nationality(self):
        return self.__nationality

    def get_greetings(self):
        return self.__greetings

    def get_age(self):
        return self.__age

    def get_majority(self):
        return self.__majority

    def is_adult(self):
        """
        Retourne 'True' si la majorité est atteinte. 'False' sinon.
        """
        return self.__age >= 18

    def get_info(self):
        """
        Retourne la chaine de caractère indiquant toutes les informations
        """
        majority = 'majeur' if self.is_adult() else 'mineur'
        return f'Identité : {self.__full_name} - Nationalité : {self.__nationality.upper()} - Age : {self.__age} ans ({majority})'

    def ageing(self, years=1):
        """
        ajoute les années 'years' à l'age
        """
        self.__age += years

    def get_shout(self):
        """
                Retourne la chaine de caractère selon l'âge:
                - jusqu'à an : "Ouin ouin"
                - jusqu'à 2 ans : "Areuh baba gaga"
                - jusqu'à 3 ans : les salutations en mélangeant les lettres
                - à partir de 3 ans : les salutations normales
                """
        salutation = ''
        if (self.__age < 1):
            salutation = 'Ouin ouin'
        elif (self.__age >= 1 and self.__age < 2):
            salutation = 'Areuh baba gaga'
        elif (self.__age >= 2 and self.__age < 3):
            shuffled_greeting = list(self.__greetings)
            random.shuffle(shuffled_greeting)
            salutation = ''.join(shuffled_greeting)
        else:
            salutation = self.__greetings

        return salutation


class Cow:
    def __init__(self, nickname, weight, owner):
        """Constructor de la classe Cow
        - attribut 'nickname" initialisé par la chaine de caractère du paramètre 'nickname'
        - attribut 'weight' initialisé par le réel du paramètre 'weight"
        - attribut 'owner' initialisé par un objet Human du paramètre 'owner'
        """
        self.__nickname = nickname
        self.__weight = weight
        self.__owner = owner

    def get_nickname(self):
        return self.__nickname

    def set_nickname(self, nickname):
        self.__nickname = nickname

    def get_weight(self):
        return self.__weight

    def get_owner(self):
        return self.__owner

    def get_info(self):
        """ Retourne la chaine de caractère indiquant toutes les informations """
        return f'{self.__nickname} : cow de {self.__weight} Kg. Appartient à {self.__owner.get_full_name()}.'

    def gain_weight(self, weight=1):
        """ ajoute le réel 'weight' au poids """
        self.__weight += weight

    def lose_weight(self, weight=1):
        """ retire le réel 'weight' au poids """
        self.__weight -= weight

    def take_owner(self, owner):
        """ désigne l'objet Human 'owner' comme propriétaire """
        self.__owner = owner

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
        self.__nickname = nickname
        self.__owner = owner

        if state not in (0, 1):
            raise ValueError('State must be 0 or 1')
        self.__state = state

    def get_nickname(self):
        return self.__nickname

    def set_nickname(self, nickname):
        self.__nickname = nickname

    def get_owner(self):
        return self.__owner

    def get_state(self):
        return self.__state

    def get_info(self):
        """ Retourne la chaine de caractère indiquant toutes les informations """
        state = 'colère' if (self.__state) else 'cool'

        if (self.__state):
            return f"{self.__nickname} : dog en {state}. Appartient à {self.__owner.get_full_name()}."

        return f"{self.__nickname} : dog {state}. N'a pas de propriétaire."

    def swap_state(self):
        """ inverse l'état"""
        if (self.__state):
            self.__state = 0
        else:
            self.__state = 1

    def take_owner(self, owner):
        """ désigne l'objet Human 'owner' comme propriétaire """
        self.__owner = owner

    def get_shout(self):
        """ Retourne la chaine de caractère 'Ouah ouah' ou 'Grrr' selon l'état"""
        if (self.__state):
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

    #!_____ cour: ___________________________________________________________________
    # attribute d'instance => can be private or public

    # attribute de class
    # Human.__humans_count
    # boy.__humans_count

    # method d'instances
    assert boy.get_info() == 'Identité : Marcel junior Duchamps Zpola - Nationalité : FR - Age : 3 ans (mineur)'
    assert boy.get_full_name() == 'Marcel junior Duchamps Zpola'

    # method de class
    assert boy.get_humans_count() == 3

    # method statique
    assert Human.statique() == 'method statique'

    # accesseur ecriture / lecture => setter / getter
    # * _______________________________________________________________________________

    try:
        Dog("Spike", state=3)
        assert False
    except ValueError as e:
        assert str(e) == 'State must be 0 or 1'

    farm = Farm("Fermarcel", farmer)
    farm.populate(farmeress)
    farm.populate(boy)
    farm.populate(milk_cow)
    farm.populate(stray_dog)

    # test farm.get_talk()
    # rstrip() method to remvoe all whitespace
    expected_string_output = 'Les 5 habitants de la ferme Fermarcel se retrouvent :\nMarcel junior Duchamps Zpola : Bonjour\nMarcela Zpola : Dzień dobry\nAglaë : Meuh\nMédor : Grrr\nMarcel Robert Duchamps : Bonjour'
    actual_output_shuffeled = farm.get_talk().rstrip().split('\n')
    actual_output_sorted = sorted(actual_output_shuffeled)
    assert actual_output_sorted == sorted(expected_string_output.split('\n'))

    assert boy.get_nationality_greetings() == {}
    boy.add_nationality_greetings('fr', 'Bonjour')
    assert boy.get_nationality_greetings() == {'fr': 'Bonjour'}

    print("Tests all OK")
