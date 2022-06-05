"""
    sprawdzenie wieku uzytkownika na podstawie inputu
"""

age = int(input("Podaj swoj wiek: "))

if age >= 18:
    print("Jestes osoba pelnoletnia.")
    if age >= 100:
        print("200 lat!!!")
    else:
        print("100 lat!!!")
else:
    print("Jestes osoba niepelnoletnia.")
    print(f"Do osiemnastki zostalo Ci: {18 - age}")
