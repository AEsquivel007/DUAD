import FreeSimpleGUI as sg
from navigation import go_to_category_window, go_to_movement_window
from managers.movement_manager import MovementManager
from helpers.csv_helper import return_movement_csv_path_file


def show_main_window():
    file_path = return_movement_csv_path_file()
    manager = MovementManager(file_path)
    manager.load_movements()
    
    table_headings = ["Category", "Type", "Description", "Amount", "Date"]
    
    main_layout = [
        [sg.Push(), sg.Text("Personal Finance System"), sg.Push()],
        [sg.Push(), sg.Button("Manage Categories"), sg.Push(), sg.Push(), sg.Button("Manage Movements"), sg.Push()],
        [sg.Table(values=manager.get_movements_as_rows(),
                headings=table_headings,
                auto_size_columns=False,
                col_widths=[10,10,40, 10, 10],
                expand_x=True,
                expand_y=True,
                justification="c")],
        [sg.Push(), sg.Button("Exit")]
    ]
    
    window = sg.Window("Personal Financial System", main_layout)
    
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        elif event == "Manage Categories":
            window.close()
            go_to_category_window()
        elif event == "Manage Movements":
            window.close()
            go_to_movement_window()
    
    window.close()