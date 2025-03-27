from student import Student
import utilities
import csv


class StudentSystem:
    def __init__(self):
        self.students = {}
        self.csv_file = "students.csv"
    
    
    def create_student(self, id:int, full_name:str, section:str, scores:list):
        if id in self.students:
            print(f"WARNING: The student with ID: {id} already exists.")
            return
        
        student = Student(id, full_name, section)
        student.add_scores(scores)
        self.students[id] = student
        
        print(f"Student '{full_name}' successfully registered!!!")
    
    
    def obtain_students_information(self):
        if not self.students:
            print("WARNING: We're sorry, we cannot display information due to there is no information yet.")
            return
        for student in self.students.values():
            print(student)
    

    def obtain_average_top_three(self):
        if not self.students:
            print("WARNING: We're sorry, we cannot display information due to there is no information yet.")
            return
        sorted_information = sorted(self.students.values(), key = lambda x: x.calculate_student_average(), reverse = True)[:3]
        
        for student in sorted_information:
            print(f"The student '{student.full_name}' has an average of: {student.calculate_student_average()}")
    
    
    def print_students_average(self):
        if not self.students:
            print("WARNING: We're sorry, we cannot display information due to there is no information yet.")
            return
        students_average = 0
        total_students = 0
        averages = 0
        for student in self.students.values():
            total_students += 1
            averages += student.calculate_student_average()
        students_average = averages / total_students
        
        print(f"The average among all students is: {students_average:.2f}")
    
    
    def export_data_to_csv_file(self):
        try:
            csv_path = utilities.obtain_csv_path_file()
            
            if not self.students:
                print("WARNING: We're sorry, we cannot export the information due to there is no information yet.")
            else:
                headers = ["Id", "Full Name", "Section", "Spanish", "English", "Geography", "Sciences"]
                with open(csv_path, "w", encoding = "utf-8", newline = "") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(headers)

                    for student in self.students.values():
                        row = [student.id, student.full_name, student.section] + list(student.scores)
                        writer.writerow(row)           
                
                print(f"Data exported successfully into the file: '{csv_path}'.")
        except Exception as ex:
            print("ERROR: An unexpected error occurred when exporting the information into a .csv file")
            print(f"System error: {ex}")


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
                
                print("Data imported successfully.")
            else:
                print(f"WARNING: The information cannot be imported due to the '.csv' file does not exist.")
        
        except Exception as ex:
            print("ERROR: An unexpected error occurred when importing the information from a .csv file")
            print(f"System error: {ex}")

