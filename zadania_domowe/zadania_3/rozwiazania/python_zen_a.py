"""
Na podstawie pliku python_zen.txt z repozytorium, wykonaj szereg
operacji:
a) Napisz funkcję wczytującą plik i wyliczającą ilość linii oraz ilość
znaków niebędących spacjami
"""


def count_lines_and_signs(file_path: str) -> tuple:

    with open(file_path) as file:

        amount_of_lines = 0
        amount_of_signs = 0

        for line in file:
            amount_of_lines += 1
            # 1.
            # amount_of_signs += sum([1 for sign in line if sign != " "])
            # 2.
            # amount_of_signs += len([sign for sign in line if sign != " "])
            # 3.
            amount_of_signs += len(list(filter(lambda sign: sign != " ", line)))
            # 4.
            # for sign in line:
            #     if sign != " ":
            #         amount_of_signs += 1

    return amount_of_lines, amount_of_signs
