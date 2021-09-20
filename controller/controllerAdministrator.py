from view.viewError import ViewError
from exception.NotExistsException import NotExistsException
from dao.daoAdministrator import AdministratorDao
from model.administrator import Administrator
from view.viewAdministrator import ViewAdministrator


class ControllerAdministrator:
    def __init__(self):
        self.__dao = AdministratorDao
        self.__view = ViewAdministrator()
        self.__viewError = ViewError()

    def options(self):
        option = self.__view.options()

        if option == 'insert':
            self.insert()
        elif option == 'update':
            self.update()
        elif option == 'delete':
            self.delete()
        elif option == 'list':
            self.listView()
        elif option == 'cancel':
            pass

    def insert(self):
        try:
            name, username, email, password = self.__view.insert()
            if isinstance(name, str) and isinstance(username, str) and isinstance(email, str) and isinstance(password, str):
                administrator = Administrator(name, username, email, password)
                self.__dao.insert(administrator)
            else:
                raise TypeError
        except Exception:
            self.__viewError.error()

    def update(self):
        try:
            list = self.__dao.list()
            administrator = self.__view.select(list)
            if administrator:
                name, username, email, password = self.__view.update(
                    administrator)

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

                self.__dao.update(administrator)
            else:
                raise NotExistsException
        except NotExistsException:
            pass
        except Exception:
            self.__viewError.error()

    def delete(self):
        try:
            list = self.__dao.list()
            administrator = self.__view.select(list)

            if administrator:
                confirm = self.__view.delete(administrator)
                if confirm:
                    self.__dao.delete(administrator)
            else:
                raise NotExistsException
        except Exception:
            self.__viewError.error()

    def read(self, id: int):
        try:
            if isinstance(id, int):
                administrator = self.__dao.read(id)
                if administrator:
                    return administrator
                else:
                    raise NotExistsException
        except Exception:
            pass

    def readByUsername(self, username: str):
        try:
            if isinstance(username, str):
                administrators = self.__dao.list()

                for administrator in administrators:
                    if(administrator.username == username):
                        return administrator
                raise NotExistsException
        except Exception:
            pass

    def list(self):
        return self.__dao.list()

    def login(self, email: str, password: str):
        try:
            if isinstance(email, str) and isinstance(password, str):
                user = self.__dao.readByEmail(email)
                if(user):
                    if(user.password == password):
                        return True
                return False
        except Exception:
            pass

    def listView(self):
        list = self.__dao.list()
        self.__view.list(list)
