"""
Pobierz zawartość pliku snake_game.csv z repozytorium za
pomocą biblioteki csv. Zaproponuj i stwórz strukturę
przechowującą dane na temat przebiegu gry. Dla takich
danych napisz:
c) funkcję dodającą nowy wiersz danych do pliku csv (funkcja
powinna automatycznie inkrementować indeks danych)
"""

import csv


def add_score(path: str, points: int):

    # 1.
    # ustalic ilosc dotychczasowych gier - trzeba to zrobic czytajac plik
    # with open(path) as file:
    #     reader = csv.DictReader(file)
    #     index = 0
    #     for _ in reader:
    #         index += 1
    #
    # print(index)
    #
    # # utworzyc obiekt zapisujacy
    # with open(path, 'a', newline='') as writer_file:  # newline dla windowsa (pozdrawiam)
    #     writer = csv.writer(writer_file)
    #     # wywolac metode writerow z argumentami
    #     writer.writerow([index+1, points])

    # 2.
    with open(path, 'r+', newline='') as read_write_file:  # r+ oznacza: otwórz zarówno do odczytu jak i zapisu

        reader = csv.DictReader(read_write_file)
        index = 0
        for _ in reader:
            index += 1

        writer = csv.writer(read_write_file)
        writer.writerow([index + 1, points])
