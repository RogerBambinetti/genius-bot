from controller.controllerCategory import ControllerCategory


class ViewCategory():
    def __init__(self):
        self.__controller_category = ControllerCategory()

    def options(self):
        print("-------- CATEGORIA ----------")
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
        name = input("Nome: ")

        return self.__controller_category.insert(name)

    def update(self):
        id = input('Identificador: ')

        print("Preencher apenas os campos que deseja alterar: ")
        name = input("Nome: ")

        return self.__controller_category.update(id, name)

    def delete(self):
        id = input('Identificador: ')

        return self.__controller_category.delete(id)

    def list(self):
        return self.__controller_category.list()
