"""Cree un programa que le pida un numero al usuario y muestre la suma de todos los números desde 1 hasta ese número. """

numero_ingresado = int(input('Ingrese un número: '))
contador = 1
acumulador = 0
resultado = 0

while (contador <= numero_ingresado):
    acumulador = acumulador + 1
    resultado = resultado + acumulador
    contador += 1
print(f'La suma total de todos los números desde 1 hasta el número ingresado {numero_ingresado} es de: {resultado}')