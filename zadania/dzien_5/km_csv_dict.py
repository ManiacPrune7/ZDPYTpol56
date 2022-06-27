"""
    analiza pliku km.csv z wykorzystaniem csv.DictReadera
"""

import csv


with open(r'C:\Users\lukie\OneDrive\Dokumenty\SDA\zajecia_repos\ZDPYTpol56\materialy\km.csv') as file:

    csv_reader = csv.DictReader(file)
    kms = {}

    for row in csv_reader:
        kms[row['Dzien']] = int(row['Przebiegniete kilometry'])

    print(kms)
    print(sum(kms.values()))
    print(round(sum(kms.values()) / len(kms), 2))
