from model.player import Player
from model.daoPlayer import Dao


class ControllerPlayer:

    def __init__(self):
        self.__dao = Dao
        self.__view = None

    def insert(self, name, username):
        player = Player(name, username)
        self.__dao.insert(player)

    def update(self, id: int, name=None, username=None):
        player = self.__dao.read(id)

        if name:
            player.name = name
        if username:
            player.username = username

        self.__dao.update(player)

    def delete(self, id: int):
        player = self.__dao.read(id)
        self.__dao.delete(player)

    def red(self, id: int):
        return self.__dao.read(id)

    def list(self):
        return self.__dao.list()
