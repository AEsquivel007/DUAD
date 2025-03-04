"""Cree un programa que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer o 2 si es hombre, 
    y muestre al final el porcentaje de mujeres y hombres. """


import math

cantidad_de_sexos_a_ingresar = 6
contador = 1
cantidad_sexos_masculinos = 0
cantidad_sexos_femeninos = 0
porcentaje_hombres = 0
porcentaje_mujeres = 0

while (contador <= cantidad_de_sexos_a_ingresar):
    sexo_ingresado = int(input('Por favor ingrese el sexo [1-Mujer, 2-Hombre]: '))
    if (sexo_ingresado == 1):
        cantidad_sexos_femeninos += 1
    elif (sexo_ingresado == 2):
        cantidad_sexos_masculinos += 1
    else:
        print(f'El valor {sexo_ingresado} es inválido, por favor ingrese uno válido [1-Mujer, 2-Hombre]:')
        contador -=1

    contador += 1

if (cantidad_sexos_femeninos != 0):
    porcentaje_mujeres = (cantidad_sexos_femeninos / cantidad_de_sexos_a_ingresar) * 100
    porcentaje_mujeres_con_dos_decimales = math.trunc(porcentaje_mujeres * 10) / 10
    print(f'El porcentaje de mujeres es de: {porcentaje_mujeres_con_dos_decimales} %.')

if (cantidad_sexos_masculinos != 0):
    porcentaje_hombres = (cantidad_sexos_masculinos / cantidad_de_sexos_a_ingresar) * 100
    porcentaje_hombres_con_dos_decimales = math.trunc(porcentaje_hombres * 10) / 10
    print(f'El porcentaje de hombres es de: {porcentaje_hombres_con_dos_decimales} %.')