"""4. Cree un programa que le pida tres números al usuario y muestre el mayor. """

primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))
tercer_numero = int(input("Ingrese el tercer número: "))

numero_mayor = primer_numero
if (segundo_numero > numero_mayor):
    numero_mayor = segundo_numero
if (tercer_numero > numero_mayor):
    numero_mayor = tercer_numero

print(f'El número mayor es: {numero_mayor}')