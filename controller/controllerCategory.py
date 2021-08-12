from model.category import Category
from model.daoCategory import Dao


class ControllerCategory:

    def __init__(self):
        self.__dao = Dao

    def create(self, name: str):
        category = Category(name)
        self.__dao.insert(category)

    def update(self, id: int, name: str):
        category = self.__dao.read(id)
        category.name = name
        self.__dao.update(category)

    def delete(self, id: int):
        category = self.__dao.read(id)
        self.__dao.delete(category)

    def listCategories(self):
        return self.__dao.list()
