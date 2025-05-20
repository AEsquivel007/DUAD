import FreeSimpleGUI as sg

def show_main_window():

    #Here we define the elements that will be shown on the GUI.
    #Note that here we define a list of lists (separating each list by comma).
    layout = [
        [sg.Text("Congratulations for creating the first GUI!!!!!!")],
        [sg.Text("Name:"),sg.InputText()],
        [sg.Button("Aceptar"), sg.Button("Cancelar")],
        [sg.Button("Cerrar")]
    ]


    #Here we create the window where we'll show the elements ("layout")
    window = sg.Window("First GUI", layout)


    #Here we create and infinite loop to render the GUI
    #Processing the events and obtaining the values from inputs
    #This structure is the same always.

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cerrar":
            break
        elif event == "Aceptar":
            show_second_window()

    window.close()


def show_second_window():

    #Here we define the elements that will be shown on the GUI.
    #Note that here we define a list of lists (separating each list by comma).
    layout = [
        [sg.Text("Congratulations for opening a second window!!!!!!")],
        [sg.Text("Name:"),sg.InputText()],
        [sg.Button("Aceptar"), sg.Button("Regresar")],
    ]


    #Here we create the window where we'll show the elements ("layout")
    window = sg.Window("First GUI", layout)


    #Here we create and infinite loop to render the GUI
    #Processing the events and obtaining the values from inputs
    #This structure is the same always.

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cerrar":
            break
        elif event == "Regresar":
            window.close()
            show_main_window()
    window.close()


if __name__ == "__main__":
    show_main_window()