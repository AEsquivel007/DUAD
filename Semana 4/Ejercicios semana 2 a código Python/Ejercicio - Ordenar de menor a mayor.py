"""Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas (primero y segundo) 
y los ordene de menor a mayor en dichas variables. """

primer_numero = int(input('Ingrese el primero número: '))
segundo_numero = int(input('Ingrese el segundo número: '))

if (primer_numero > segundo_numero):
    variable_temporal = primer_numero
    primer_numero = segundo_numero
    segundo_numero = variable_temporal
print(f'El número menor es: {primer_numero}')
print(f'El número mayor es: {segundo_numero}')