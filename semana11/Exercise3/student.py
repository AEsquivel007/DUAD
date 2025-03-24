class Student:
    def __init__(self, id:int, full_name:str, section:str):
        self.id = id
        self.full_name = full_name
        self.section = section
        self.scores = [0, 0, 0, 0]
    
    
    def add_scores(self, scores):
        try:
            if len(scores) > 0:
                self.scores = scores
            else:
                print("ERROR: No se han asignado calificaciones para el estudiante.")
        except Exception as ex:
            print("Ha ocurrido un error al intentar asignar las notas.")
            print(f"Error obtenido: {ex}")
    
    
    def calculate_student_average(self):
        try:
            if not self.scores:
                print("ADVERTENCIA: No se puede calcular el promedio del estudiante, debido a que no tiene calificaciones registradas.")
                return 0
            summed_scores = sum(self.scores)
            total_scores = len(self.scores)
            total = summed_scores / total_scores
            return total
        except Exception as ex:
            print("Ha ocurrido un error al intentar calcular el promedio de notas.")
            print(f"Error obtenido: {ex}")
    
    
    def __str__(self):
        try:
            Spanish, English, Geography, Science = self.scores
            return f"Cédula: {self.id} | Estudiante: {self.full_name} | Sección: {self.section} | Calificaciones obtenidas: Español: {Spanish} | Inglés: {English} | Geografía: {Geography} | Ciencias: {Science}"
        except Exception as ex:
            print("Ha ocurrido un error al intentar la información del estudiante.")
            print(f"Error obtenido: {ex}")
