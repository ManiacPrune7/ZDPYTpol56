"""
    sprawdzenie czy liczby dziela sie/nie dziela się przez konkretne inne liczby
    w konkretnym zakresie
"""

# 2000 - 3200


def run_calculations(start, stop):
    """Sprawdza liczby podzielne i niepodzielne.

    :param start: poczatek, int
    :param stop: koniec, int
    :return: lista liczb podzielnych przez 7, niepodzielnych przez 5
    """
    numbers = []

    for i in range(start, stop+1):
        if i % 7 == 0 and i % 5 != 0:
            numbers.append(i)

    return numbers

# print(numbers)


def prettify_print(numbers):
    """Wypisuje 5 liczb w linii.

    :param numbers: lista liczb do wypisania
    """
    max_numbers_in_one_line = 8
    current_numbers_in_line = 0

    for number in numbers:
        if current_numbers_in_line == max_numbers_in_one_line:
            print()
            current_numbers_in_line = 0
        print(number, end=' ')
        current_numbers_in_line += 1


prettify_print(run_calculations(2000, 3200))
