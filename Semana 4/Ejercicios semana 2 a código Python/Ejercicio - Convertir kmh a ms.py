"""Cree un programa que le pida al usuario una velocidad en km/h y la convierta a m/s. 
    Recuerda que 1 km == 1000m y 1 hora == 60 minutos * 60 segundos. """

import math
velocidad_en_kmh = int(input('Ingrese una velocidad en kilómetros por hora (km/h): '))
un_km_en_metros = 1000
una_hora_en_segundos = 3600

resultado_en_metros_por_segundo = velocidad_en_kmh * un_km_en_metros / una_hora_en_segundos
resultado_con_dos_decimales_sin_redondeo = math.trunc(resultado_en_metros_por_segundo * 100) / 100

print(f'La conversión de {velocidad_en_kmh} kilómetros por hora (km/h) a metros por segundo (m/s) es de: {resultado_con_dos_decimales_sin_redondeo}')