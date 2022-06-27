"""
    wyciaganie nazwiska ze stringa z wykorzystaniem modulu re
"""

import re


def get_surname(string: str) -> str:

    pattern = r"^imie: ([A-Z][a-z]+), nazwisko: ([A-Z][a-z]+), wiek: (\d{1,3})$"
    match = re.fullmatch(pattern, string)

    if match is not None:
        # name = match.group(1)
        # print(name)
        surname = match.group(2)
        return surname
    else:
        return "Błędny format!!!"


print(get_surname("imie: Bob, nazwisko: Marley, wiek: 100"))
