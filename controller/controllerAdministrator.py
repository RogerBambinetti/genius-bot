from exception.NotExistsException import NotExistsException
from dao.daoAdministrator import AdministratorDao
from model.administrator import Administrator
from view.viewAdministrator import ViewAdministrator


class ControllerAdministrator:
    def __init__(self):
        self.__dao = AdministratorDao
        self.__view = ViewAdministrator

    def insert(self, name: str, username: str, email: str, password: str):
        if isinstance(name, str) and isinstance(username, str) and isinstance(email, str) and isinstance(password, str):
            administrator = Administrator(name, username, email, password)
            return self.__dao.insert(administrator)
        else:
            raise TypeError

    def update(self, id: int, name=None, username=None, email=None, password=None):
        if isinstance(id, int):
            administrator = self.__dao.read(id)
            if administrator:
                if name:
                    if isinstance(name, str):
                        administrator.name = name
                    else:
                        raise TypeError
                if username:
                    if isinstance(username, str):
                        administrator.username = username
                    else:
                        raise TypeError
                if email:
                    if isinstance(email, str):
                        administrator.email = email
                    else:
                        raise TypeError
                if password:
                    if isinstance(password, str):
                        administrator.password = password
                    else:
                        raise TypeError

                return self.__dao.update(administrator)
            else:
                raise NotExistsException
        else:
            raise TypeError

    def delete(self, id: int):
        if isinstance(id, int):
            administrator = self.__dao.read(id)
            if administrator:
                return self.__dao.delete(administrator)
            else:
                raise NotExistsException
        else:
            raise TypeError

    def read(self, id: int):
        if isinstance(id, int):
            administrator = self.__dao.read(id)
            if administrator:
                return administrator
            else:
                raise NotExistsException
        else:
            raise TypeError

    def readByUsername(self, username: str):
        if isinstance(username, str):
            administrators = self.__dao.list()

            for administrator in administrators:
                if(administrator.username == username):
                    return administrator
            raise NotExistsException
        else:
            TypeError

    def list(self):
        return self.__dao.list()

    def login(self, email: str, password: str):
        if isinstance(email, str) and isinstance(password, str):
            user = self.__dao.readByEmail(email)
            if(user):
                if(user.password == password):
                    return True
            return False
        else:
            raise TypeError
