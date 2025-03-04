"""Cree un programa que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, 
        mostrar “Correcto”. Sino, mostrar “incorrecto”. """


primer_numero = int(input('Ingrese el primer número: '))
segundo_numero = int(input('Ingrese el segundo número: '))
tercer_numero = int(input('Ingrese el tercer número: '))


if (primer_numero == 30 or segundo_numero == 30 or tercer_numero == 30):
    print('Correcto!!!')
else:
    suma_numeros = primer_numero + segundo_numero + tercer_numero
    if (suma_numeros == 30):
        print('Correcto!!!')
    else:
        print('Incorrecto!!!')