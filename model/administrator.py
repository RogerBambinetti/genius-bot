from model.user import User

class Administrator(User):
    def __init__(self, name, username, email, password, id=None):
        super().__init__(name, username)
        self.__email = email
        self.__password = password
        
        if(id != None):
            self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password