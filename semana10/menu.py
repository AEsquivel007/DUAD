import actions
import data


def select_option(action):
    match action:
        case 1:
            actions.register_student_information()
        case 2:
            actions.obtain_students_information()
        case 3:
            actions.obtain_average_top_three()
        case 4:
            actions.print_students_average()
        case 5:
            data.export_data_to_csv_file()
        case 6:
            data.import_data_from_csv_file()
