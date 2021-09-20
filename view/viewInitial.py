import PySimpleGUI as sg


class ViewInitial():

    def options(self):
        sg.ChangeLookAndFeel('Tan')
        layout_column = [
            [sg.Text('Escolha uma opção', font=(25))],
            [sg.Button('Categoria', size=(30, 1))],
            [sg.Button('Pergunta', size=(30, 1))],
            [sg.Button('Administrador', size=(30, 1))],
            [sg.Cancel('Cancelar')]
        ]

        layout = [[sg.Column(layout_column, element_justification='center')]]

        window = sg.Window('Genius Bot', size=(800, 800),
                           element_justification='center').Layout(layout)
        button, values = window.Read()
