from model.daoAdministrator import AdministratorDao
from model.administrator import Administrator


class ControllerAdministrator:
    def __init__(self):
        self.__dao = AdministratorDao

    def insert(self, name, username, email, password):
        administrator = Administrator(name, username, email, password)
        return self.__dao.insert(administrator)

    def update(self, id: int, name=None, username=None, email=None, password=None):
        administrator = self.__dao.read(id)

        if name:
            administrator.name = name
        if username:
            administrator.username = username
        if email:
            administrator.email = email
        if password:
            administrator.password = password

        return self.__dao.update(administrator)

    def delete(self, id: int):
        administrator = self.__dao.read(id)
        return self.__dao.delete(administrator)

    def read(self, id: int):
        return self.__dao.read(id)

    def readByUsername(self, username):
        administrators = self.__dao.list()

        for administrator in administrators:
            if(administrator.username == username):
                return administrator

    def list(self):
        return self.__dao.list()
