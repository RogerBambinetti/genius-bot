from view.viewAdministrator import ViewAdministrator
from view.viewQuestion import ViewQuestion
from view.viewCategory import ViewCategory


class ViewSystem():
    def __init__(self):
        self.__view_category = ViewCategory()
        self.__view_question = ViewQuestion()
        self.__view_administrator = ViewAdministrator()

    def main(self):
        print("ESCOLHA UMA OPÇÃO")
        print("1 - Categoria")
        print("2 - Pergunta")
        print("3 - Administrador")
        print("0 - Encerrar sistema")

        option = int(input("Escolha a opção: "))

        if option == 1:
            self.__view_category.options()
        elif option == 2:
            self.__view_question.options()
        elif option == 3:
            self.__view_administrator.options()
        elif option == 0:
            exit()
        else:
            print("Inválido")
