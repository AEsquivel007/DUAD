""" 3. Cree un programa que use una lista para eliminar keys de un diccionario.
    Ejemplos:
        list_of_keys = ["access_level", "age", "phone_number"]
        employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}
            → {"name": "John", 'email": "john@ecorp.com"} """

list_of_keys = ["access_level", "age", "phone_number"]
employee = {"name": "Alberth", "email": "alberth@test.com", "access_level": 5, "age": 28, "phone_number": "+506 8899-0011"}

print(f'Información original del empleado: {employee}')

for key in list_of_keys:
    employee.pop(key)

print(f'Información actualizada del empleado: {employee}')