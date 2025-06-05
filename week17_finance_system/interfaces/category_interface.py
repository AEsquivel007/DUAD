import FreeSimpleGUI as sg
from interfaces.main_interface import show_main_window
from helpers.csv_helper import return_category_csv_path_file
from managers.category_manager import CategoryManager
from classes.category import Category


def create_category_window(manager: CategoryManager):
    
    headings = ["Category"]
    
    layout = [
        [sg.Text("List of categories:")],
        [sg.Table(values=manager.get_categories_as_rows(),
                headings=headings,
                key="-TABLE-",
                justification="c",
                expand_x=True,
                expand_y=True,
                size= (50, 10),
                enable_events=True)],
        [sg.Text("Category:"), sg.Input(key="-CATEGORY-")],
        [sg.Push(), sg.Button("Add Category"), sg.Push(), sg.Button("Modify Category"), sg.Push() ,sg.Button("Delete Category"), sg.Push(), sg.Button("Exit"), sg.Push()],
    ]
    return sg.Window("Category Interface", layout)


def validate_input(category_value):
    if not category_value:
        sg.popup_error("Category field is required!")
        return False
    return True


def handle_category_selection(values, manager:CategoryManager, window):
    index = values["-TABLE-"][0]
    category = manager.categories[index]
    
    window["-CATEGORY-"].update(category.category)
    return index


def handle_save_category(manager:CategoryManager):
    manager.save_categories()


def get_form_data(values):
    return values["-CATEGORY-"].strip()


def handle_add_category(values, manager:CategoryManager, window):
    category = get_form_data(values)
    
    if validate_input(category):
        new_category = Category(category)
        manager.add_category(new_category)
        window["-TABLE-"].update(values=manager.get_categories_as_rows())
        window["-CATEGORY-"]("")
        sg.popup("The category was added!")


def handle_modify_category(values, index, manager:CategoryManager, window):
    if index is None:
        sg.popup_error("Select one category to modify it!")
        return
    
    category = get_form_data(values)
    
    if validate_input(category):
        modified_category = Category(category)
        manager.modify_category(index, modified_category)
        window["-TABLE-"].update(values=manager.get_categories_as_rows())
        window["-CATEGORY-"]("")
        sg.popup("The category was modified!")


def handle_delete_category(index, manager:CategoryManager, window):
    if index is None:
        sg.popup_error("Select one category to delete it!")
        return
    
    confirmation = sg.popup_yes_no("Do you want to delete the selected category?")
    
    if confirmation == "Yes":
        manager.delete_category(index)
        window["-TABLE-"].update(values=manager.get_categories_as_rows())
        window["-CATEGORY-"]("")
        sg.popup("The category was deleted!")
        return None
    return index


def handle_exit(window):
    window.close()
    show_main_window()


def handle_x(window):
    window.close()


def show_category_interface():
    file_path = return_category_csv_path_file()
    
    manager = CategoryManager(file_path)
    manager.load_categories()
    
    window = create_category_window(manager)
    index = None
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            handle_x(window)
            break
        elif event == "-TABLE-":
            if values["-TABLE-"]:
                index = handle_category_selection(values, manager, window)
        elif event == "Add Category":
            handle_add_category(values, manager, window)
        elif event == "Modify Category":
            handle_modify_category(values, index, manager, window)
        elif event == "Delete Category":
            handle_delete_category(index, manager, window)
        elif event == "Exit":
            handle_exit(window)
    
    window.close()