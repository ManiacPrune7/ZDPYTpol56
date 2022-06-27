"""
    analiza pliku km.csv z wykorzystaniem csv.readera
"""

import csv


with open(r'C:\Users\lukie\OneDrive\Dokumenty\SDA\zajecia_repos\ZDPYTpol56\materialy\km.csv') as file:

    csv_reader = csv.reader(file)
    kms = {}

    no_line = 0
    for line in csv_reader:
        if no_line == 0:
            no_line += 1
            continue
        kms[line[0]] = int(line[1])

    print(kms)
    print(sum(kms.values()))
    print(round(sum(kms.values()) / len(kms), 2))
