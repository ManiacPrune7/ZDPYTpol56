"""
    Dekorator obliczajacy czas dzialania funkcji
"""

import time
from functools import wraps


def measure_time(func):

    @wraps(func)
    def timer(*args, **kwargs):
        """Funkcja wewnetrzna.

        :param args:
        :param kwargs:
        :return:
        """
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Funkcja wywolywala sie {end-start} sekund")
        return result

    # timer.__name__ = func.__name__
    # timer.__doc__ = func.__doc__
    return timer


@measure_time
def long_hello_world():
    """Wypisuje hello world po 2 sekundach

    :return: None
    """
    time.sleep(2)
    print("hello world!")
    # return None


long_hello_world = measure_time(long_hello_world)


def add(a: int, b: int) -> int:
    """Funkcja dodajaca dwie liczby a i b.

    :param a: int do dodania
    :param b: int do dodania
    :return: zwraca sume liczb a i b
    """
    return a+b


print(add.__name__)
print(add.__doc__)

print(long_hello_world.__name__)
print(long_hello_world.__doc__)


long_hello_world()
