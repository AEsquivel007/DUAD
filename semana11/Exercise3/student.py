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
                print("ERROR: No grades were assigned.")
        except Exception as ex:
            print("ERROR: An unexpected error occurred while assigning the grades")
            print(f"System error: {ex}")
    
    
    def calculate_student_average(self):
        try:
            if not self.scores:
                print("WARNING: The system cannot calculate the student's average, due to no grades were registered.")
                return 0
            summed_scores = sum(self.scores)
            total_scores = len(self.scores)
            total = summed_scores / total_scores
            return total
        except Exception as ex:
            print("ERROR: An unexpected error occurred while calculating the average.")
            print(f"System error: {ex}")
    
    
    def __str__(self):
        try:
            Spanish, English, Geography, Science = self.scores
            return f"Id: {self.id} | Student: {self.full_name} | Section: {self.section} | Grades: Spanish: {Spanish} | English: {English} | Geography: {Geography} | Sciences: {Science}"
        except Exception as ex:
            print("ERROR: An unexpected error occurred while obtaining the student's information.")
            print(f"System error: {ex}")
