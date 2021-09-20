import PySimpleGUI as sg


class ViewError():

    def error(self):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Text('Desculpe, ocorreu algum erro inesperado na execução', font=(5))],
            [sg.Submit('OK')]
        ]

        window = sg.Window(
            'Erro', element_justification="center").Layout(layout)
        button, values = window.Read()

        window.close()
