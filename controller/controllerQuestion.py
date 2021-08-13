from model.question import Question
from model.category import Category
from controller.controllerCategory import ControllerCategory
from model.daoQuestion import Dao
from datetime import date


class ControllerQuestion:
    def __init__(self):
        self.__dao = Dao
        self.__controllerCategory = ControllerCategory()
        self.__view = None

    def insert(self, description, answer, id_category, points, date):
        category = self.__controllerCategory.read(id_category)
        if category:
            question = Question(description, answer, category, points, date)
            self.__dao.insert(question)

    def update(self, id: int, description=None, answer=None, id_category=None, points=None, date=None):
        question = self.__dao.read(id)

        if description:
            question.description = description
        if answer:
            question.answer = answer
        if id_category:
            category = self.__controllerCategory.read(id_category)
            if category:
                question.category = category
        if points:
            question.points = points
        if date:
            question.date = date

        self.__dao.update(question)

    def delete(self, id: int):
        question = self.__dao.read(id)
        self.__dao.delete(question)

    def red(self, id: int):
        return self.__dao.read(id)

    def list(self):
        return self.__dao.list()
