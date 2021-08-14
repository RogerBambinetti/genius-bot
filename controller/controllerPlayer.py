from model.player import Player
from model.daoPlayer import PlayerDao


class ControllerPlayer:

    def __init__(self):
        self.__dao = PlayerDao

    def insert(self, name, username):
        player = Player(name, username)
        return self.__dao.insert(player)

    def update(self, id: int, name=None, username=None):
        player = self.__dao.read(id)

        if name:
            player.name = name
        if username:
            player.username = username

        return self.__dao.update(player)

    def delete(self, id: int):
        player = self.__dao.read(id)
        return self.__dao.delete(player)

    def read(self, id: int):
        return self.__dao.read(id)

    def list(self):
        return self.__dao.list()
