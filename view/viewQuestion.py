import PySimpleGUI as sg
from datetime import date as Date


class ViewQuestion():

    def options(self):
        sg.ChangeLookAndFeel('Tan')
        pass

    def insert(self, categories):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Text('Insira os valores:')],
            [sg.Text('Descrição', size=(15, 1)),
                sg.Multiline(size=(40, 10), key='description')],
            [sg.Text('Resposta', size=(15, 1)),
                sg.InputText(key='answer')],
            [sg.Text('Pontos', size=(15, 1)), sg.In(key='points')],
            [sg.Text('Categoria', size=(15, 1)), sg.InputCombo(
                (categories), size=(30, 1), key='category')],
            [sg.Submit('OK'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Questão').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['description'], values['answer'], values['category'], int(values['points']), Date.today()
        else:
            return False

    def update(self, categories, question):

        sg.ChangeLookAndFeel('Tan')

        layout = [
            [sg.Text(
                'Campos pré-preenchidos com valores originais, altere apenas aqueles que deseja:')],
            [sg.Text('Descrição', size=(15, 1)),
                sg.Multiline(default_text=question.description, size=(35, 3), key='description')],
            [sg.Text('Resposta', size=(15, 1)),
                sg.InputText(question.answer, key='answer')],
            [sg.Text('Pontos', size=(15, 1)), sg.In(
                question.points, key='points')],
            [sg.Text('Categoria', size=(15, 1)), sg.InputCombo(
                (categories), default_value=question.category, size=(30, 1), key='category')],
            [sg.Submit('OK'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Questão').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['description'], values['answer'], values['category'], int(values['points']), Date.today()
        else:
            return False

    def delete(self, question):
        sg.ChangeLookAndFeel('Tan')

        layout = [
            [sg.Text(
                'Possui certeza que deseja excluir esse cadastro? : ')],
            [sg.Text('Questão', size=(15, 1)), sg.Text(
                question.description, key='question')],
            [sg.Text('Categoria', size=(15, 1)), sg.Text(
                question.category.name, key='category')],
            [sg.Submit('OK'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Questão').Layout(layout)

        button, values = window.Read()
        window.close()
        if button == 'OK':
            return True
        else:
            return False

    def select(self, list):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Text('Questões')], [sg.InputCombo(
                (list), key='question')],
            [sg.Submit('OK'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Questão').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['question']
        else:
            return False

    def list(self, list):
        for item in list:
            print(item)
