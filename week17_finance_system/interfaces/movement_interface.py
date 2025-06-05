import FreeSimpleGUI as sg
from interfaces.main_interface import show_main_window
from helpers.csv_helper import *
from managers.movement_manager import MovementManager
from managers.category_manager import CategoryManager
from classes.movement import Movement
from navigation import go_to_category_window, go_to_main_window


def create_movements_window(movement_manager:MovementManager, category_manager:CategoryManager, types):
    
    headings = ["Category", "Type", "Description", "Amount", "Date"]
    
    layout = [
        [sg.Text("List of movements: ")],
        [sg.Table(values=movement_manager.get_movements_as_rows(),
                headings=headings,
                key="-TABLE-",
                justification="c",
                expand_x=True,
                expand_y=True,
                auto_size_columns=False,
                col_widths=[10,10,40, 10, 10],
                enable_events=True,),],
        [sg.Text("Select Category:"), sg.Combo(values=category_manager.get_categories(), key="-COMBO-", readonly=True)],
        [sg.Text("Select Type: ")] + [sg.Radio(movement_type, group_id=1, key=f"-TYPE-{movement_type}-") for movement_type in types],
        [sg.Text("Description: "), sg.Input(key="-DESCRIPTION-")],
        [sg.Text("Amount ($): "), sg.Input(key="-AMOUNT-", size=(20,1))],
        [sg.Text("Select Date:"), sg.Input(key="-DATE-", size=(20,1)), sg.CalendarButton("Choose",format="%Y-%m-%d")],
        [sg.Push(), sg.Button("Add Movement"), sg.Push(), sg.Button("Modify Movement"), sg.Push() ,sg.Button("Delete Movement"), sg.Push(), sg.Button("Exit"), sg.Push()],
    ]
    
    return sg.Window("Movement Interface", layout)


def validate_input(category_value, movement_type, description_value, amount_value:float, date_value):
    if not category_value or not movement_type or not description_value or not amount_value or not date_value:
        sg.popup_error("All fields are required!")
        return False
    try: 
        float(amount_value)
    except ValueError:
        sg.popup_error("Amount value must be a number!")
        return False
    return True


def handle_movement_selection(values, movement_manager:MovementManager, window):
    index = values["-TABLE-"][0]
    movement = movement_manager.movements[index]
    radio_button_key = f"-TYPE-{movement.movement_type}-"
    
    window["-COMBO-"].update(movement.category)
    window["-DESCRIPTION-"].update(movement.description)
    window["-AMOUNT-"].update(float(movement.amount))
    window["-DATE-"].update(movement.date)
    
    if radio_button_key in window.AllKeysDict:
        window[radio_button_key].update(value=True)
    
    return index


def handle_save_movement(manager:MovementManager):
    manager.save_movements()


def get_selected_type(values, types):
    return next((movement_type for movement_type in types if values.get(f"-TYPE-{movement_type}-")), None)


def get_form_data(values, types):
    selected_type = get_selected_type(values, types)
    return values["-COMBO-"], selected_type, values["-DESCRIPTION-"].strip(), values["-AMOUNT-"].strip(), values["-DATE-"].strip()


def reset_radio_buttons(window, types):
    for movement_type in types:
        radio_button_key = f"-TYPE-{movement_type}-"
        if radio_button_key in window.AllKeysDict:
            window[radio_button_key].update(value=False)


def clean_inputs(window, types):
    
    window["-COMBO-"]("")
    window["-DESCRIPTION-"]("")
    window["-AMOUNT-"]("")
    window["-DATE-"]("")
    reset_radio_buttons(window, types)


def handle_add_movement(values, manager:MovementManager, window, types):
    category, movement_type, description, amount, date  = get_form_data(values, types)
    
    if validate_input(category, movement_type, description, amount, date):
        new_movement = Movement(category, movement_type, description, float(amount), date)
        manager.add_movement(new_movement)
        window["-TABLE-"].update(values=manager.get_movements_as_rows())
        clean_inputs(window, types)
        sg.popup("The movement was added!")


def handle_modify_category(values, index, manager:MovementManager, window, types):
    if index is None:
        sg.popup_error("Select one movement to modify it!")
        return
    
    category, movement_type, description, amount, date  = get_form_data(values, types)
    
    if validate_input(category, movement_type, description, float(amount), date):
        modified_movement = Movement(category, movement_type, description, float(amount), date)
        manager.modify_movement(index, modified_movement)
        window["-TABLE-"].update(values=manager.get_movements_as_rows())
        clean_inputs(window, types)
        sg.popup("The movement was modified!")


def handle_delete_category(index, manager:MovementManager, window, types):
    if index is None:
        sg.popup_error("Select one movement to delete it!")
        return
    
    confirmation = sg.popup_yes_no("Do you want to delete the selected movement?")
    
    if confirmation == "Yes":
        manager.delete_movement(index)
        window["-TABLE-"].update(values=manager.get_movements_as_rows())
        clean_inputs(window, types)
        sg.popup("The movement was deleted!")
        return None
    return index


def handle_exit(window):
    window.close()
    show_main_window()


def handle_x(window):
    window.close()


def validate_if_categories_exist(manager:CategoryManager, window):
    categories = manager.get_categories()
    
    if not categories:
        confirmation = sg.popup_yes_no("No categories are registered yet, do you want to register at least one?")
    
        if confirmation == "Yes":
            go_to_category_window()
            window.close()
        else:
            go_to_main_window()
            window.close()


def show_movement_interface():
    movement_file_path = return_movement_csv_path_file()
    category_file_path = return_category_csv_path_file()
    
    movement_manager = MovementManager(movement_file_path)
    category_manager = CategoryManager(category_file_path)
    
    movement_manager.load_movements()
    category_manager.load_categories()
    
    types = ["Income", "Expense"]
    index = None
    
    window = create_movements_window(movement_manager, category_manager, types)
    
    validate_if_categories_exist(category_manager, window)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            handle_x(window)
            break
        elif event == "-TABLE-":
                if values["-TABLE-"]:
                    index = handle_movement_selection(values, movement_manager, window)
        elif event == "Add Movement":
                handle_add_movement(values, movement_manager, window, types)
        elif event == "Modify Movement":
            handle_modify_category(values, index, movement_manager, window, types)
        elif event == "Delete Movement":
                handle_delete_category(index, movement_manager, window, types)
        elif event == "Exit":
            handle_exit(window)
    
    window.close()