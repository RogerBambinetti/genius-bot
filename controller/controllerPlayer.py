from model.player import Player
from model.daoPlayer import PlayerDao


class ControllerPlayer:

    def __init__(self):
        self.__dao = PlayerDao

    def insert(self, name, username):
        player = Player(name, username)
        return self.__dao.insert(player)

    def update(self, id: int, name=None, username=None):
        if isinstance(id, int):
            player = self.__dao.read(id)

            if name:
                player.name = name
            if username:
                player.username = username

            return self.__dao.update(player)
        else:
            raise TypeError

    def delete(self, id: int):
        if isinstance(id, int):
            player = self.__dao.read(id)
            return self.__dao.delete(player)
        else:
            raise TypeError

    def read(self, id: int):
        if isinstance(id, int):
            return self.__dao.read(id)
        else:
            raise TypeError

    def readByUsername(self, username):
        players = self.__dao.list()

        for player in players:
            if(player.username == username):
                return player

    def list(self):
        return self.__dao.list()
