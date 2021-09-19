import PySimpleGUI as sg


class ViewAdministrator():

    def options(self):
        sg.ChangeLookAndFeel('Tan')
        pass

    def insert(self):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Text('Insira os valores:')],
            [sg.Text('Nome', size=(15, 1)),
                sg.InputText(key='name')],
            [sg.Text('Username', size=(15, 1)),
             sg.InputText(key='username')],
            [sg.Text('Email', size=(15, 1)),
             sg.InputText(key='email')],
            [sg.Text('Senha', size=(15, 1)),
             sg.InputText(key='password')],
            [sg.Submit('OK'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Administrador').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['name'], values['username'], values['email'], values['password']
        else:
            return False

    def update(self, administrator):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Text('Insira os valores:')],
            [sg.Text('Nome', size=(15, 1)),
                sg.InputText(administrator.name, key='name')],
            [sg.Text('Username', size=(15, 1)),
             sg.InputText(administrator.username, key='username')],
            [sg.Text('Email', size=(15, 1)),
             sg.InputText(administrator.email, key='email')],
            [sg.Text('Senha', size=(15, 1)),
             sg.InputText(administrator.password, key='password')],
            [sg.Submit('OK'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Administrador').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['name'], values['username'], values['email'], values['password']
        else:
            return False

    def delete(self, administrator):
        sg.ChangeLookAndFeel('Tan')

        layout = [
            [sg.Text(
                'Possui certeza que deseja excluir esse cadastro? : ')],
            [sg.Text('Nome', size=(15, 1)), sg.Text(
                administrator.name, key='name')],
            [sg.Text('Username', size=(15, 1)), sg.Text(
                administrator.username, key='username')],
            [sg.Submit('OK'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Administrador').Layout(layout)

        button, values = window.Read()
        window.close()
        if button == 'OK':
            return True
        else:
            return False

    def select(self, list):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Text('Administradores')], [sg.InputCombo(
                (list), key='administrator')],
            [sg.Submit('OK'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Administrador').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['administrator']
        else:
            return False

    def list(self, list):
        for item in list:
            print(item)
