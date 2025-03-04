"""2. Cree un programa que le pida al usuario su nombre, apellido, y edad, 
y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor. """


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

classification = ""

if (edad >= 0 and edad <=  2):
    classification = "Bebé"
elif (edad >= 3 and edad <= 11):
    classification = "Niño"
elif (edad >= 12 and edad <= 13):
    classification = "Preadolescente"
elif (edad >= 13 and edad <= 19):
    classification = "Adolescente"
elif (edad >= 20 and edad <= 35):
    classification = "Adulto joven"
elif (edad >= 36 and edad <= 64):
    classification = "Adulto"
else:
    classification = "Adulto mayor"

print(f'Hola {nombre} {apellido}, según tu edad eres un: {classification}')