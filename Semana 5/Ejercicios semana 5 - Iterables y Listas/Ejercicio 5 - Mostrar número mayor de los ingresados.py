""" Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, 
        seguido del numero ingresado más alto. 
                86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [54, 86, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86."""

counter = 1
largest_number = 0
my_list = []

while (counter <= 10):
        number_entered = int(input(f'Por favor digite el {counter}° número: '))
        my_list.append(number_entered)

        if(number_entered > largest_number):
                largest_number = number_entered

        counter += 1

print(f'La lista de los números ingresados es: {my_list}. Donde el número más alto fue: {largest_number}')