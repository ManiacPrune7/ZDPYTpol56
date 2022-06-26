"""
    tworzenie listy kwadratow liczb na 3 sposoby
"""

from typing import List, Generator

# 1 sposob: za pomoca petli for

pre_squares = list(range(1, 11))


def for_squares(numbers: List[int]) -> List[int]:
    squares = []
    for number in numbers:
        squares.append(number**2)
    return squares


# 2 sposob: za pomoca list comprehension

def comprehension_squares(numbers: List[int]) -> List[int]:
    return [number**2 for number in numbers]


def generator_squares(numbers: List[int]) -> Generator:
    return (number**2 for number in numbers)


# 3 sposob: za pomoca funkcji map

def map_squares(numbers: List[int]) -> List[int]:
    return list(map(lambda number: number**2, numbers))


print(for_squares(pre_squares))
print(comprehension_squares(pre_squares))
print(map_squares(pre_squares))
print(list(generator_squares(pre_squares)))
