"""
    analiza najwyzszego ucznia i najwyzszej uczennicy
"""

import csv
from functools import reduce


def find_tallest_students(path: str) -> tuple:

    with open(path) as file:

        csv_reader = csv.reader(file)

        man_height = []
        woman_height = []

        for row in csv_reader:
            if row[1] == 'M':
                man_height.append((row[0], int(row[2])))
            else:
                woman_height.append((row[0], int(row[2])))

        # print(man_height)
        # print(woman_height)
        heighest_man = reduce(lambda x, y: x if x[1] > y[1] else y, man_height)
        heighest_woman = reduce(
            lambda x, y: x if x[1] > y[1] else y, woman_height
        )
        return heighest_man[0], heighest_woman[0]


print(
    find_tallest_students(
        r'C:\Users\lukie\OneDrive\Dokumenty\SDA\zajecia_repos\ZDPYTpol56\materialy\students.csv'
    )
)
