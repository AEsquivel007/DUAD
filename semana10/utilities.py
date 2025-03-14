import os
import menu
import json


def display_menu():
    try:
        print("""Bienvenido al Sistema de Control de Estudiantes de Lyfter, seleccione una de las siguientes opciones:
            1. Registrar información de estudiantes
            2. Ver información de todos los estudiantes
            3. Ver top tres de estudiantes con mejor promedio
            4. Ver la nota promedio entre todos los estudiantes
            5. Exportar datos a archivo CSV
            6. Importar datos de un archivo CSV""")
        
        given_option:str = input("Seleccione una de las opciones anteriores (debe ingresar el número de la opción): ")

        if given_option.isdigit():
            option = int(given_option)

            if option > 0 and option < 7:
                menu.select_option(option)
            else:
                print("El número ingresado no corresponde a ninguna de las opciones brindadas, por favor ingrese un número válido entre el 1 y 6.")
        else:
            print("Por favor ingrese un valor numérico, solo números son permitidos.")
        
    except ValueError as ex:
        print("Lo sentimos, ha ocurrido un error al seleccionar una de las opciones.")
        print(f"El error obtenido por el sistema es: {ex}")
        exit()


def validate_if_file_exists(path):
    try:      
        file_exists = os.path.exists(path)
        
        if file_exists:    
            return True
        return False
    except Exception as ex:
        print("ERROR: Ha ocurrido un error al intentar validar la existencia del archivo.")
        print(f"El error obtenido por el sistema es: {ex}")


def validate_if_file_is_empty(path):
    try:
        file_exists = validate_if_file_exists(path)
        
        if file_exists:
            length = os.path.getsize(path)
            if length > 0:
                return True
            return False
        else:
            return False
    except Exception as ex:
        print("ERROR: Ha ocurrido un error al intentar validar longitud del archivo.")
        print(f"El error obtenido por el sistema es: {ex}")


def ask_if_continue():
    try:
        while True:
            user_input = input("¿Deseas seguir usando el sistema, (s/n)?: ")
            
            if user_input not in ["s","n"]:
                print("ERROR: Los únicos valores aceptados como respuesta son: (s) y (n)...")
            elif user_input == "s":
                return True
            else:
                return False

    except Exception as ex:
        print("ERROR: Ha ocurrido un error al momento de continuar con la ejecución del programa.")
        print(f"El error obtenido por el sistema es: {ex}")
        print("Muchas gracias.")


def obtain_path_file():
    path_file = "semana10/students.json"
    return path_file


def obtain_csv_path_file():
    path_file = "semana10/exported_data_of_students.csv"
    return path_file


def calculate_average_per_student():
    path_file = obtain_path_file()
    students_average = []
    
    try:
        with open(path_file, "r", encoding = "utf-8") as file:
            file_content = file.read()
            json_data = json.loads(file_content)
            
        for student in json_data:
            scores = student["scores"].values()
            values = list(map(float,scores))
            total = sum(values)
            total_scores = len(values)

            average_per_student = total / total_scores
            
            average = {"full_name" : student["full_name"], "average" : average_per_student}
            students_average.append(average)
        
        return students_average

    except Exception as ex:
        print("ERROR: Ha ocurrido un error al intentar calcular la nota promedio de cada estudiante.")
        print(f"El error obtenido por el sistema es: {ex}")