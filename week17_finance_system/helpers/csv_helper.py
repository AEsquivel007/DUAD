import os


def validate_if_file_exists(path):
    try:      
        file_exists = os.path.exists(path)
        
        if file_exists:    
            return True
        return False
    except:
        print("[ERROR]: An error occurred when validating the existence of a file!!!")


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
        print("ERROR: An error occurred when trying to validate the length of a file!!!")


def return_category_csv_path_file():
    path_file = "./week17_finance_system/data/categories.csv"
    return path_file


def return_movement_csv_path_file():
    path_file = "./week17_finance_system/data/movements.csv"
    return path_file