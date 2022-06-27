"""
    weryfikacja emaila za pomoca moduly re
"""

import re


def verify_email(string: str) -> str:  # YES - jesli poprawny, NO - jezeli nie

    pattern = r"[A-Za-z_]+@[A-Za-z]+\.[a-z]{2,3}"
    match = re.fullmatch(pattern, string)

    if match is not None:
        return "YES"
    else:
        return "NO"


print(verify_email("supernazwaemaila@google.com"))
