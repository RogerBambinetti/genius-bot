import PySimpleGUI as sg


class ViewCategory():

    def options(self):
        sg.ChangeLookAndFeel('Tan')
        pass

    def insert(self):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Text('Insira os valores:')],
            [sg.Text('Nome', size=(15, 1)), sg.InputText(key='name')],
            [sg.Submit('OK'), sg.Cancel('Cancelar')]
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
                'Campos pré-preenchidos com valores originais, altere apenas aqueles que deseja: ')],
            [sg.Text('Nome', size=(15, 1)), sg.InputText(
                category.name, key='name')],
            [sg.Submit('OK'), sg.Cancel('Cancelar')]
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
                'Possui certeza que deseja excluir esse cadastro? : ')],
            [sg.Text(category.name, size=(15, 1), key='category')],
            [sg.Submit('OK'), sg.Cancel('Cancelar')]
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
            [sg.Text('Categorias')], [sg.InputCombo(
                (list), size=(30, 1), key='category')],
            [sg.Submit('OK'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Categoria').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['category']
        else:
            return False

    def list(self, list):
        for item in list:
            print(item)
