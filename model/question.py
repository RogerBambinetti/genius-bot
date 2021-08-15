from model.category import Category
from datetime import date


class Question:

    def __init__(self, description: str, answer: str, category: Category, points: int, date: date):
        self.__id = None
        self.__description = description
        self.__answer = answer
        if isinstance(category, Category):
            self.__category = category
        else:
            raise TypeError
        self.__points = points
        self.__date = date

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, answer: str):
        self.__answer = answer

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: Category):
        self.__category = category

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points: int):
        self.__points = points

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    def __str__(self):
        string = f'id: {self.__id} \n'
        string += f'descrição: {self.__description} \n'
        string += f'resposta: {self.__answer} \n'

        return string
