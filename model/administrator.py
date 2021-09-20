from model.user import User


class Administrator(User):
    def __init__(self, name: str, username: str, email: str, password: str):
        super().__init__(name, username)
        self.__email = email
        self.__password = password

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    def __str__(self):
        string = f'nome: {self.name} \n'
        string += f'username: {self.username} \n'
        string += f'e-mail: {self.__email} \n'

        return string
