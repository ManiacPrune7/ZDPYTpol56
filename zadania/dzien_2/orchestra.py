"""
    Przyklad polimorfizmu na podstawie orkiestry
"""

import abc


class MusicalInstrument(abc.ABC):
    @abc.abstractmethod
    def play(self):
        ...


class Guitar(MusicalInstrument):
    def play(self):
        print("Brzdek, brzdek")


class Flute(MusicalInstrument):
    def play(self):
        print("Fluuu, fluuu")


class Drums(MusicalInstrument):
    def play(self):
        print("Badumtssss")


class Violin(MusicalInstrument):
    def play(self):
        print("Skrzyp skrzyp")


guitar = Guitar()
flute = Flute()
drums = Drums()
vio = Violin()
orchestra = [guitar, flute, drums, vio]


def play_instruments(instruments):
    for instrument in instruments:
        instrument.play()


if __name__ == "__main__":
    play_instruments(orchestra)
