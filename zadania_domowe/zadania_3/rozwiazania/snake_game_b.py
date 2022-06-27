"""
Pobierz zawartość pliku snake_game.csv z repozytorium za
pomocą biblioteki csv. Zaproponuj i stwórz strukturę
przechowującą dane na temat przebiegu gry. Dla takich
danych napisz:
b) funkcję obliczającą średnią ilość zdobytych punktów.
"""
import csv


def count_mean_points(file_path: str) -> float:

    with open(file_path) as file:

        csvreader = csv.DictReader(file)
        points = 0
        n = 0

        for game in csvreader:
            points += int(game["Points"])
            n += 1

        return points/n
