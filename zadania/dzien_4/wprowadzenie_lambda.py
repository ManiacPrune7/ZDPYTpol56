"""
    lambda wykorzystana jako funkcja do funkcji
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


# def add_one(x: int) -> int:
#     return x+1


long_hello_world = measure_time(long_hello_world)
add_one = measure_time(lambda x: x+1)
