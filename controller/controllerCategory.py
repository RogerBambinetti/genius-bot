from model.category import Category
from model.daoCategory import Dao


class ControllerCategory:

    def __init__(self):
        self.__dao = Dao

    def insert(self, name):
        category = Category(name)
        self.__dao.insert(category)

    def update(self, id: int, name=None):
        category = self.__dao.read(id)
        if name:
            category.name = name
        self.__dao.update(category)

    def delete(self, id: int):
        category = self.__dao.read(id)
        self.__dao.delete(category)

    def read(self, id: int):
        return self.__dao.read(id)

    def list(self):
        return self.__dao.list()
