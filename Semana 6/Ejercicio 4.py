""" 4. Cree una función que le de la vuelta a un string y lo retorne.
        a. Esto ya lo hicimos en iterables.
        b. “Hola mundo” → “odnum aloH” """


def reverse_a_string(string_to_reverse):
        reversed_string = ""
        for char in string_to_reverse[::-1]:
                reversed_string += char
        return reversed_string


string_to_reverse = "Hola mundo"

reversed_string = reverse_a_string(string_to_reverse)

print(f'El resultado de reversar el texto "{string_to_reverse}" es: "{reversed_string}"')