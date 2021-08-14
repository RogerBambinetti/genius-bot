from controller.controllerCategory import ControllerCategory
from controller.controllerQuestion import ControllerQuestion
from datetime import date


class ViewQuestion():
    def __init__(self):
        self.__controller_question = ControllerQuestion()
        self.__controller_category = ControllerCategory()

    def options(self):
        print("-------- PERGUNTA ----------")
        print("1 - Inserir")
        print("2 - Editar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Retornar")

        option = int(input("Escolha a opção: "))
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
            return False

    def insert(self):
        description = input("Descrição: ")
        answer = input("Resposta: ")
        points = input("Pontos: ")

        print('Digite o identificador da Categoria para essa pergunta: ')
        for category in self.__controller_category.list():
            print(f'Identificador: {category.id}')
            print(f'Nome: {category.name}')

        id_category = input('Identificador: ')
        return self.__controller_question.insert(
            description, answer, id_category, points, date.today())

    def update(self):
        id = input('Identificador: ')

        description = input("Descrição: ")
        answer = input("Resposta: ")
        points = input("Pontos: ")

        print('Digite o identificador da Categoria para essa pergunta: ')
        for category in self.__controller_category.list():
            print(f'Identificador: {category.id}')
            print(f'Nome: {category.name}')

        id_category = input('Identificador: ')

        return self.__controller_question.update(
            id, description, answer, id_category, points, date.today())

    def delete(self):
        id = input('Identificador: ')

        return self.__controller_question.delete(id)

    def list(self):
        return self.__controller_question.list()
