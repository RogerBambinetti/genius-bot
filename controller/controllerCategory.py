from typing import Type
from model.category import Category
from model.daoCategory import CategoryDao


class ControllerCategory:

    def __init__(self):
        self.__dao = CategoryDao

    def insert(self, name):
        if isinstance(name, str):
            category = Category(name)
            return self.__dao.insert(category)
        else:
            raise TypeError

    def update(self, id: int, name=None):
        if isinstance(id, int):
            category = self.__dao.read(id)
            if name:
                if isinstance(name, str):
                    category.name = name
                else:
                    raise TypeError
            return self.__dao.update(category)
        else:
            raise TypeError

    def delete(self, id: int):
        if isinstance(id, int):
            category = self.__dao.read(id)
            return self.__dao.delete(category)
        else:
            raise TypeError

    def read(self, id: int):
        if isinstance(id, int):
            return self.__dao.read(id)
        else:
            raise TypeError

    def list(self):
        return self.__dao.list()
