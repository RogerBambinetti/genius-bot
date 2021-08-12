from controller.controllerAdministrator import ControllerAdministrator

class ViewAdministrator():
    def __init__(self):
        self.__controllerAdministrator = ControllerAdministrator()
    
    def options(self):
        print("-------- ADMINISTRADOR ----------")
        print("1 - Inserir")
        print("2 - Editar")
        print("3 - Exlcuir")
        print("4 - Listar")
        print("0 - Retornar")

        option = int(input("Escolha a opção: "))

        return option


    def insert(self):
        name = input("Nome: ")
        username = input("Username: ")
        email = input("Email: ")
        password = input("Senha: ")

        self.__controllerAdministrator.insert(name, username, email, password)

    def update(self, id):
        print()

    def delete(self, administrator):
        print()