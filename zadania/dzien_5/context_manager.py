"""
    prezentacja dzialania context managerow
"""


# with open("path_to_file.txt") as file:
#     file.write('dasdasdas')
#     # file.close()


# def open_db(url):
#     print(url)
#     return url
#
# # Nie jestesmy w stanie wrzucac na context manager (wykorzystujac with)
# # byle jaka funkcje
# with open_db("mysql://user:password") as db:
#     print(f"baza otwarta: {db}")


class DatabaseConnector:

    def __init__(self, url):
        self.url = url
        self.connected = False

    def __enter__(self):
        print("Wywoluje __enter__")
        self.open()
        return self
        # return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Wywoluje __exit__")
        self.close()

    @staticmethod
    def get_data():
        print("DANE Z BAZY")
        # return None

    def open(self):
        print(f"łączę się z bazą, url: {self.url}")
        self.connected = True

    def close(self):
        print(f"zamykam połączenie z bazą, url: {self.url}")
        self.connected = False


# za kazdym razem trzeba otwierac i zamykac - jak to wrzucic na context manager?
# db_conn = DatabaseConnector("mysql://user:password")
# db_conn.open()
# db_conn.get_data()
# db_conn.close()


with DatabaseConnector("mysql://user:password") as db_conn:
    db_conn.get_data()

print(f"Zakonczono: {db_conn.connected}")

# print('----------------')
# print(DatabaseConnector.get_data())
