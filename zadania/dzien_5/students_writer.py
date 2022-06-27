"""
    jak zapisywac do pliku csv z wykorzystaniem modulu csv?
"""

import csv

with open(
    r'C:\Users\lukie\OneDrive\Dokumenty\SDA\zajecia_repos\ZDPYTpol56\materialy\students_dict.csv',
    'w',
    newline=""
) as file:
    # z wykorzystaniem csv.writer
    # writer = csv.writer(file)
    # writer.writerow(["Marian", "M", 193, 113])

    # z wykorzystaniem DictWritera
    writer = csv.DictWriter(file,
                            fieldnames=["name", "gender", "height", "weight"])
    writer.writeheader()
    writer.writerow(
        {"name": "Marian", "gender": "M", "height": 193, "weight": 113}
    )
