

class Category:

    def __init__(self, name: str):
        self.__id = None
        self.__name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def __str__(self):
        string = f'Nome: {self.__name} \n'

        return string
