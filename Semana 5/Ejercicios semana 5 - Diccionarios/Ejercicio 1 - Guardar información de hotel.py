""" 1. Cree un diccionario que guarde la siguiente información sobre un hotel:
    - nombre
    - numero_de_estrellas
    - habitaciones
- El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
    - numero
    - piso
    - precio_por_noche """

import json


hotel_dictionary = {}
rooms = []
counter = 1

hotel_name = input("Ingrese el nombre del hotel: ")
number_of_stars = int(input("Ingrese el número de estrellas: "))
number_of_rooms = int(input("Ingrese el número de habitaciones: "))

hotel_dictionary["hotel_name"] = hotel_name
hotel_dictionary["number_of_stars"] = number_of_stars
hotel_dictionary["number_of_rooms"] = number_of_rooms
hotel_dictionary["rooms"] = rooms

while (counter <= number_of_rooms):
    room_number = input(f'Ingrese el número de la {counter}° habitación: ')
    floor_number = input(f'Ingrese el número de piso de la {counter}° habitación: ')
    price_per_night = input(f'Ingrese el precio por noche de la {counter}° habitación: ')

    hotel_dictionary["rooms"].append({"room_number": room_number, "floor_number": floor_number, "price_per_night": price_per_night})

    counter += 1 

formatted_dictionary = json.dumps(hotel_dictionary)

print(formatted_dictionary)