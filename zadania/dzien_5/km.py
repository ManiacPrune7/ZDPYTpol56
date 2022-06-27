"""
    analiza pliku km.csv bez wykorzystania modulu csv
"""


with open(r'C:\Users\lukie\OneDrive\Dokumenty\SDA\zajecia_repos\ZDPYTpol56\materialy\km.csv') as file:

    kms = {}
    # i = 0
    for i, line in enumerate(file):
        if i == 0:
            # i += 1
            continue
        stripped_line = line.strip()
        row = stripped_line.split(',')
        kms[row[0]] = int(row[1])

    print(kms)
    print(sum(kms.values()))
    print(round(sum(kms.values())/len(kms), 2))
