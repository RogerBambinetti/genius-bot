from view.viewError import ViewError
from view.viewCategory import ViewCategory
from model.category import Category
from dao.daoCategory import CategoryDao
from exception.NotExistsException import NotExistsException
import PySimpleGUI as sg


class ControllerCategory:

    def __init__(self):
        self.__dao = CategoryDao
        self.__view = ViewCategory()
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
            name = self.__view.insert()
            if name:
                if isinstance(name, str):
                    category = Category(name)
                    self.__dao.insert(category)
                else:
                    raise TypeError
        except Exception:
            self.__viewError.error()

    def update(self):
        try:
            list = self.__dao.list()
            category = self.__view.select(list)

            if category:
                name = self.__view.update(category)
                if name:
                    if isinstance(name, str):
                        category.name = name
                    else:
                        raise TypeError
                    self.__dao.update(category)
            else:
                raise NotExistsException
        except NotExistsException:
            pass
        except Exception:
            self.__viewError.error()

    def delete(self):
        try:
            list = self.__dao.list()
            category = self.__view.select(list)

            if category:
                confirm = self.__view.delete(category)
                if confirm:
                    self.__dao.delete(category)
            else:
                raise NotExistsException
        except NotExistsException:
            pass
        except Exception:
            self.__viewError.error()

    def read(self, id: int):
        try:
            if isinstance(id, int):
                category = self.__dao.read(id)
                if category:
                    return category
            else:
                raise TypeError
        except Exception:
            pass

    def listView(self):
        list = self.__dao.list()
        self.__view.list(list)

    def list(self):
        return self.__dao.list()
