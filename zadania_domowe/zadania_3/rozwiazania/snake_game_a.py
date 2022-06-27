"""
Pobierz zawartość pliku snake_game.csv z repozytorium za
pomocą biblioteki csv. Zaproponuj i stwórz strukturę
przechowującą dane na temat przebiegu gry. Dla takich
danych napisz:
a) funkcję sortującą dane, powinny być one poukładane
według ilości zdobytych punktów (rosnąco),
"""

import csv
from typing import List


def sort_results(input_path: str) -> List[tuple]:

    # wczytac plik za pomoca modulu csv
    with open(input_path, 'r') as file:
        csv_reader = csv.DictReader(file)

        games_and_points = []

        # zapisać dane do listy/slownika ?
        # otrzymac liste tupli z danych - [(1, 30), (2, 29), ...]
        for row in csv_reader:
            games_and_points.append(tuple(row.values()))

        # print(games_and_points)

        # posortowac wedlug punktow - sorted/sort + key
        games_and_points.sort(key=lambda pair: int(pair[1]))

        # zwrocic wynik
        return games_and_points
