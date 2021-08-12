from model.daoAdministrator import Dao
from model.administrator import Administrator

class ControllerAdministrator():
    def __init__(self):
        self.__dao = Dao
        self.__view = None
    
    def insert(self, name, username, email, password):
        administrator =  Administrator(name, username, email, password)
        if self.__dao.insert(administrator):
            print('Inserido com sucesso!')
        else:
            print('Falha ao inserir')

    def update(self, id):
        if self.__dao.update(id):
            print('Editado com sucesso!')
        else:
            print('Falha ao editar')

    def delete(self, administrator):
        if self.__dao.delete(administrator):
            print('Deletado com sucesso!')
        else:
            print('Falha ao deletar')

    def list(self):
        return self.__dao.list()