import os
import menu


def display_menu():
    try:
        print("""Welcome to the Student's Control System, please select one of the following options:
            1. Register a new student
            2. Display student's information
            3. Calculate student's average top three
            4. Calculate the average among all students
            5. Export data into a '.csv' file
            6. Import data from a '.csv' file""")
        
        given_option:str = input("Select one of the given options (You have to provide the number of the option): ")

        if given_option.isdigit():
            option = int(given_option)

            if option > 0 and option < 7:
                menu.select_option(option)
            else:
                print("The chosen number is invalid, please select one between 1 to 6.")
        else:
            print("Please provide a number as a value, only integers are allowed")
    
    except ValueError as ex:
        print("Sorry, something went wrong when selecting the options.")
        print(f"System error: {ex}")
        exit()


def validate_if_file_exists(path):
    try:      
        file_exists = os.path.exists(path)
        
        if file_exists:    
            return True
        return False
    except Exception as ex:
        print("ERROR: An unexpected error occurred when trying to validate the existence of the file.")
        print(f"System error: {ex}")


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
        print("ERROR: An unexpected error occurred when validating the file length.")


def ask_if_continue():
    try:
        while True:
            user_input = input("Would you like to continue using the system (s/n)?: ")
            
            if user_input not in ["s","n"]:
                print("ERROR: Only (s) or (n) values are allowed...")
            elif user_input == "s":
                return True
            else:
                return False

    except:
        print("ERROR: An unexpected error occurred.")
        print("Thank you.")


def obtain_csv_path_file():
    path_file = "semana11/Exercise3/exported_data_of_students.csv"
    return path_file
