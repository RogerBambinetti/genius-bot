from view.viewError import ViewError
from model.category import Category
from view.viewQuestion import ViewQuestion
from exception.NotExistsException import NotExistsException
import random
from model.question import Question
from controller.controllerCategory import ControllerCategory
from dao.daoQuestion import QuestionDao
from datetime import date as Date


class ControllerQuestion:
    def __init__(self):
        self.__dao = QuestionDao
        self.__controller_category = ControllerCategory()
        self.__view = ViewQuestion()
        self.__viewError = ViewError()

    def options(self):
        option = self.__view.options()

        if option == 'insert':
            self.insert()
        elif option == 'update':
            self.update()
        elif option == 'delete':
            self.delete()
        elif option == 'list':
            self.listView()
        elif option == 'cancel':
            pass

    def insert(self):
        try:
            categories = self.__controller_category.list()

            description, answer, category, points, date = self.__view.insert(
                categories)
            if isinstance(description, str) and isinstance(answer, str) and isinstance(category, Category) and isinstance(points, int) and isinstance(date, Date):
                if category:
                    question = Question(description, answer,
                                        category, points, date)
                    self.__dao.insert(question)
                else:
                    raise NotExistsException
            else:
                raise TypeError
        except NotExistsException:
            pass
        except Exception:
            self.__viewError.error()

    def update(self):
        try:
            categories = self.__controller_category.list()
            list = self.__dao.list()
            question = self.__view.select(list)

            if question:
                description, answer, category, points, date = self.__view.update(
                    categories, question)

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
                    if category:
                        question.category = category
                    else:
                        raise NotExistsException
                if points:
                    if isinstance(points, int):
                        question.points = points
                    else:
                        raise TypeError
                if date:
                    question.date = date

                self.__dao.update(question)
            else:
                raise NotExistsException
        except NotExistsException:
            pass
        except Exception:
            self.__viewError.error()

    def delete(self):
        try:
            list = self.__dao.list()
            question = self.__view.select(list)

            if question:
                confirm = self.__view.delete(question)
                if confirm:
                    self.__dao.delete(question)
            else:
                raise NotExistsException
        except NotExistsException:
            pass
        except Exception:
            self.__viewError.error()

    def read(self, id: int):
        try:
            if isinstance(id, int):
                question = self.__dao.read(id)
                if question:
                    return question
            else:
                raise TypeError
        except Exception:
            pass

    def readRandom(self):
        try:
            list = self.__dao.list()

            if(list):
                return random.choice(list)
            else:
                return False
        except Exception:
            pass

    def listView(self):
        list = self.__dao.list()
        self.__view.list(list)

    def list(self):
        return self.__dao.list()
