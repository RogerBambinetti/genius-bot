class User:
    def __init__(self, name, username):
        self.__id = None
        self.__name = name
        self.__username = username

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username