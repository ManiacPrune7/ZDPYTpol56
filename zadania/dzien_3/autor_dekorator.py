"""
    definicja dekoratora z wypisywaniem autora funkcji
"""

from typing import Callable


def author(function: Callable) -> Callable:

    def wrapper(name):
        print("Autor: JA")
        function(name)
        print("Najlepszy autor")

    return wrapper


@author
def hello(name):
    print(f"hello {name}!")


@author
def goodbye(name):
    print(f"goodbye {name}!")


# dekorator to funkcja
# dekorator musi przyjmowac inna funkcje jako argument
# dekorator musi definiować funkcję wewnętrzną
# dekorator musi zwracać funkcję wewnętrzną którą zdefiniował


# hello()
# hello = author(hello)#()
# decorated_func()
hello("Joe")

# goodbye = author(goodbye)
goodbye("Joe")
