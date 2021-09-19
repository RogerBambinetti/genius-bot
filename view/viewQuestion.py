from model.category import Category
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
             sg.InputText(key='description')],
            [sg.Text('Resposta', size=(15, 1)),
             sg.Multiline(size=(35, 3), key='answer')],
            [sg.Text('Pontos', size=(15, 1)), sg.In(key='points')],
            [sg.Text('Categoria', size=(15, 1)), sg.InputCombo(
                (categories), size=(30, 1), key='category')],
            [sg.Submit('OK'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Questão').Layout(layout)
        button, values = window.Read()

        window.close()

        if button == 'OK':
            return values['description'], values['answer'], values['points'], values['category'], Date.today()
        else:
            return False

    def select(self, list):
        sg.ChangeLookAndFeel('Tan')
        layout = [
            [sg.Text('Questões')], [sg.InputCombo(
                (list), size=(30, 1), key='question')],
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
