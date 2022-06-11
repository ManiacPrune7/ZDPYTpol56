"""
    prezentacja tworzenia wlasnych wyjatkow i ich obsluga
"""

from typing import Any


class StrArgTypeError(Exception):
    pass


class NumberArgTypeError(Exception):
    pass


class BoolArgTypeError(Exception):
    pass


class GreaterThanOneLenError(Exception):
    pass


def check_type(arg: Any):

    if type(arg) is str:
        raise StrArgTypeError("BLAD STR")

    # if type(arg) is int or type(arg) is float:
    #     raise NumberArgTypeError

    if type(arg) in (int, float):
        raise NumberArgTypeError

    if type(arg) is bool:
        raise BoolArgTypeError

    if type(arg) in (list, dict, set, tuple) and len(arg) > 1:
        raise GreaterThanOneLenError

    if arg is None:
        print("None jest okej")


def try_func():
    try:
        check_type(True)
    except NumberArgTypeError:
        print("BLAD NUMBER")
    except BoolArgTypeError:
        print("BLAD BOOL")
    except GreaterThanOneLenError:
        print("BLAD LEN")
    finally:
        print("funkcje wykonano")


if __name__ == "__main__":

    try:
        try_func()
    except StrArgTypeError:
        print("BLAD STR")
