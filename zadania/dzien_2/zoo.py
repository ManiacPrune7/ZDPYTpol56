"""
    przykład z Zoo, z wykorzystaniem klas abstrakcyjnych i polimorfizmu
"""

import abc


class Animal(abc.ABC):

    def __init__(self, name: str):
        self.name = name

    @abc.abstractmethod
    def move(self):
        ...

    @abc.abstractmethod
    def make_noise(self):
        ...

    @abc.abstractmethod
    def eat(self):
        ...


class Lion(Animal):

    def __init__(self, name: str, ferocity: int):
        super().__init__(name)
        self.ferocity = ferocity

    def move(self):
        print("Biegu biegu")

    def make_noise(self):
        print("Roaarrrrr!!!")

    def eat(self):
        print("Mlasku mlask!")


class Eagle(Animal):

    def __init__(self, name: str, flight_speed: float):
        super().__init__(name)
        self.flight_speed = flight_speed

    def move(self):
        print("Lotu lotu")

    def make_noise(self):
        print("Arrrrrrr!!!")

    def eat(self):
        print("Dziob dziob!")


class Zoo:

    def __init__(self, animals):
        self.animals = animals

    def open(self):
        for animal in self.animals:
            animal.move()
            animal.make_noise()

    def close(self):
        for animal in self.animals:
            animal.eat()
            animal.make_noise()
            animal.move()


# animals = [Lion("Leon", 100), Eagle("Bob", 50.5)]
zoo_wroclaw = Zoo([Lion("Leon", 100), Eagle("Bob", 50.5)])
zoo_wroclaw.open()
zoo_wroclaw.close()
