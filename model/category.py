

class Category:

    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

