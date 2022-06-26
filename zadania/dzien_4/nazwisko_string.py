"""
    wyciaganie nazwiska ze stringu z wykorzystaniem metod str
"""


def get_surname(string: str) -> str:
    # return string.split('nazwisko: ')[1].split(',')[0]
    start = string.find('nazwisko: ') + len('nazwisko: ')
    end = string.find(', wiek:')
    return string[start:end]


print(get_surname('imie: Jan, nazwisko: Kowalski, wiek: 50'))
