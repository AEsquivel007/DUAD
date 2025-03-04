"""5. Dada `n` cantidad de notas de un estudiante, calcular:
    1. Cuantas notas tiene aprobadas (mayor a 70).
    2. Cuantas notas tiene desaprobadas (menor a 70).
    3. El promedio de todas.
    4. El promedio de las aprobadas.
    5. El promedio de las desaprobadas. """


import math
cantidad_de_notas_desaprobadas = 0
cantidad_de_notas_aprobadas = 0
promedio_de_notas_total = 0
promedio_de_notas_desaprobadas = 0
promedio_de_notas_aprobadas = 0

total_de_notas = int(input("¿Cuál es el total de notas a ingresar?: "))
contador_de_nota = 1

while (contador_de_nota <= total_de_notas):
    nota_ingresada = int(input(f'Ingrese la nota número {contador_de_nota}:  '))

    if(nota_ingresada < 70):
        cantidad_de_notas_desaprobadas = cantidad_de_notas_desaprobadas + 1
        promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas + nota_ingresada
    else:
        cantidad_de_notas_aprobadas = cantidad_de_notas_aprobadas + 1
        promedio_de_notas_aprobadas = promedio_de_notas_aprobadas + nota_ingresada

    promedio_de_notas_total = promedio_de_notas_total + (nota_ingresada / total_de_notas)
    promedio_de_notas_total_con_2_decimales = math.trunc(promedio_de_notas_total * 100) / 100
    contador_de_nota += 1

if (cantidad_de_notas_aprobadas >= 1):
    promedio_de_notas_aprobadas = promedio_de_notas_aprobadas / cantidad_de_notas_aprobadas
    print(f'El estudiante tiene un total de {cantidad_de_notas_aprobadas} notas aprobadas')
    print(f'El promedio de notas aprobadas es de: {promedio_de_notas_aprobadas}')

if ( cantidad_de_notas_desaprobadas >= 1):
    promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas / cantidad_de_notas_desaprobadas
    print(f'El estudiante tiene un total de {cantidad_de_notas_desaprobadas} notas desaprobadas')
    print(f'El promedio de notas desaprobadas es de: {promedio_de_notas_desaprobadas}')

print(f'El promedio total de notas es de: {promedio_de_notas_total_con_2_decimales}')
