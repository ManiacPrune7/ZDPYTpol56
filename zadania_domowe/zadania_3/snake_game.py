"""
Pobierz zawartość pliku snake_game.csv z repozytorium za
pomocą biblioteki csv. Zaproponuj i stwórz strukturę
przechowującą dane na temat przebiegu gry. Dla takich
danych napisz:
a) funkcję sortującą dane, powinny być one poukładane
według ilości zdobytych punktów (rosnąco),
b) funkcję obliczającą średnią ilość zdobytych punktów.
c) funkcję dodającą nowy wiersz danych do pliku csv (funkcja
powinna automatycznie inkrementować indeks danych)
"""

from typing import List


def sort_results(input_path: str) -> List[tuple]:
    ...


def count_mean_points(file_path: str) -> float:
    ...


def add_score(path: str, points: int):
    ...
