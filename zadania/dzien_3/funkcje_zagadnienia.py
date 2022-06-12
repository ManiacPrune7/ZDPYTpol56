"""
    pokazanie mozliwosci w przyjmowaniu funkcji jako arg, zwracaniu i definicji
"""

from typing import Callable


def func_outer(func: Callable):
    x = func()
    print(x)
    return x


def hello():
    return "hello"


def goodbye():
    return "goodbye"


def hi(name):
    return f"hi {name}!"


# print(hello())
tmp_func = func_outer(hello)
print(tmp_func is hello)

tmp_func = func_outer(goodbye)
print(tmp_func is hello)

# tmp_func = func_outer(hi)
# print(tmp_func is hi)
