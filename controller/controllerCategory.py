from model.category import Category
from model.daoCategory import CategoryDao


class ControllerCategory:

    def __init__(self):
        self.__dao = CategoryDao

    def insert(self, name):
        category = Category(name)
        return self.__dao.insert(category)

    def update(self, id: int, name=None):
        category = self.__dao.read(id)
        if name:
            category.name = name
        return self.__dao.update(category)

    def delete(self, id: int):
        category = self.__dao.read(id)
        return self.__dao.delete(category)

    def read(self, id: int):
        return self.__dao.read(id)

    def list(self):
        return self.__dao.list()
