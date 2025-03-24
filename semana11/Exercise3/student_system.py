from student import Student
import utilities
import csv


class StudentSystem:
    def __init__(self):
        self.students = {}
        self.csv_file = "students.csv"
    
    
    def create_student(self, id:int, full_name:str, section:str, scores:list):
        if id in self.students:
            print(f"ADVERTENCIA: El estudiante con Id: {id} ya se encuentra registrado.")
            return
        
        student = Student(id, full_name, section)
        student.add_scores(scores)
        self.students[id] = student
        
        print(f"El estudiante '{full_name}' se registró correctamente.")
    
    
    def obtain_students_information(self):
        if not self.students:
            print("ADVERTENCIA: No se puede mostrar la información de los estudiantes debido a que no existe información registrada.")
            return
        for student in self.students.values():
            print(student)
    

    def obtain_average_top_three(self):
        if not self.students:
            print("ADVERTENCIA: No se puede mostrar la información de los estudiantes debido a que no existe información registrada.")
            return
        sorted_information = sorted(self.students.values(), key = lambda x: x.calculate_student_average(), reverse = True)[:3]
        
        for student in sorted_information:
            print(f"El estudiante '{student.full_name}' tiene un promedio de: {student.calculate_student_average()}")
    
    
    def print_students_average(self):
        if not self.students:
            print("ADVERTENCIA: No se puede mostrar la información de los estudiantes debido a que no existe información registrada.")
            return
        students_average = 0
        total_students = 0
        averages = 0
        for student in self.students.values():
            total_students += 1
            averages += student.calculate_student_average()
        students_average = averages / total_students
        
        print(f"La nota promedio entre todos los estudiantes es de: {students_average:.2f}")
    
    
    def export_data_to_csv_file(self):
        try:
            csv_path = utilities.obtain_csv_path_file()
            
            if not self.students:
                print("ADVERTENCIA: No se puede exportar la información de los estudiantes debido a que no existe información registrada.")
            else:
                headers = ["Cédula", "Nombre Completo", "Sección", "Español", "Inglés", "Geografía", "Ciencias"]
                with open(csv_path, "w", encoding = "utf-8", newline = "") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(headers)

                    for student in self.students.values():
                        row = [student.id, student.full_name, student.section] + list(student.scores)
                        writer.writerow(row)           
                
                print(f"Datos exportados exitosamente en el archivo: '{csv_path}'.")
        except Exception as ex:
            print("ERROR: Ha ocurrido un error al intentar exportar la información al archivo CSV.")
            print(f"El error obtenido por el sistema es: {ex}")


    def import_data_from_csv_file(self):
        csv_path = utilities.obtain_csv_path_file()
        try:
            file_exists = utilities.validate_if_file_exists(csv_path)
            
            if file_exists:
                with open(csv_path, "r", encoding = "utf-8") as csv_file:
                    reader = csv.reader(csv_file)
                    next(reader)
                    
                    for row in reader:
                        student = Student(row[0], row[1], row[2])
                        scores_str = [row[3],row[4], row[5], row[6]]
                        scores = list(map(int, scores_str))
                        student.add_scores(scores)
                        self.students[row[0]] = student
                
                print("Información importada correctamente.")
            else:
                print(f"ADVERTENCIA: No se pueden importar los datos desde el archivo '.csv', debido a que el archivo no existe.")
        
        except:
            print("ERROR: Ha ocurrido un error al intentar importar la información desde un archivo '.CSV'.")

