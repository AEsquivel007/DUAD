""" 1. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
        Ejemplos:
            list_a = ["first_name", "last_name", "role"]
            list_b = ["Alek", "Castillo", "Software Engineer"]
                → {"first_name": "Alek", "last_name": "Castillo", "role": "Software Engineer"} """

list_a = ["first_name", "last_name", "role"]
list_b = ["Alberth", "Esquivel", "QA Engineer"]

dictionary_result = {}

for index in range(0, len(list_a)):
    key = list_a[index]
    value = list_b[index]

    dictionary_result[key] = value

print(dictionary_result)