import PySimpleGUI as sg


class ViewCategory():

    def options(self):
        sg.ChangeLookAndFeel('Tan')
        layout_column = [
            [sg.Text('Escolha uma opção.', font=(25))],
            [sg.Button('Inserir', key='insert', size=(30, 1))],
            [sg.Button('Atualizar', key='update', size=(30, 1))],
            [sg.Button('Deletar', key='delete', size=(30, 1))],
            [sg.Button('Listar', key='list', size=(30, 1))],
            [sg.Cancel('Cancelar', key='cancel')]
        ]

        layout = [[sg.Column(layout_column, element_justification='center')]]

        window = sg.Window('Categoria',
                           element_justification='center').Layout(layout)
        button, values = window.Read()
        window.close()

        return button

    def insert(self):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Text('Insira os valores.', font=(25))],
            [sg.Text('Nome', size=(15, 1)),
             sg.InputText(key='name')],
            [sg.Submit('OK'), sg.Cancel('Cancelar', key='cancel')]
        ]

        window = sg.Window('Categoria').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['name']
        else:
            return False

    def update(self, category):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Text(
                'Campos pré-preenchidos com valores originais, altere apenas aqueles que deseja.', font=(25))],
            [sg.Text('Nome', size=(15, 1)), sg.InputText(
                category.name, key='name')],
            [sg.Submit('OK'), sg.Cancel('Cancelar', key='cancel')]
        ]

        window = sg.Window('Categoria').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['name']
        else:
            return False

    def delete(self, category):
        sg.ChangeLookAndFeel('Tan')

        layout = [
            [sg.Text(
                'Possui certeza que deseja excluir esse cadastro?', font=(25))],
            [sg.Text('Categoria', size=(15, 1)),
             sg.Text(category.name, key='category')],
            [sg.Submit('OK'), sg.Cancel('Cancelar', key='cancel')]
        ]

        window = sg.Window('Categoria').Layout(layout)

        button, values = window.Read()
        window.close()
        if button == 'OK':
            return True
        else:
            return False

    def select(self, list):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Text('Categorias', font=(25))], [sg.InputCombo(
                (list), key='category')],
            [sg.Submit('OK'), sg.Cancel('Cancelar', key='cancel')]
        ]

        window = sg.Window('Categoria').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['category']
        else:
            return False

    def list(self, list):
        sg.ChangeLookAndFeel('Tan')

        layout = [
            [sg.Text('Categorias', font=(25))],
            [sg.Listbox(list, size=(100, 10))],
            [sg.Button('OK')]
        ]

        window = sg.Window('Categoria', element_justification="center",
                           grab_anywhere=True).Layout(layout)
        button, values = window.Read()

        window.close()
