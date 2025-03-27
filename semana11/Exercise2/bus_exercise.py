class Bus:

    def __init__(self):
        self.passengers_on_bus = []
        self.max_passengers = 2
    
    def validate_total_of_passengers(self):
        total = len(self.passengers_on_bus)
        return total
    
    
    def add_passenger(self, person):
        total_of_passengers = self.validate_total_of_passengers()
        total = total_of_passengers + 1
        
        if total <= self.max_passengers:
            self.passengers_on_bus.append(person)
            print("A passanger got on the bus.")
        
        else:
            print("Sorry, the bus doesn't have seats.")
    
    
    def delete_passenger(self):
        total_of_passengers = self.validate_total_of_passengers()
        
        if total_of_passengers == 0:
            print("All the passengers have gotten off the bus.")
        
        else:
            self.passengers_on_bus.pop()
            print("A passenger has gotten off the bus.")


class Person():
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age


def main():
    try:
        bus = Bus()
        while True:
            print("""Welcome to the Lyfter's Bus System, please select one of the following options:
            1. Pick up passanger
            2. Drop off passanger""")
            
            user_input:str = input("Select one of the given options: ")
            
            if user_input.isdigit():
                value = int(user_input)
                
                if value == 1:
                    name = input("Insert the name of the passanger: ")
                    age = int(input("Insert the age of the passanger: "))
                    
                    person = Person(name, age)
                    bus.add_passenger(person)
                elif value == 2:
                    bus.delete_passenger()
                
                response = input("Would you like to continue using the system? [s/n]: ")
                
                if response == "n":
                    print("Thank you for using the Lyfter's Bus System. Bye!!!")
                    break 
            else:
                print("You have to provide a numeric value...")
    
    except Exception as ex:
        print(f"ERROR: An unexpected error occurred. System error: {ex}")


if __name__ == "__main__":
    main()