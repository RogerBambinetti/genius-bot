from _typeshed import Self
from view.viewCategory import ViewCategory
from model.category import Category
from dao.daoCategory import CategoryDao
from exception.NotExistsException import NotExistsException


class ControllerCategory:

    def __init__(self):
        self.__dao = CategoryDao
        self.__view = ViewCategory

    def options(self):
        sg.ChangeLookAndFeel('Tan')
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
            pass

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
            pass

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
            pass

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

    def list(self):
        return self.__dao.list()
