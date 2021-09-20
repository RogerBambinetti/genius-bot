import PySimpleGUI as sg


class ViewInitial():

    def options(self):
        sg.ChangeLookAndFeel('Tan')
        layout_column = [
            [sg.Text('Escolha uma opção', font=(25))],
            [sg.Button('Categoria', key='category', size=(30, 1))],
            [sg.Button('Pergunta', key='question', size=(30, 1))],
            [sg.Button('Administrador', key='administrator', size=(30, 1))],
            [sg.Cancel('Cancelar', key='cancel')]
        ]

        layout = [[sg.Column(layout_column, element_justification='center')]]

        window = sg.Window('Genius Bot',
                           element_justification='center').Layout(layout)
        button, values = window.Read()
        window.close()

        return button
