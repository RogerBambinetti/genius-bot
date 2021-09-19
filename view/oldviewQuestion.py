from controller.controllerCategory import ControllerCategory
from controller.controllerQuestion import ControllerQuestion
from datetime import date


class ViewQuestion():
    def __init__(self):
        self.__controller_question = ControllerQuestion()
        self.__controller_category = ControllerCategory()

    def options(self):
        try:
            print('-------- PERGUNTA ----------')
            print()
            print('1 - Inserir')
            print('2 - Editar')
            print('3 - Excluir')
            print('4 - Listar')
            print('0 - Retornar')

            option = int(input('Digite a opção: '))
            if option == 1:
                return self.insert()
            elif option == 2:
                return self.update()
            elif option == 3:
                return self.delete()
            elif option == 4:
                return self.list()
            elif option == 0:
                return True
            else:
                raise ValueError
        except ValueError:
            print('O valor inserido não é válido, digite um valor válido')

    def insert(self):
        try:
            description = input('Descrição: ')
            answer = input('Resposta: ')
            points = int(input('Pontos: '))

            print('Digite o identificador da Categoria para essa pergunta: ')
            print()
            for category in self.__controller_category.list():
                print(f'Identificador: {category.id}')
                print(f'Nome: {category.name}')
                print()
            id_category = int(input('Identificador: '))
            return self.__controller_question.insert(
                description, answer, id_category, points, date.today())
        except TypeError:
            print('Valores inválidos')

    def update(self):
        try:
            id = int(input('Identificador: '))

            description = input('Descrição: ')
            answer = input('Resposta: ')
            points = input('Pontos: ')
            points = int(points) if points else points

            print('Digite o identificador da Categoria para essa pergunta: ')
            print()
            for category in self.__controller_category.list():
                print(f'Identificador: {category.id}')
                print(f'Nome: {category.name}')
                print()
            id_category = input('Identificador: ')
            id_category = int(id_category) if id_category else id_category

            return self.__controller_question.update(
                id, description, answer, id_category, points, date.today())
        except TypeError:
            print('Valores inválidos')

    def delete(self):
        try:
            id = int(input('Identificador: '))
            return self.__controller_question.delete(id)
        except TypeError:
            print('Valores inválidos')

    def list(self):
        list = self.__controller_question.list()

        for item in list:
            print(item)
