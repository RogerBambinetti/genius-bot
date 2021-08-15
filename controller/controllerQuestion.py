import random
from model.question import Question
from controller.controllerCategory import ControllerCategory
from model.daoQuestion import QuestionDao
from datetime import date


class ControllerQuestion:
    def __init__(self):
        self.__dao = QuestionDao
        self.__controller_category = ControllerCategory()

    def insert(self, description: str, answer: str, id_category: int, points: int, date: date):
        if isinstance(description, str) and isinstance(answer, str) and isinstance(id_category, int) and isinstance(points, int) and isinstance(date, date):
            category = self.__controller_category.read(id_category)
            if category:
                question = Question(description, answer,
                                    category, points, date)
                return self.__dao.insert(question)
        else:
            raise TypeError

    def update(self, id: int, description=None, answer=None, id_category=None, points=None, date=None):
        if isinstance(id, int):
            question = self.__dao.read(id)

            if description:
                if isinstance(description, str):
                    question.description = description
                else:
                    raise TypeError
            if answer:
                if isinstance(answer, str):
                    question.answer = answer
                else:
                    raise TypeError
            if id_category:
                if isinstance(id_category, int):
                    category = self.__controller_category.read(id_category)
                    if category:
                        question.category = category
                else:
                    raise TypeError
            if points:
                if isinstance(points, int):
                    question.points = points
                else:
                    raise TypeError
            if date:
                if isinstance(date, date):
                    question.date = date
                else:
                    raise TypeError

            return self.__dao.update(question)
        else:
            raise TypeError

    def delete(self, id: int):
        if isinstance(id, int):
            question = self.__dao.read(id)
            return self.__dao.delete(question)
        else:
            raise TypeError

    def read(self, id: int):
        if isinstance(id, int):
            return self.__dao.read(id)
        else:
            raise TypeError

    def readRandom(self):
        list = self.__dao.list()

        if(list):
            return random.choice(list)
        else:
            return False

    def list(self):
        return self.__dao.list()
