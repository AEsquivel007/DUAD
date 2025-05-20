import FreeSimpleGUI as sg
from navigation import go_to_category_window, go_to_movement_window
#from interfaces.category_interface import show_category_interface
#from interfaces.movement_interface import show_movement_interface


def show_main_window():
    
    table_values = [
        ["1", "New AMD 9600X Computer", 3500, "Technology", "16-05-2025"],
    ]
    main_layout = [
        [sg.Text("Personal Finance System")],
        [sg.Button("Add Category"), sg.Button("List Categories")],
        [sg.Button("Add Movement")],
        [sg.Table(table_values, ["Id", "Description", "Amount", "Category", "Date"], auto_size_columns=True,justification="c")],
        [sg.Push(), sg.Button("Exit")]
    ]
    
    window = sg.Window("Personal Financial System", main_layout)
    
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        elif event == "Add Category":
            window.close()
            go_to_category_window()
        elif event == "Add Movement":
            window.close()
            go_to_movement_window()
    
    window.close()