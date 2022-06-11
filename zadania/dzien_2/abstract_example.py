"""
    Przyklad działania klas abstrakcyjnych w Pythonie
"""

from abc import ABC, abstractmethod


class MusicalInstrument(ABC):

    @abstractmethod
    def play(self):
        print("Nie wiem jak grac")

    def repair(self):
        print("Zepsulo sie, wiec naprawiam")


class Drums(MusicalInstrument):

    def play_sound(self):
        print("Badumtssss")

    def play(self):
        # super().play()
        print("Badumtssss111111")


class Guitar(MusicalInstrument):

    def play_fine_sound(self):
        print("Brzdek")

    def play(self):
        print("Brzdek111111")


drums = Drums()
drums.play()

guitar = Guitar()
guitar.play()
