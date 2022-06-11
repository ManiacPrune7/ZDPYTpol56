"""
    Przykład starej obsługi błędów.
"""

# from typing import Union
import typing


def podaj_imie(imie: str) -> typing.Union[str, int]:
    if type(imie) is str:
        print(imie)
        return imie
    else:
        print("Bledny typ arg imie!!!")
        return -1


x = podaj_imie(23)
