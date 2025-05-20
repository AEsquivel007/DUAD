import FreeSimpleGUI as sg
from interfaces.main_interface import show_main_window


def show_movement_interface():
    
    layout = [
        [sg.Text("Category:"), sg.Radio("Income", group_id=1, default=True), sg.Radio("Expense", group_id=1)],
        [sg.Text("Description: "), sg.Input(key="description")],
        [sg.Text("Amount ($): "), sg.Input(key="amount")],
        [sg.Text("Date: "), sg.Input(key="date"), sg.CalendarButton("Choose",)],
        [sg.Push(), sg.Button("Add Movement")],
        [sg.Push(), sg.Button("Exit")]
    ]
    
    window = sg.Window("Movement Interface", layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Exit":
            window.close()
            show_main_window()
    
    window.close()