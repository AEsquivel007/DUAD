"""Cree un programa que le pida 5 números al usuario y muestre el mayor. """

primer_numero = int(input('Ingrese el primer número: '))
segundo_numero = int(input('Ingrese el segundo número: '))
tercer_numero = int(input('Ingrese el tercer número: '))
cuarto_numero = int(input('Ingrese el cuarto número: '))
quinto_numero = int(input('Ingrese el quinto número: '))

numero_mayor = primer_numero

if(segundo_numero > numero_mayor):
    numero_mayor = segundo_numero
if(tercer_numero > numero_mayor):
    numero_mayor = tercer_numero
if(cuarto_numero > numero_mayor):
    numero_mayor = cuarto_numero
if(quinto_numero > numero_mayor):
    numero_mayor = quinto_numero

print(f'Los números ingresados fueron, {primer_numero}, {segundo_numero}, {tercer_numero}, {cuarto_numero}, {quinto_numero}')
print(f'De los números ingresados, el número mayor es: {numero_mayor}')
