from model.category import Category
from model.daoCategory import CategoryDao
from exception.NotExistsException import NotExistsException


class ControllerCategory:

    def __init__(self):
        self.__dao = CategoryDao

    def insert(self, name):
        if isinstance(name, str):
            category = Category(name)
            return self.__dao.insert(category)
        else:
            raise TypeError

    def update(self, id: int, name: str):
        if isinstance(id, int):
            category = self.__dao.read(id)
            if category:
                if name:
                    if isinstance(name, str):
                        category.name = name
                    else:
                        raise TypeError
                return self.__dao.update(category)
            else:
                raise NotExistsException
        else:
            raise TypeError

    def delete(self, id: int):
        if isinstance(id, int):
            category = self.__dao.read(id)
            if category:
                return self.__dao.delete(category)
            else:
                raise NotExistsException
        else:
            raise TypeError

    def read(self, id: int):
        if isinstance(id, int):
            category = self.__dao.read(id)
            if category:
                return category
            else:
                raise NotExistsException
        else:
            raise TypeError

    def list(self):
        return self.__dao.list()
