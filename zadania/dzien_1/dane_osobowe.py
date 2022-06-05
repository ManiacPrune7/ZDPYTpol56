"""
    przyklad z danymi osobowymi na dwa sposoby
"""
# ctrl + / -> komentarz wielolinijkowy w Pycharmie

name = "Alojzy"
surname = "Stary"
age = 50
phone = "123-456-789"
job = "listonosz"

person_data = [name, surname, age, phone, job]

NAME_INDEX = 0
# SHOE_SIZE = 27

print(f"imie: {person_data[NAME_INDEX]}")

person_data_dict = {
    "name": name,
    "surname": surname,
    "age": age,
    "phone": phone,
    "job": job
}

print(f"surname: {person_data_dict['surname']}")


def generate_person_data(name, surname, age, phone, job):
    """Funkcja do generacji danych osobowych.

    :param name: imie do wstawienia do slownika, typ: str
    :param surname: ...
    :param age: ...
    :param phone: ...
    :param job: ...
    :return: wygenerowany slownik z danymi osobowymi
    """
    person_data_dict = {
        "name": name,
        "surname": surname,
        "age": age,
        "phone": phone,
        "job": job
    }
    return person_data_dict


print(generate_person_data("Anna", "Inna", 30, "987-654-321", "programistka")["name"])
