"""
    utworzenie ogolnego dekoratora do wykorzystania przez rozne funkcje
"""

from typing import Callable


def author(function: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        print("Autor: JA")
        x = function(*args, **kwargs)
        print("Najlepszy autor")
        return x
        # return None

    return wrapper


@author
def hello(name):
    print(f"hello {name}!")
    return name


@author
def goodbye(name):
    print(f"goodbye {name}!")


@author
def hi():
    print("hiiiiii!!!")


print(hello("Joe"))
print(goodbye("Joe"))
hi()
