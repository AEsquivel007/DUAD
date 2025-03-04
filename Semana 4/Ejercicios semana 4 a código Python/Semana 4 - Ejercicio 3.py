"""3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
    1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute."""

import random

numero_secreto = random.randint(0, 10)
print(numero_secreto)

while (True):
    numero = int(input("Ingrese un número: "))
    if(numero == numero_secreto):
        break
print("Felicidades, adivinaste el número secreto.!!!")