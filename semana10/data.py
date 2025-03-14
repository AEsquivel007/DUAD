import utilities
import csv
import json
import actions


def export_data_to_csv_file():
    try:
        path_file = utilities.obtain_path_file()
        csv_path = utilities.obtain_csv_path_file()
        file_exists = utilities.validate_if_file_exists(path_file)
        file_is_empty = utilities.validate_if_file_is_empty(path_file)
        
        if not file_exists or not file_is_empty:
            print("ADVERTENCIA: No se puede exportar la información de los estudiantes debido a que no existe información registrada.")
        else:
            with open(path_file, "r", encoding = "utf-8") as file:
                content_file = file.read()
                json_content = json.loads(content_file)
            
            subjects = list(json_content[0]["scores"].keys())
            headers = ["full_name", "student_section"] + subjects

            with open(csv_path, "w", encoding = "utf-8", newline = "") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(headers)

                for student in json_content:
                    row = [student["full_name"], student["student_section"]] + list(student["scores"].values())
                    writer.writerow(row)           
                
            print(f"Datos exportados exitosamente en el archivo: '{csv_path}'.")
    except Exception as ex:
        print("ERROR: Ha ocurrido un error al intentar exportar la información al archivo CSV.")
        print(f"El error obtenido por el sistema es: {ex}")


def import_data_from_csv_file():
    csv_path = utilities.obtain_csv_path_file()
    students = []
    try:
        file_exists = utilities.validate_if_file_exists(csv_path)
        
        if file_exists:
            with open(csv_path, "r", encoding = "utf-8") as csv_file:
                reader = csv.DictReader(csv_file)
                
                for row in reader:
                    student_information = {"full_name" : row["full_name"], "student_section" : row["student_section"], 
                        "scores": {"spanish": row["spanish"], "english" : row["english"], "geography": row["geography"], "science": row["science"]}}
                    students.append(student_information)
                save_imported_data(students)
            
        else:
            print(f"ADVERTENCIA: No se pueden importar los datos desde el archivo '.csv', debido a que el archivo no existe.")
    
    except Exception as ex:
        print("ERROR: Ha ocurrido un error al intentar importar la información desde un archivo '.CSV'.")
        print(f"El error obtenido por el sistema es: {ex}")


def save_imported_data(students_data):
    imported_data_file_path = "semana10/imported_data.csv"
    
    try:
        headers = ["full_name", "student_section", "spanish", "english", "geography", "science"] 
        
        with open(imported_data_file_path, "w", encoding = "utf-8", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            
            for student in students_data:
                row = [student["full_name"], student["student_section"]] + list(student["scores"].values())
                writer.writerow(row)
        print("La información importada se registró correctamente.")

    except Exception as ex:
        print("ERROR: Ha ocurrido un error al intentar guardar la información importada.")
        print(f"El error obtenido por el sistema es: {ex}")