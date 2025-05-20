import FreeSimpleGUI as sg
from interfaces.main_interface import show_main_window
from helpers.csv_helper import return_category_csv_path_file
from managers.category_manager import CategoryManager
from classes.category import Category


def create_category_window(manager: CategoryManager):
    layout = [
        [sg.Text("List of categories:")],
        [sg.Table(values=manager.get_categories_as_rows(),
                headings=["Categories"],
                key="table",
                auto_size_columns=False, 
                display_row_numbers=True, 
                starting_row_number=1, 
                justification="c",
                expand_x=True)],
        [sg.Text("Category:"), sg.Input(key="category")],
        [sg.Push(), sg.Button("Add Category")],
        [sg.Push(), sg.Button("Exit")]
    ]
    return sg.Window("Category Interface", layout)


def handle_category_window(values, manager: CategoryManager, window):
    category_value = values["category"].strip()

    if not category_value:
        sg.popup_error("Category field is required!")
        return
    
    category = Category(category_value)
    manager.add_category(category)
    
    window["table"].update(values=manager.get_categories_as_rows())
    window["category"]("")
    sg.popup("Category added!") 


def handle_save_category(manager: CategoryManager):
    manager.save_categories()


def handle_exit(manager: CategoryManager, window):
    handle_save_category(manager)
    window.close()
    show_main_window()


def show_category_interface():
    file_path = return_category_csv_path_file()
    
    manager = CategoryManager(file_path)
    manager.load_categories()
    
    window = create_category_window(manager)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Add Category":
            handle_category_window(values, manager, window)
        
        elif event == "Exit":
            handle_exit(manager, window)
    
    window.close()