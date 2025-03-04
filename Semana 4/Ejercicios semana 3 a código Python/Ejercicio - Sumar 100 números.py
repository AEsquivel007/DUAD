"""Cree un programa que le pida 100 números al usuario y muestre la suma de todos. """

contador = 1
suma_total = 0

while (contador <= 100):

    numero_ingresado = int(input(f'Solicitud {contador} de 100 -> Ingrese un número: '))
    suma_total += numero_ingresado

    contador +=1

print(f'La suma total es: {suma_total}')