""" Cree un programa que intercambie el primer y último elemento de una lista. 
        Debe funcionar con listas de cualquier tamaño. 
        my_list = [4, 3, 6, 1, 7]"""

my_list = [4, 3, 6, 1, 7]

first_element = 0
last_element = 0
end_index = 0

for index in range(0, len(my_list)):
    if (index == 0):
        first_element = my_list[index]

    if (index == my_list.index(my_list[-1])):
        last_element = my_list[index]
        end_index = index

print(f'La lista original es: {my_list}')

my_list[0] = last_element
my_list[end_index] = first_element

print(f'El resultado de intercambiar el primer y último elemento de la lista origial es: {my_list}')