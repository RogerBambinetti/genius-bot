from model.daoAdministrator import Dao
from model.administrator import Administrator


class ControllerAdministrator:
    def __init__(self):
        self.__dao = Dao
        self.__view = None

    def insert(self, name, username, email, password):
        administrator = Administrator(name, username, email, password)
        self.__dao.insert(administrator)

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

        self.__dao.update(administrator)

    def delete(self, id: int):
        administrator = self.__dao.read(id)
        self.__dao.delete(administrator)

    def red(self, id: int):
        return self.__dao.read(id)

    def list(self):
        return self.__dao.list()
