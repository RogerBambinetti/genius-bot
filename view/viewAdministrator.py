import PySimpleGUI as sg


class ViewAdministrator():

    def options(self):
        sg.ChangeLookAndFeel('Tan')
        layout_column = [
            [sg.Text('Escolha uma opção', font=(25))],
            [sg.Button('Inserir', key='insert', size=(30, 1))],
            [sg.Button('Atualizar', key='update', size=(30, 1))],
            [sg.Button('Deletar', key='delete', size=(30, 1))],
            [sg.Button('Listar', key='list', size=(30, 1))],
            [sg.Cancel('Cancelar', key='cancel')]
        ]

        layout = [[sg.Column(layout_column, element_justification='center')]]

        window = sg.Window('Administrador',
                           element_justification='center').Layout(layout)
        button, values = window.Read()
        window.close()

        return button

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
            [sg.Submit('OK'), sg.Cancel('Cancelar', key='cancel')]
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
            [sg.Submit('OK'), sg.Cancel('Cancelar', key='cancel')]
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
            [sg.Submit('OK'), sg.Cancel('Cancelar', key='cancel')]
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
            [sg.Submit('OK'), sg.Cancel('Cancelar', key='cancel')]
        ]

        window = sg.Window('Administrador').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['administrator']
        else:
            return False

    def list(self, list):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Listbox(list, size=(60, 15))],
            [sg.Button('OK')]
        ]

        window = sg.Window('Administrador').Layout(layout)
        button, values = window.Read()

        window.close()
