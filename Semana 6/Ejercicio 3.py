""" 3. Cree una función que retorne la suma de todos los números de una lista.
        a. La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
        b. [4, 6, 2, 29] → 41 """


def sum_numbers(list_of_numbers):
        total = 0
        for number in list_of_numbers:
                total += number
        return total


list_of_numbers = [1, 1, 1, 1, 1, 4, 6, 1, 1, 1, 1, 1, 2, 29, 1, 1, 1, 1, 1]

sum_of_all_numbers = sum_numbers(list_of_numbers)

print(f'El total de la suma de todos los números es de: {sum_of_all_numbers}')