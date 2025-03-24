import os
import menu


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
        print(f"Error obtenido por el sistema: {ex}")
        exit()


def validate_if_file_exists(path):
    try:      
        file_exists = os.path.exists(path)
        
        if file_exists:    
            return True
        return False
    except:
        print("ERROR: Ha ocurrido un error al intentar validar la existencia del archivo.")


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
    except:
        print("ERROR: Ha ocurrido un error al intentar validar longitud del archivo.")


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

    except:
        print("ERROR: Ha ocurrido un error al momento de continuar con la ejecución del programa.")
        print("Muchas gracias.")


def obtain_csv_path_file():
    path_file = "semana11/Exercise3/exported_data_of_students.csv"
    return path_file
