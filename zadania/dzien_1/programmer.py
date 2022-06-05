"""
    definicja klasy programisty
"""

from human import Human


class Programmer(Human):

    def __init__(self, name, surname, age, energy, languages):
        super().__init__(name, surname, age, energy)
        self.languages = languages

    def do_programming(self, hours):
        self.energy -= 5*hours


ada = Programmer("Ada", "X", 25, 100, ['Python', 'Java', 'Scala'])
print(ada.energy)
ada.do_programming(6)
print(ada.energy)
ada.eat()
print(ada.energy)
print(ada.name)
