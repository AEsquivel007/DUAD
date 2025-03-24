""" 2. Cree una clase de `Bus` con:
        1. Un atributo de `max_passengers`.
        2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección). 
                **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
        3. Un método para bajar pasajeros uno por uno (en cualquier orden). """


class Bus:

    max_passengers = 2
    passengers_on_bus = []
    
    def validate_total_of_passengers(self):
        total = len(self.passengers_on_bus)
        return total
    
    
    def add_passenger(self, person):
        total_of_passengers = self.validate_total_of_passengers()
        total = total_of_passengers + 1
        
        if total <= self.max_passengers:
            self.passengers_on_bus.append(person)
            print("Se ha subido un nuevo pasajero al bus.")
        
        else:
            print("Lo sentimos, el bus está lleno.")
    
    
    def delete_passenger(self):
        total_of_passengers = self.validate_total_of_passengers()
        
        if total_of_passengers == 0:
            print("Todos los pasajeros se han bajado del bus.")
        
        else:
            self.passengers_on_bus.pop()
            print("Se ha bajado un pasajero del bus.")


class Person():
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age


def main():
    try:
        bus = Bus()
        while True:
            print("""Bienvenido al Sistema de Buses de Lyfter, seleccione una de las siguientes opciones:
            1. Subir pasajero
            2. Bajar pasajero""")
            
            user_input:str = input("Seleccione una de las opciones brindadas: ")
            
            if user_input.isdigit():
                value = int(user_input)
                
                if value == 1:
                    name = input("Ingrese el nombre del pasajero: ")
                    age = int(input("Ingrese la edad del pasajero: "))
                    
                    person = Person(name, age)
                    bus.add_passenger(person)
                elif value == 2:
                    bus.delete_passenger()
                
                response = input("¿Desea realizar otra operación? [s/n]: ")
                
                if response == "n":
                    print("Muchas gracias por usar el Sistema de Buses de Lyfter. Adiós...")
                    break 
            else:
                print("Debe ingresar un valor numérico...")
    
    except Exception as ex:
        print(f"Ha ocurrido un error en el sistema de buses. El error obtenido fue: {ex}")


if __name__ == "__main__":
    main()