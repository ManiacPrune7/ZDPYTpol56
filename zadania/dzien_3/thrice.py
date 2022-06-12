"""
    stworzenie dekoratora thrice uruchamiajacego kod trzykrotnie
"""

from typing import Callable


def thrice(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        for _ in range(3):
            result = func(*args, **kwargs)
        return result
        # return None

    return wrapper


@thrice
def hello():
    print("Hello world!")
    return 5


x = hello()
print(x)
