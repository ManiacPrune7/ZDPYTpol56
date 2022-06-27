"""
    odczytujemy z csv, zapisujemy do jsona
"""

import csv
import json

with open(r'C:\Users\lukie\OneDrive\Dokumenty\SDA\zajecia_repos\ZDPYTpol56\materialy\students.csv') as file:
    csv_reader = csv.reader(file)

    students = []

    for row in csv_reader:
        student = {
            "name": row[0],
            "gender": row[1],
            "height": int(row[2]),
            "weight": int(row[3])
        }
        students.append(student)

with open(r'C:\Users\lukie\OneDrive\Dokumenty\SDA\zajecia_repos\ZDPYTpol56\materialy\students.json', 'w') as file:
    json.dump(students, file, indent=2)
