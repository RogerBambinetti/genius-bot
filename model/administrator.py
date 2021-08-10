class Administrator:
    def __init__(self, name, username, email, password):
        super().__init__(name, username)
        self.__email = email
        self.__password = password

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