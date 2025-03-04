"""Cree un programa que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. 
    Si es menor, muestre cuántos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”. """


tiempo_en_segundos = int(input("Ingrese un tiempo en segundos: "))
tiempo_en_minutos = tiempo_en_segundos / 60

if (tiempo_en_minutos < 10):
    tiempo_faltante_en_segundos = 600 - tiempo_en_segundos
    print(f'Para llegar a 10 minutos en segundos, debes añadir la siguiente cantidad de segundos a la cantidad inicial brindada en segundos: {tiempo_faltante_en_segundos}.')
elif (tiempo_en_minutos == 10):
    print('La cantidad de segundos brindada corresponde a 10 minutos exactos.')
else:
    print('Mayor.')