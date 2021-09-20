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

    def notExists(self):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Text(
                'Desculpe, não foi possível encontrar nenhum cadastro para finalizar essa operação', font=(5))],
            [sg.Submit('OK')]
        ]

        window = sg.Window(
            'Erro', element_justification="center").Layout(layout)
        button, values = window.Read()

        window.close()
