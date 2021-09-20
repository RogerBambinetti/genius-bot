from view.viewInitial import ViewInitial
from controller.controllerQuestion import ControllerQuestion
from controller.controllerCategory import ControllerCategory
from controller.controllerAdministrator import ControllerAdministrator


class Initial():
    def __init__(self):
        self.__controller_question = ControllerQuestion()
        self.__controller_category = ControllerCategory()
        self.__controller_administrator = ControllerAdministrator()
        self.__view = ViewInitial()

    def options(self):
        while True:
            option = self.__view.options()

            if option == 'category':
                self.__controller_category.options()
            elif option == 'question':
                self.__controller_question.options()
            elif option == 'administrator':
                self.__controller_administrator.options()
            elif option == 'cancel':
                exit()
