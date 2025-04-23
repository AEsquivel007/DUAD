from datetime import date

class User:
    
    def __init__(self, name:str, date_of_birth: date):
        self.name = name
        self.date_of_birth: date = date_of_birth
    
    
    @property
    def age(self):
        today = date.today()
        return (
            today.year - self.date_of_birth.year - 
            (
                (today.month, today.day) 
                <(self.date_of_birth.month, self.date_of_birth.day)
            )
        )


def is_of_legal_age(func):
    def wrapper_is_of_legal_age(user, *args):
        try:
            if user.age < 18:
                raise ValueError("User is not of legal age.")
            return func(user, *args)
        except ValueError as ex:
            print(f"[WARNING]: {ex}")
    return wrapper_is_of_legal_age


@is_of_legal_age
def drive_a_vehicle(user, type_of_car:str):
        print(f"User {user.name} is allowed to drive a {type_of_car}")


user = User("Alberth", date(1997,10,30))
print(f"The user {user.name} is {user.age} years old.")

drive_a_vehicle(user, "Truck")