from model.user import User


class Player(User):
    def __init__(self, name: str, username: str):
        super().__init__(name, username)
