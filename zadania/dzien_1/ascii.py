"""
    wypisanie numerow z tabeli kodow ascii
"""


def sign_to_number(S):
    """Zamienia kazdy znak napisu na liczbe z tabeli ascii.

    :param S: string
    """
    for sign in S:
        print(f"Character: {sign} - ascii code: {ord(sign)}")


sign_to_number("ABCDEF")