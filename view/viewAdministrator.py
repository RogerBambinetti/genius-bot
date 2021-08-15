from controller.controllerAdministrator import ControllerAdministrator


class ViewAdministrator():
    def __init__(self):
        self.__controller_administrator = ControllerAdministrator()

    def options(self):
        try:
            print('-------- ADMINISTRADOR ----------')
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
            name = input('Nome: ')
            username = input('Username: ')
            email = input('Email: ')
            password = input('Senha: ')

            return self.__controller_administrator.insert(name, username, email, password)
        except TypeError:
            print('Valores inválidos')

    def update(self):
        try:
            id = int(input('Identificador: '))

            print('Preencher apenas os campos que deseja alterar: ')
            print()
            name = input('Nome: ')
            username = input('Username: ')
            email = input('Email: ')
            password = input('Senha: ')

            return self.__controller_administrator.update(
                id, name, username, email, password)
        except TypeError:
            print('Valores inválidos')

    def delete(self):
        try:
            id = int(input('Identificador: '))

            return self.__controller_administrator.delete(id)
        except TypeError or ValueError:
            print('Valores inválidos')

    def list(self):
        list = self.__controller_administrator.list()

        for item in list:
            print(item)
