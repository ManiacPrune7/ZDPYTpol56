"""
    uruchomienie funkcji lub nie w zaleznosci od SHOULD_BE_RUN
"""

from typing import Callable

SHOULD_BE_RUN = True


def should_be_run(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        if SHOULD_BE_RUN:
            return func(*args, **kwargs)
        else:
            print("POMIJAM...")
        # return None

    return wrapper


@should_be_run
def hello():
    print("hello world!")
    return "RESULT"


print(hello())
