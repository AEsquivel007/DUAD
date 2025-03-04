""" 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
        a. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
        b. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable” """


def order_words_alphabetically_of_a_given_string(phrase):
        list_of_words = phrase.rsplit("-") 

        list_of_words.sort()

        separator = "-"
        ordered_string = separator.join(list_of_words)

        return ordered_string


ordered_string = order_words_alphabetically_of_a_given_string("python-variable-funcion-computadora-monitor")

print(ordered_string)