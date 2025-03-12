import json
import utilities


def register_student_information():
    counter = 0
    
    try:
        while True:
            user_input = input("Ingrese el total de estudiantes a los que les desea registrar la información en el sistema: ")
            if user_input.isdigit():
                total_of_students = int(user_input)
                while counter < total_of_students:
                    type_student_information(counter)
                    counter += 1
                break
            else:
                print("ERROR: Debe ingresar un número entero positivo. ")
    except:
        print("Lo sentimos, ha ocurrido un error inesperado en el sistema.")
        exit()


def type_student_information(counter):
    subjects = {
        "spanish": "español", 
        "english": "inglés", 
        "geography": "geografía", 
        "science": "ciencias"
    }
    
    try:
        scores = {}
        while True:
            full_name = input(f"Ingrese el nombre completo del {counter + 1}° estudiante: ")
            if full_name.replace(" ", "").isalpha():
                break
            print("ERROR: El nombre del estudiante solo debe contener letras.")
        
        while True:
            student_section = input("Ingrese la sección del estudiante: ")
            if student_section.isalnum():
                break
            print("ERROR: Solo letras y números son permitidos. Por favor no inserte espacios ni caracteres especiales.")   
        
        for key, subject in subjects.items():

            while True:
                given_score = input(f"Ingrese la calificación de la materia de {subject}: ")
                
                if given_score.isdigit():
                    score = float(given_score)
                    
                    if score >= 0 and score <= 100:
                        scores[key] = score
                        break
                    else:
                        print(f"ERROR: Debe ingresar una nota entre 0 y 100 para la calificación de {subject}.")
                else:
                    print(f"ERROR: La nota ingresada para la asignación de {subject} solo debe contener valores númericos.") 
        student_information = {"full_name": full_name, "student_section": student_section, "scores": scores}
        register_information_within_json_file(student_information)
        
    except ValueError as ex:
        print("Ha ocurrido un error al intentar registrar el estudiante, inténtelo más tarde.")
        exit()


def register_information_within_json_file(student_information):
    path_file = utilities.obtain_path_file()
    try:
        students = []
        students.append(student_information)
        
        file_exists = utilities.validate_if_file_exists(path_file)
        file_is_empty = utilities.validate_if_file_is_empty(path_file)
        
        if not file_exists or not file_is_empty:
            with open(path_file, "w", encoding = "utf-8") as file:
                content = json.dumps(students, indent = 4, separators = (",", ":"))
                file.write(content)
        
        else:

            with open(path_file, "r", encoding = "utf-8") as file:
                json_content = file.read()
                data:list = json.loads(json_content)
                data.append(student_information)
            
            with open(path_file, "w", encoding = "utf-8") as file:
                content = json.dumps(data, indent = 4, separators = (",", ":"))
                file.write(content)
            
        print(f"El/La estudiante {student_information["full_name"]} se registró correctamente.")
        
    except:
        print("ERROR: Ha ocurrido un error al intentar registrar la información del estudiante.")


def obtain_students_information():
  
    try:
        path_file = utilities.obtain_path_file()
        file_exists = utilities.validate_if_file_exists(path_file)
        file_is_empty = utilities.validate_if_file_is_empty(path_file)
        
        if not file_exists or not file_is_empty:
            print("ADVERTENCIA: No se puede mostrar la información de los estudiantes debido a que no existe información registrada.")
        else:
            with open(path_file, "r", encoding = "utf-8") as file:
                file_content = file.read()
                json_data = json.loads(file_content)
                
                print("A continuación se muestra la información asociada a cada uno de los estudiantes: ")
                
                for student in json_data:
                    print(student)
    except:
        print("ERROR: Se ha producido un error al intentar mostrar la información de todos los estudiantes.")


def obtain_average_top_three():
    try:  
        path_file = utilities.obtain_path_file()
        file_exists = utilities.validate_if_file_exists(path_file)
        file_is_empty = utilities.validate_if_file_is_empty(path_file)
        
        if not file_exists or not file_is_empty:
            print("ADVERTENCIA: No se puede mostrar la información de los tres estudiantes con mejor promedio, debido a que no existe información registrada.")
        else:
            students_average = utilities.calculate_average_per_student()
            sorted_information = sorted(students_average, key = lambda x: (x["average"]), reverse = True)
            
            print("A continuación se listan los estudiantes del top 3 con mejores calificaciones promedio: ")
            
            for index  in range(0, 3):
                print(f"El/la estudiante: {sorted_information[index]["full_name"]} tiene una calificación promedio de: {sorted_information[index]["average"]}")
    except:
        print("ERROR: Ha ocurrido un error al obtener el top tres de las mejores calificaciones promedio.")


def print_students_average():
    total_average = 0
    total_students = 0
    total = 0
    
    try:
        path_file = utilities.obtain_path_file()
        file_exists = utilities.validate_if_file_exists(path_file)
        file_is_empty = utilities.validate_if_file_is_empty(path_file)
        
        if not file_exists or not file_is_empty:
            print("ADVERTENCIA: No se puede mostrar el promedio de notas entre todos los estudiantes, debido a que no existe información registrada.")
        else:
            students:list = utilities.calculate_average_per_student()
            
            for student in students:
                total_students += 1
                total_average += student["average"]
                total = total_average / total_students
            print(f"La nota promedio entre todos los estudiantes es de: {total:.2f}")

    except:
        print("ERROR: Ha ocurrido un error al obtener la nota promedio de todos los estudiantes.")