""" Cree un programa que elimine todos los números impares de una lista. 
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]"""

my_list = [1, 1, 1, 1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 6, 7, 8, 1, 1, 1, 9, 10, 11, 11, 11, 11, 11]
my_odd_numbers = []


# 1. Eliminar los impares recorriendo la lista de atrás hacia adelante. 
        # -> Soluciona problema de no encontrar el íncide eliminado.

for index in range(len(my_list)-1, -1, -1):
        number_in_list = my_list[index]

        if(number_in_list % 2 != 0):
                odd_number = my_list.pop(index)
                my_odd_numbers.insert(0, odd_number)

print(f'El resultado de la lista con números pares es: {my_list}')
print(f'Los elementos impares de la lista son: {my_odd_numbers}')


# 2. Eliminar los impares de la lista a través de una lista auxiliar.
        # -> Soluciona problema de no encontrar el íncide eliminado.

my_list_1 = [1, 1, 1, 1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 6, 7, 8, 1, 1, 1, 9, 10, 11, 11, 11, 11, 11]
my_odd_numbers_1 = []

for index, element in enumerate(my_list_1[:]):
        
        if(element %2 != 0):
                my_list_1.remove(element)
                my_odd_numbers_1.append(element)

print(f'El resultado de la lista con números pares es: {my_list_1}')
print(f'Los elementos impares de la lista son: {my_odd_numbers_1}')