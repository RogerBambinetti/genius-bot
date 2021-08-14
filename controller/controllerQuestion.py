import random
from model.question import Question
from controller.controllerCategory import ControllerCategory
from model.daoQuestion import QuestionDao


class ControllerQuestion:
    def __init__(self):
        self.__dao = QuestionDao
        self.__controller_category = ControllerCategory()

    def insert(self, description, answer, id_category, points, date):
        category = self.__controller_category.read(id_category)
        if category:
            question = Question(description, answer, category, points, date)
            return self.__dao.insert(question)

    def update(self, id: int, description=None, answer=None, id_category=None, points=None, date=None):
        question = self.__dao.read(id)

        if description:
            question.description = description
        if answer:
            question.answer = answer
        if id_category:
            category = self.__controller_category.read(id_category)
            if category:
                question.category = category
        if points:
            question.points = points
        if date:
            question.date = date

        return self.__dao.update(question)

    def delete(self, id: int):
        question = self.__dao.read(id)
        return self.__dao.delete(question)

    def read(self, id: int):
        return self.__dao.read(id)

    def readRandom(self):
        list = self.__dao.list()

        if(list):
            return random.choice(list)
        else:
            return False

    def list(self):
        return self.__dao.list()
