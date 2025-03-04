""" 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
        a. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
        b. Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código. No busque el código, eso no ayudaría.
        c. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada número es primo, y agregarlo a otra lista). 
            Así que lo mejor es agregar **otra función** para revisar si el número es primo o no.* """


def is_prime(number_to_validate):
    if number_to_validate < 2:
        return False
    else:
        for number in range(2, int(number_to_validate ** 0.5) + 1):
            if number_to_validate % number == 0:
                return False
    return True


def validate_prime_numbers(list_of_numbers):
    list_of_prime_numbers = []

    for number in list_of_numbers:
        result = is_prime(number)

        if result == True:
            list_of_prime_numbers.append(number)

    return list_of_prime_numbers


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 25, 67, 70, 71, 72, 73, 89, 90, 96, 97]

result_of_prime_numbers = validate_prime_numbers(list_of_numbers)

print(result_of_prime_numbers)