from model.daoAdministrator import AdministratorDao
from model.administrator import Administrator


class ControllerAdministrator:
    def __init__(self):
        self.__dao = AdministratorDao

    def insert(self, name: str, username: str, email: str, password: str):
        if isinstance(name, str) and isinstance(username, str) and isinstance(email, str) and isinstance(password, str):
            administrator = Administrator(name, username, email, password)
            return self.__dao.insert(administrator)
        else:
            raise ValueError

    def update(self, id: int, name=None, username=None, email=None, password=None):

        administrator = self.__dao.read(id)
        print(administrator)
        print(name)
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
        if isinstance(id, int):
            administrator = self.__dao.read(id)
            return self.__dao.delete(administrator)
        else:
            raise ValueError

    def read(self, id: int):
        if isinstance(id, int):
            return self.__dao.read(id)
        else:
            raise ValueError

    def readByUsername(self, username: str):
        if isinstance(username, str):
            administrators = self.__dao.list()

            for administrator in administrators:
                if(administrator.username == username):
                    return administrator
        else:
            ValueError

    def list(self):
        return self.__dao.list()
