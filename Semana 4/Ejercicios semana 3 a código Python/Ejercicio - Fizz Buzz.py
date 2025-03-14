"""Cree un programa que le pida un numero al usuario y muestre “Fizz” si es divisible entre 3, “Buzz” 
        si es divisible entre 5, y “FizzBuzz” si es divisible entre ambos. """


numero_ingresado = int(input('Ingrese un número: '))
if(numero_ingresado % 3 == 0 and numero_ingresado % 5 == 0):
    print('FizzBuzz')
elif(numero_ingresado % 3 == 0):
    print('Fizz')
elif(numero_ingresado % 5 == 0):
    print('Buzz')
else:
    print(f'El número ingresado {numero_ingresado} no es divisible por 3 o por 5.')