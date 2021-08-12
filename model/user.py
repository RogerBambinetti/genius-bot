class User:
    def __init__(self, name: str, username: str):
        self.__id = None
        self.__name = name
        self.__username = username

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

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username
