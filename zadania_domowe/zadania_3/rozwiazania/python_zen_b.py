"""
Na podstawie pliku python_zen.txt z repozytorium, wykonaj szereg
operacji:
b) Napisz funkcję, która podmieni wszystkie słowa „is‛ na słowa „was‛ i
zapisze wynik do nowego pliku
"""


def replace_word(source_file: str,  # python_zen.txt
                 destination_file: str,  # python_zen_was.txt
                 word_to_replace: str,  # is
                 replacing_word: str):  # was

    with open(source_file, "r") as file:
        lines = file.readlines()

    with open(destination_file, "w") as file:
        for line in lines:
            file.write(line.replace(word_to_replace, replacing_word))
