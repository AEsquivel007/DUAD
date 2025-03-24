from student_system import StudentSystem

student_system = StudentSystem()

def register_student_information():
    counter = 0
    
    try:
        while True:
            user_input = input("Ingrese el total de estudiantes a los que les desea registrar la información en el sistema: ")
            if user_input.isdigit():
                total_of_students = int(user_input)
                while counter < total_of_students:
                    create_student(counter)
                    counter += 1
                break
            else:
                print("ERROR: Debe ingresar un número entero positivo. ")
    except:
        print("Lo sentimos, ha ocurrido un error inesperado en el sistema.")
        exit()


def create_student(counter):
    
    subjects = {
        "spanish": "español", 
        "english": "inglés", 
        "geography": "geografía", 
        "science": "ciencias"
    }
    
    try:
        scores = []
        while True:
            id = input(f"Ingrese número de cédula del {counter + 1}° estudiante: ")
            if id.isdigit():
                student_id = int(id)
                break
            print("ERROR: La cédula del estudiante solo debe contener números.")
        
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
        
        for subject in subjects.values():

            while True:
                given_score = input(f"Ingrese la calificación de la materia de {subject}: ")
                
                if given_score.isdigit():
                    score = int(given_score)
                    
                    if score >= 0 and score <= 100:
                        scores.append(score)
                        break
                    else:
                        print(f"ERROR: Debe ingresar una nota entre 0 y 100 para la calificación de {subject}.")
                else:
                    print(f"ERROR: La nota ingresada para la asignación de {subject} solo debe contener valores númericos.")
        
        student_system.create_student(student_id, full_name, student_section, scores)
    
    except Exception as ex:
        print("Ha ocurrido un error al intentar registrar el estudiante, inténtelo más tarde.")
        print(f"El error obtenido por el sistema fue: {ex}")
        exit()


def obtain_students_information():
    
    try:
        student_system.obtain_students_information()
    except:
        print("ERROR: Se ha producido un error al intentar mostrar la información de todos los estudiantes.")


def obtain_average_top_three():
    try:  
        student_system.obtain_average_top_three()
    except:
        print("ERROR: Ha ocurrido un error al obtener el top tres de las mejores calificaciones promedio.")


def print_students_average():
    try:  
        student_system.print_students_average()

    except:
        print("ERROR: Ha ocurrido un error al obtener la nota promedio de todos los estudiantes.")


def export_to_csv():
    try:  
        student_system.export_data_to_csv_file()

    except:
        print("ERROR: Ha ocurrido un error al exportar la información de estudiantes a un archivo '.csv'.")


def import_from_csv():
    try:  
        student_system.import_data_from_csv_file()

    except:
        print("ERROR: Ha ocurrido un error al importar la información de estudiantes a un archivo '.csv'.")