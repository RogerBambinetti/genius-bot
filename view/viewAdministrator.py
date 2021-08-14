from controller.controllerAdministrator import ControllerAdministrator


class ViewAdministrator():
    def __init__(self):
        self.__controller_administrator = ControllerAdministrator()

    def options(self):
        print("-------- ADMINISTRADOR ----------")
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
        username = input("Username: ")
        email = input("Email: ")
        password = input("Senha: ")

        return self.__controller_administrator.insert(name, username, email, password)

    def update(self):

        id = input('Identificador: ')

        print("Preencher apenas os campos que deseja alterar: ")
        name = input("Nome: ")
        username = input("Username: ")
        email = input("Email: ")
        password = input("Senha: ")

        return self.__controller_administrator.update(
            id, name, username, email, password)

    def delete(self):

        id = input('Identificador: ')

        return self.__controller_administrator.delete(id)

    def list(self):
        list = self.__controller_administrator.list()

        for item in list:
            print(item)
