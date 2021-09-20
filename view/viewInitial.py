import PySimpleGUI as sg


class ViewInitial():

    def login(self):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Text('Login', font=(25))],
            [sg.Text('Email', size=(15, 1)),
             sg.InputText(key='email')],
            [sg.Text('Senha', size=(15, 1)),
             sg.InputText(key='password')],
            [sg.Submit('OK'), sg.Cancel('Cancelar', key='cancel')]
        ]

        window = sg.Window('Administrador').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['email'], values['password']
        else:
            return False

    def options(self):
        sg.ChangeLookAndFeel('Tan')
        layout_column = [
            [sg.Text('Escolha uma opção', font=(25))],
            [sg.Button('Categoria', key='category', size=(30, 1))],
            [sg.Button('Pergunta', key='question', size=(30, 1))],
            [sg.Button('Administrador', key='administrator', size=(30, 1))],
            [sg.Cancel('Sair', key='cancel')]
        ]

        layout = [[sg.Column(layout_column, element_justification='center')]]

        window = sg.Window('Genius Bot',
                           element_justification='center').Layout(layout)
        button, values = window.Read()
        window.close()

        return button
