class User:
    def __init__(self, name, username):
        self.__name = name
        self.__username = username

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