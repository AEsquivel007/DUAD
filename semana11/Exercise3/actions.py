from student_system import StudentSystem

student_system = StudentSystem()

def register_student_information():
    counter = 0
    
    try:
        while True:
            user_input = input("How many students would you like to register in the system?: ")
            if user_input.isdigit():
                total_of_students = int(user_input)
                while counter < total_of_students:
                    create_student(counter)
                    counter += 1
                break
            else:
                print("ERROR: You must enter a positive integer!!!")
    except Exception as ex:
        print(f"We're sorry, an unexpected error occurred.")
        print(f"System error: {ex}")
        exit()


def create_student(counter):
    
    subjects = {
        "spanish": "spanish", 
        "english": "english", 
        "geography": "geography", 
        "science": "science"
    }
    
    try:
        scores = []
        while True:
            id = input(f"What's the ID of the {counter + 1}° student?: ")
            if id.isdigit():
                student_id = int(id)
                break
            print("ERROR: The student's ID must contain only numbers!!!")
        
        while True:
            full_name = input(f"What's the full name of the {counter + 1}° student?: ")
            if full_name.replace(" ", "").isalpha():
                break
            print("ERROR: The student's name must contain only strings!!!")
        
        while True:
            student_section = input(f"Which is the section of {full_name}?: ")
            if student_section.isalnum():
                break
            print("ERROR: Only strings and numbers are allowed!!!")   
        
        for subject in subjects.values():

            while True:
                given_score = input(f"What's the grade for the {subject} subject?: ")
                
                if given_score.isdigit():
                    score = int(given_score)
                    
                    if score >= 0 and score <= 100:
                        scores.append(score)
                        break
                    else:
                        print(f"WARNING: You've to provide a grade between '0' to '100' for {subject}.")
                else:
                    print(f"ERROR: The provided grade for {subject} must contain only numbers!!!")
        
        student_system.create_student(student_id, full_name, student_section, scores)
    
    except Exception as ex:
        print("WARNING: An error occurred when trying to register the student, please, try it again later.")
        print(f"System error: {ex}")
        exit()


def obtain_students_information():
    
    try:
        student_system.obtain_students_information()
    except:
        print("ERROR: An unexpected error occurred when trying to display the students information!!!")


def obtain_average_top_three():
    try:  
        student_system.obtain_average_top_three()
    except:
        print("ERROR: An unexpected error occurred when fetching the top three best average ratings!!!")


def print_students_average():
    try:  
        student_system.print_students_average()

    except:
        print("ERROR: An unexpected error occurred when fetching the average between all the students!!!")


def export_to_csv():
    try:  
        student_system.export_data_to_csv_file()

    except:
        print("ERROR: An unexpected error occurred when exporting the student's information into a '.csv' file!!!")


def import_from_csv():
    try:  
        student_system.import_data_from_csv_file()

    except:
        print("ERROR: An unexpected error occurred when importing the student's information from a '.csv' file!!!")