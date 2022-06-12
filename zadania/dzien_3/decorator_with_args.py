"""
    wypisuje ilosc argumentow za pomoca dekoratora
"""

from typing import Callable


def print_arg(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        # args - tuple, kwargs - dict
        print(args, kwargs)
        result = func(*args, **kwargs)
        print(f"Wykonano z {len(args) + len(kwargs)} argumentami.")
        return result

    return wrapper


@print_arg
def add(a, b):
    return a+b


print(add(a=5, b=15))
