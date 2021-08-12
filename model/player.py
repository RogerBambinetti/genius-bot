from model.user import User

class Player(User):
    def __init__(self, name, username):
        super().__init__(name, username)