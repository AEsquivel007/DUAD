"""Cree un programa que le pida 100 números al usuario y muestre el mayor de todos. """

contador = 1
numero_mayor = 0

while (contador <= 100):

    numero_ingresado = int(input(f'Solicitud {contador} de 100 -> Ingrese un número: '))

    if(numero_ingresado > numero_mayor):
        numero_mayor = numero_ingresado

    contador += 1

print(f'El número mayor de los 100 números ingresados es: {numero_mayor}')