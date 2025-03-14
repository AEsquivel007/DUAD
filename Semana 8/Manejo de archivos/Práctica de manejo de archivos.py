def open_and_print_file_content(path):
    with open(path) as file:
        print(file.read())


def open_and_print_file_by_line(path):
    with open(path, "r") as file:
        for line in file.readlines():
            print(f"Línea: {line}")


def write_text_in_a_file(path, text):
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)


open_and_print_file_content("my_file.txt")
#open_and_print_file_by_line("superheroes.txt")

text = "This is Alberth, adding its first line in a file."

text_to_write = """
Tradicionalmente, el número de especies de pingüinos a nivel mundial es de 17.
En 2006, se cambió este número a 18, cuando se empezó a reconocer al
pingüino saltarrocas como dos especies distintas:
el pingüino saltarrocas austral y el pingüino saltarrocas norteño.
"""


write_text_in_a_file("my_file.txt",text_to_write)
open_and_print_file_content("my_file.txt")